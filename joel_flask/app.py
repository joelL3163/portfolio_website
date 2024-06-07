# First we need to import the Flask class
from flask import Flask
from markupsafe import escape

'''Next we need to create an instance of the class.

__name__ is a specialized built-in vairable in Python that
represents the name of the current module and when a python
file is run directly, __name__ is set to __main__'''
app = Flask(__name__)

# use the route decorator to tell Flask which URL should trigger our function
# in this case it's just the default URL
@app.route("/")
# standard python function which returns HTML to display Hello, World to the user
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<username>")
def show_user_profile(username):
    return f'<h1 style="color:blue;">User {escape(username)}</h1>'

@app.route("/volunteering/")
def volunteering():
    return f"""
    <h1 style= "text-align:Center; color:#23324d; font-family: 'Courier New', 'Lucida Console', monospace; padding-top: 30px;">VOLUNTEERING</h1>
    <p style= "text-align:Center; color:23324d; font-family: 'Courier New', 'Lucida Console', monospace;"">volunteering tex</p>
    """

@app.route("/projects/")
def projects():
    return f''

@app.route("/awards/")
def awards():
    return f''

@app.route("/certifications/")
def certifications():
    return f''

@app.route("/interests")
def interests():
    return f''