from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    
    message = ""
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < session['number']:
            message = "Too low! Try again."
        elif guess > session['number']:
            message = "Too high! Try again."
        else:
            message = "Correct! The number was " + str(session['number'])
            session.pop('number')

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
