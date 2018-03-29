from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

caesar_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eeee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form action="/" method="post">
        <label>
            Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <textarea name="text">
        </textarea>
        <input type="submit" value="Submit Query" />
    </form>
    </body>
</html> 
"""

@app.route("/", methods =['POST'])
def index():
    return caesar_form

def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    rot = int(rot)
    encrypted = rotate_string(text, rot)
    return '<h1>' + encrypted + '<h1>'

app.run()