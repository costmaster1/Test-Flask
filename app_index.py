from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/admin")
def admin():
    return render_template('admin/index.html')

@app.route("/admin/admin_pnl")
def admin_pnl():
    return render_template('admin/admin_pnl.html')

@app.route("/user_page")
def user_page():
    return render_template('user_page/index.html')

@app.route("/user_page_users")
def user_page_users():
    return render_template('user_page/user_page.html')

@app.route("/registr_user")
def registr_user():
    return render_template('registr_user/index.html')    


if __name__ == '__main__':
    app.run()
