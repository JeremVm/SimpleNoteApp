from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', notes=notes)

@app.route('/note/<title>')
def view_note(title):
    note = next((n for n in notes if n['title'] == title), None)
    
    if note:
        return render_template('note.html', note=note)
    else:
        return "Note not found", 404

@app.route('/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note = {'title': title, 'content': content}
        notes.append(note)
        return redirect(url_for('index'))  # Przeładuj stronę po dodaniu notatki
    return render_template('new_note.html')
    
if __name__ == '__main__':
    app.run(debug=True)

