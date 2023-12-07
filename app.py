from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Flask app that uses URL parameters to display dynamic content."

@app.route("/dynamic")
def dynamic_content():
    name = request.args.get("name","Guest")
    return f'Hi {name} this is dynamic content'

if __name__=="__main__":
    app.run(host="0.0.0.0")
