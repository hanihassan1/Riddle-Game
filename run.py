import os
from flask import Flask,render_template, request, flash, jsonify
import json


app = Flask(__name__)
app.secret_key = "its_secure"

@app.route('/')
def index():
     if request.method=="POST":
        file= open("user_info.txt", "a")
        file.write("Name:{},Age:{},Grade:{}\n"
                  .format(request.form['Name'],request.form['Age'],
                  request.form['Grade']))
        file.close()
        flash("Hello {}, Welcome! Let's get started. Choose a grade.".format(request.form['Name']))
     return render_template("index.html", title = "Home Page")
    
@app.route('/jk_sk')
def jk_sk():
    return render_template("jk_sk.html", title = "jk_sk Page")
    
@app.route('/one_two')
def one_two():
    return render_template("one_two.html", title = "one_two Page")
    
@app.route('/three_four')
def three_four():
    return render_template("three_four.html", title = "three_four Page")
    
@app.route('/five')
def five():
    return render_template("five.html", title = "five Page")
    
    
api_test_list = ["daniel","mais","hani","abhay"]

@app.route('/checkans/api/v1/task', methods=['GET'])
def check_word():
    my_arg = request.args
    ans_to_check = my_arg['word']
    print(ans_to_check)
    if ans_to_check in api_test_list:
        return jsonify({'result':True})
    else:
        return jsonify({'result':False})
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    