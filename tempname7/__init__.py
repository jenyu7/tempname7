from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
from utils import db

app = Flask(__name__)
app.secret_key = "235jk-6fa_qwef79034jk"
db.init_db()

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("profile"))
    return render_template("index.html", log = False)

@app.route("/signup")
def signup():
    if "username" in session:
        return redirect(url_for("profile"))
    return render_template("signup.html", log = False)

@app.route("/login")
def login():
    if "username" in session:
        return redirect(url_for("profile"))
    return render_template("login.html", log = False)



@app.route('/signupauth', methods=["GET", "POST"])
def signupauth():

    if "username" not in session:

        try:
            usern = request.form['username']
            passs = request.form['password']
            passc = request.form['confpass']
        except:
            return render_template("index.html")
        
        #passwords dont match
        if passs != passc:
            flash("Passwords don't match")
            return render_template("signup.html", log = False)

        #successful signup
        else:
            if ( db.add_user(usern, passs) == False ):
                flash("Username not good")
                return render_template("signup.html", log = False)

            else:
                session['username'] = usern
                return redirect(url_for('profile'))

    else:
        return redirect(url_for("profile"))

@app.route('/loginauth', methods=['GET', 'POST'])
def loginauth():
    if 'user' in session:
        return redirect('/')

    else:

        try:
            usern = request.form['username']
            passs =  request.form['password']
        except:
            return render_template("index.html", log = False)
            
        #success!
        if db.get_user(usern):

            if db.auth(usern,passs):
                session['username'] = usern
                return redirect(url_for('profile'))

            #can not log in :(
            flash ('thats not the right password')
            return render_template("login.html", log = False)

        else:
            flash ('that person doesnt exist')
            return render_template("login.html", log = False)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('/')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if "username" not in session:
        return render_template("index.html", log = False)
    return render_template("test.html", log = True)


@app.route('/board', methods=["GET", "POST"])
def board():
    if "username" not in session:
        return render_template("index.html", log = False)
    return render_template("board.html", log = True)


# incase of bad routes go back to homepage
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


if __name__ == "__main__":
    app.debug = True  # DISABLE WHEN DONE
    app.run()
