from flask import Flask, render_template, request, session, redirect, url_for, flash
import os


app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("hello"))
    return render_template("index.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():

    if "username" not in session:
        print "lol"
        '''
        users = db.getUsers()

        #username already exists
        if request.form['username'] in users:
            flash("Username already exists")
            return render_template("index.html")

        #passwords dont match
        if request.form.get['password'] != request.form['confpass']:
            flash("Passwords don't match")
            return render_template("index.html")

        #successful signup
        else:
            db.addUser(request.form['username'], request.form['password'])
            session['username'] = request.form['username']
            return redirect(url_for('hello'))
'''
    else:
        flash("Already logged in!")
        return redirect(url_for("hello"))


@app.route('/loggit', methods=['GET', 'POST'])
def loggit():
    if 'user' in session:
        return redirect('/')
    else:
        '''
        users = db.getUsers()

        #success!
        if request.form['username'] in users:
            if request.form['password'] == users[request.form['user']]:
                session['username'] = request.form['username']
                return redirect(url_for('hello'))

            #can not log in :(
            else:
                flash ('thats not the right password')
                return render_template("index.html")

        else:
            flash ('that person doesnt exist')
            return render_template("index.html")
        '''
        print "lol"


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('/')


@app.route('/hello', methods=["GET", "POST"])
def hello():
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
