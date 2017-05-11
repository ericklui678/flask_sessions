# Session is a way to store information unique to a particular client
# Session uses cookies to store some or all of the req information
# When you want to acess and modify data over multiple redirects
# You can use session in both your servery.py file as well as templates
# Even though you have access to the session, you should not abuse the amount of information you store in it. Store only what you need in the session. Once we incorporate a database you should be limiting what you store in sessions to the most minimal amount of data possible

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
 # you need to set a secret key for security purposes
app.secret_key = 'ThisIsSecret'
# routing rules and rest of server.py below
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/users', methods=['POST'])
def create_user():
    print 'Got Post Info'
    # here we add two properties to session to store the name and email
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')
    # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!

@app.route('/show')
def show_user():
    return render_template('index.html')

app.run(debug = True)
