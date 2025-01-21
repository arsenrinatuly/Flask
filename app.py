from flask import (
    Flask, 
    render_template, 
    redirect, 
    request 
)

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def get_home():
        return render_template('base.html')
    
@app.route('/second', methods = ['GET', 'POST'])
def get_login():    
    return render_template('second.html')


@app.route('/third', methods = ['GET', 'POST'])
def get_reg():
    return render_template('third.html')

@app.route('/fourth', methods=['GET','POST'])
def get_fourth():
    return render_template('fourth.html')


if __name__ == '__main__':
    app.run(debug=True)

