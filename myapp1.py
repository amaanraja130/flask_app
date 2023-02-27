from flask import Flask

app = Flask(__name__)

@app.route('/Welcome')
def Welcome():
    return "Welcome to ABC Corporation"

@app.route('/')
def Name():
    return 'Company Name: ABC Corporation <br/> Location: India <br/> Contact Detail: 999-999-9999'

if __name__=="__main__":
    app.run(host="0.0.0.0")