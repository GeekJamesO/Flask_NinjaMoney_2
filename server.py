from flask import Flask, session, render_template, redirect, request
from random import randint
app = Flask(__name__)
app.secret_key = "FaLaLalaLa4121"

@app.route('/')
@app.route('/index')
def index():
    gold = 0
    try:
        gold = session['YourGold']
        actions = session['actions']
    except Exception as e:
        gold = 0
        session['YourGold'] = 0
        session['actions'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    verb = request.form['building']
    newGold = 0
    if verb == "Farm":
        newGold = randint(10,20)
    elif verb == "Cave":
        newGold = randint(5,10)
    elif verb == "House":
        newGold = randint(2,5)
    elif verb == "Casino":
        newGold = randint(-50,50)
    str = "Found {} gold in the {}".format(newGold, verb)
    session['actions'] += [ str ]
    session['YourGold'] += newGold
    return redirect('/')

@app.route('/reset', methods=['GET','POST'])
def reset():
    session['actions'] = [ ]
    session['YourGold'] = 0
    return redirect('/')

app.run(debug=True)
