from flask import Flask, render_template, request

app = Flask(__name__)
notes = []  # This list will store the notes


@app.route('/magic', methods=['GET', 'POST'])
def magic():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            notes.append(note)

    return render_template('home.html', notes=notes)



if __name__ == '__main__':
    app.run(debug=True)

    