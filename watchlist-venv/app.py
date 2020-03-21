from flask import Flask
from flask import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    #return "Welcome to My Watchlist!"
    #return u'欢迎来到我的 Watchlist！'
    #return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
    return 'Hello, there!'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s page' % escape(name)


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='uncleben'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'This is test page!'


if __name__ == '__main__':
    app.run(debug=True)