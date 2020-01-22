# /*
#  * @Author: Krishen.Soobramoney 
#  * @Date: 2020-01-22 13:47:01 
#  * @Last Modified by:   Krishen.Soobramoney 
#  * @Last Modified time: 2020-01-22 13:47:01
#  * @Title - FLASK WEBAPP DEMO
#  */

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')