from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note = {'title': title, 'content': content}
        notes.append(note)
        return redirect(url_for('index'))  # Przeładuj stronę po dodaniu notatki
    return render_template('index.html', notes=notes)

@app.route('/note/<title>')
def view_note(title):
    # Kod do wyświetlania pojedynczej notatki
    return render_template('note.html', title=title)  # Przykładowe wyświetlenie notatki na innej stronie

if __name__ == '__main__':
    app.run(debug=True)

