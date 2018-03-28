from flask import Flask

app = Flask(_name_)
app.config['DEBUG'] = True

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
    caesar_form = """
    <form action="/caesar" method= POST>
        <label>
            Rotate by:
            <input type="text" name="rot" />
        </label>
        <input type="textarea" name="text"/>
    </form>
    <input type="submit" value="Submit Query" />
    </body>
    """
</html>

@app.route("/")
def.index():
    return "Hello World"

app.run()