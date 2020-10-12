from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# MYSQL CONNECTION
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "roost"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)



@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "SELECT * FROM employeee"
    con.execute(sql)
    res = con.fetchall()
    return render_template("home.html", datas=res)


@app.route("/addUsers", methods=['GET', 'POST'])
def addUsers():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        joineddate= request.form['joineddate']
        #createdtime = request.form['createdtime']
        #updatedtime = request.form['updatedtime']
        con = mysql.connection.cursor()
        sql = "insert into employeee(NAME,ADDRESS,GENDER,JOINEDDATE) value (%s,%s,%s,%s)"
        con.execute(sql,[name,address,gender,joineddate])
        mysql.connection.commit()
        con.close()
        flash('User Details Added')
        return redirect(url_for("home"))
    return render_template("addUsers.html")

@app.route("/editUser/<string:id>", methods=['GET', 'POST'])
def editUser(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        joineddate = request.form['joineddate']
        #createdtime = request.form['createdtime']
        #updatedtime = request.form['updatedtime']
        sql = "update employeee set NAME=%s,ADDRESS=%s,GENDER=%s, JOINEDDATE=%s where ID=%s"
        con.execute(sql,[name,address,gender,joineddate,id])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("home"))
        con = mysql.connection.cursor()

    sql = "select * from employeee where ID=%s"
    con.execute(sql, [id])
    res = con.fetchone()
    return render_template("editUser.html", datas=res)
@app.route("/editsal/<string:id>", methods=['GET', 'POST'])
def editsal(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':

        employeeid = request.form['employeeid']
        salary = request.form['salary']
        month = request.form['month']

        sql = "update salary set EMPID=%s,SALARY=%s,MONTH=%s where ID=%s"
        con.execute(sql,[employeeid,salary,month,id])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("sal"))
        con = mysql.connection.cursor()

    sql = "select * from salary where ID=%s"
    con.execute(sql, [id])
    res = con.fetchone()
    return render_template("editsal.html", datas=res)

@app.route("/deleteUser/<string:id>", methods=['GET', 'POST'])
def deleteUser(id):
    con = mysql.connection.cursor()
    sql = "delete from employeee where ID=%s"
    con.execute(sql, id)
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("home"))

@app.route("/deleteSalary/<string:id>", methods=['GET', 'POST'])
def deleteSalary(id):
    con = mysql.connection.cursor()
    sql = "delete from salary where ID=%s"
    con.execute(sql, id)
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("sal"))

@app.route("/sal")
def sal():
    con = mysql.connection.cursor()
    sql = "SELECT * FROM salary"
    con.execute(sql)
    salary = con.fetchall()
    return render_template("salary.html", value=salary)
@app.route("/addsalary/", methods=['GET', 'POST'])
def addsalary():
    if request.method == 'POST':
        employeeid = request.form['employeeid']
        salary = request.form['salary']
        month = request.form['month']
        con = mysql.connection.cursor()
        sql = "insert into salary(EMPID,SALARY,MONTH) value (%s,%s,%s)"
        con.execute(sql,[employeeid,salary,month])
        mysql.connection.commit()
        con.close()
        flash('salary Details Added')
        return redirect(url_for("sal"))
    return render_template("sal.html");
@app.route("/minmax")
def minmax():
    con = mysql.connection.cursor()

    con.execute('SELECT AVG(salary),COUNT(*) FROM E')
    salary = con.fetchall()
    return render_template("minmax.html", values=salary)

@app.route("/maxmin", methods=['GET', 'POST'])
def maxmin():


        return render_template("minmax.html")


if (__name__ == '__main__'):
    app.secret_key = "abc123"
    app.run(debug=True)