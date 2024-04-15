#basic template of flask to get started.

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=3000,host="localhost",debug=True)