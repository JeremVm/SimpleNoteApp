
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.form['note']
    notes.append(note)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
