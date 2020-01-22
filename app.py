# /*
#  * @Author: Krishen.Soobramoney 
#  * @Date: 2020-01-22 13:47:01 
#  * @Last Modified by:   Krishen.Soobramoney 
#  * @Last Modified time: 2020-01-22 13:47:01
#  * @Title - FLASK WEBAPP DEMO
#  */

#imports
from flask import Flask
from flask import render_template

#creating application object
app = Flask(__name__)

#decorators to link functions to urls
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_route')
def new_route():
    return render_template('new_route.html')

#dynamic route page testing
@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)



# start the development server using the run() method
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')