from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # pass a dynamic message into the template
    return render_template('index.html', message="Hello from Flask – content updated!")

if __name__ == "__main__":
    app.run(debug=True)