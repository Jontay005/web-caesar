from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
        <!-- create your form here -->

        <form action="encrypt" method="post">
            <label>Rotate By </label>
            <input type="text" name="rot"/>

            <textarea name="text" rows="4" cols="50">
            {0}
            </textarea>
            <input type="submit" />
            

        </form>

        </body>
    </html>
"""

@app.route("/", methods=['GET'])
def index():
    return form.format(...)

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    message = str(request.form['text'])
    rotated = rotate_string(message, rotation)

    return form.format(rotated)
    
    #return '<h1>'  + rotated + '</h1>'
    #return '<h1> Hello Please rotate ' + message + ' ' + rotation +  ' times </h1>'
    #<button type="button">Submit Query</button>
    
app.run()