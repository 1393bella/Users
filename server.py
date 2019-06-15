from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL('user_flask')
    users = mysql.query_db('SELECT * FROM user_flask.users;')
    return render_template("index.html", all_users=users)

@app.route("/users/new")  
def new_user():
    return render_template("newuser.html")

@app.route("/users/create", methods=['POST'])
def add_users_to_db():
    mysql = connectToMySQL("user_flask")
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"]
    }
    nomadcount = mysql.query_db(query, data  )
    print(nomadcount)
    return redirect("/users/"+str(nomadcount))

@app.route("/users/<id>")  
def new_user_view(id):
    mysql = connectToMySQL('user_flask')
    query = "SELECT * FROM user_flask.users WHERE id=%(id)s;"
    data = {
        "id": id
        }
    user = mysql.query_db(query, data)
    print("hhhhhhhhhhhhhhhhhhhhhhhhh")
    print(user)
    user = user[0]   #мы обозначаем узер через ноль чтобы открыть упаковку . упаковки это квадратные скобки
    return render_template("user4.html", one_user=user)

@app.route("/users/<id>/edit")  
def new_user_edit(id):
    mysql = connectToMySQL('user_flask')
    query = "SELECT * FROM user_flask.users WHERE id=%(id)s;"
    data = {
        "id": id
    }
    user = mysql.query_db(query, data)
    return render_template("users4edit.html", one_user=user[0])

@app.route("/users/<id>/edit", methods=['POST'])  
def new_user_edited(id):
    mysql = connectToMySQL('user_flask')
    query = "UPDATE users SET first_name = %(fn)s ,last_name = %(ln)s, email = %(em)s, updated_at = NOW() WHERE id=%(id)s;"
    data = {
        "id": id,
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"]
    }
    user = mysql.query_db(query, data)
    return redirect("/users/"+id)

            
if __name__ == "__main__":
    app.run(debug=True)

