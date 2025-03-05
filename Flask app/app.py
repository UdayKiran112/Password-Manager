from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from auth import check_master_password
from database import get_all_passwords, save_password, delete_password

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"  # Change this to a secure key

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        master_password = request.form.get("password")
        if check_master_password(master_password):
            user = User(id=1)
            login_user(user)
            session["key"] = master_password  # Store master password in session
            return redirect(url_for("dashboard"))
        else:
            flash("❌ Incorrect Master Password!", "danger")
    return render_template("index.html")


@app.route("/dashboard")
@login_required
def dashboard():
    passwords = get_all_passwords()
    return render_template("dashboard.html", passwords=passwords)


@app.route("/add", methods=["POST"])
@login_required
def add_password():
    website = request.form.get("website")
    username = request.form.get("username")
    password = request.form.get("password")

    save_password(website, username, password)
    flash("✅ Password saved successfully!", "success")  # Flash success message
    return redirect(url_for("dashboard"))


@app.route("/get_password/<website>")
@login_required
def get_password(website):
    username, password = retrieve_password(website)
    return render_template(
        "dashboard.html", website=website, username=username, password=password
    )


@app.route("/delete/<int:id>", methods=["POST", "DELETE"])
@login_required
def delete(id):
    delete_password(id)
    flash("❌ Password deleted successfully!", "danger")  # Flash delete message
    return redirect(url_for("dashboard"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop("key", None)
    flash("✅ Logged out successfully!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
