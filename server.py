from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['add_num'] = 0
    if "add_num" not in session:
        session['add_num'] = 0
    else:
        session['add_num'] += 1
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def click():
    session['add_num'] = request.form['add']
    return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
    session['reset_num'] = request.form['reset']
    session.clear()		# clears all keys
    return redirect("/")

@app.route('/plustwo', methods=['POST'])
def plustwo():
    session['add_num'] += 2
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)