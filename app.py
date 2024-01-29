from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # return "Hello world"
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple flask App</title>
    </head>
    <body>
        <h1> Hello world</h1>
        <P>CANGGIH JUGA</P>
    </body>
    </html>
    """
    

if __name__ == "__main__":
    app.run()
