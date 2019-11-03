from flask import Flask, render_template, redirect, request

app = Flask(__name__)

saved_data = {}


@app.route('/')
def route_index():
    note_text = None
    if 'note' in saved_data:
        note_text = saved_data['note']

    return render_template('index.html', note=note_text)


@app.route('/edit-note', methods=['GET', 'POST'])
def route_edit():
    if request.method == 'POST':  # the function is called with POST when we save a note
        saved_data['note'] = request.form['note']
        return redirect('/')  # redirect to the home page which will show the saved note
    note_text = None
    if 'note' in saved_data:
        note_text = saved_data['note']
    return render_template('edit-note.html', note=note_text)


if __name__ == "__main__":
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
