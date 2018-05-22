from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
from utils import db

app = Flask(__name__)
app.secret_key = os.urandom(32)

db.init_db()

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("profile"))
    return render_template("index.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():

    if "username" not in session:
        print "lol"

        #passwords dont match
        if request.form['password'] != request.form['confpass']:
            flash("Passwords don't match")
            return render_template("index.html")

        #successful signup
        else:
            if ( db.add_user(request.form['username'], request.form['password']) ):
                flash("Username not good")
                return render_template("index.html")

            else:
                session['username'] = request.form['username']
                return redirect(url_for('profile'))

    else:
        flash("Already logged!")
        return redirect(url_for("profile"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect('/')

    else:

        usern = request.form['username']
        passs =  request.form['password']

        #success!
        if db.get_user(usern):

            if db.auth(usern,passs):
                return redirect(url_for('profile'))

            #can not log in :(
            else:
                flash ('thats not the right password')
                return render_template("index.html")

        else:
            flash ('that person doesnt exist')
            return render_template("index.html")


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('/')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if "username" not in session:
        return render_template("index.html")
    return render_template("test.html")


# incase of bad routes go back to homepage
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


if __name__ == "__main__":
    app.debug = True  # DISABLE WHEN DONE
    app.run()
