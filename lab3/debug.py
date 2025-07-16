from flask import Flask, render_template, request

app = Flask("my_application")

@app.route('/')
def hello() :
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)
