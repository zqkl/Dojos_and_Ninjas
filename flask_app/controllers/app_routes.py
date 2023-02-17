from flask import render_template,request,redirect
# import the class from friend.py
from flask_app.models.Dojo_methods import Dojos
from flask_app.models.Ninja_methods import Ninjas
from flask_app import app

@app.route('/')          
def home_Page():
    dojos = Dojos.show_all_dojos()
    print(dojos)
    return render_template("dojos_homepage.html",dojos=dojos)


@app.route('/add_new_dojo',methods=['POST'])
def add_new_dojo():
    data = {
        "name":request.form["name"]
    }
    

    Dojos.add_new_dojo(data)
    return redirect('/')

@app.route('/display_all_ninjas/<int:id>')
def diplay_ninjas(id):
    ninjas = Ninjas.show_all_ninjas({'id':id})
    return render_template("show_all_ninjas.html",ninjas=ninjas)


@app.route('/create_new_ninja')
def create_ninja():
    dojos = Dojos.show_all_dojos()
    return render_template('create_new_ninja.html',dojos=dojos)

@app.route('/ninja_creating',methods=['POST'])
def ninja_creating():
    print(request.form)
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo":request.form["dojo"]
    }
    Ninjas.create_ninja(data)
    return redirect('/')