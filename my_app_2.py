from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def Class():
    return 'Welcome to the Class!'

@app.route('/profile/<username>')
def profile(username):
    return f'This is {username}'

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('Class'))
        print(url_for('profile', username='Amaan'))
