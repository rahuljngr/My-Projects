from flask import Flask

app = Flask (__name__)

@app.route('/')
def home():
    return 'Welcome to homepage!'

@app.route('/about/')
def page():
    return "About content goes here!"

if __name__=="__main__":
    app.run(debug = True)

#go to browser and open 'localhost:5000'

