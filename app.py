from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Pili ka nga kung talaga.</h1>
    <ul><li><a href='/greet'>Click me please.</a></li>
    <li><a href='/meet'>Meet me please.</a></li>
    <li><a href='/invite'>Invite me please.</a></li>
    <li><a href='/accept'>Accept me please.</a></li></ul>"""

@app.route('/greet')
def greet():
    return "<p>Anong gawa mo</p>"

@app.route('/meet')
def meet():
    return "<p>Tara usap</p>"

@app.route('/invite')
def invite():
    return "<p>Tara gala</p>"

@app.route('/accept')
def accept():
    return "<p>Anong gawa mo</p>"