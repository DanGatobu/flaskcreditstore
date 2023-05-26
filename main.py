from flask import Flask,render_template,redirect,request
import psycopg2
import numpy as np



conn=psycopg2.connect(user="postgres", password="dannewton", host="localhost", port="5432", database="creditstore")
curr=conn.cursor()

curr.execute("CREATE TABLE IF NOT EXISTS userdetails(id serial PRIMARY KEY,firstname varchar(100),secondname varchar(100),email varchar(100),phonenumber int);")
curr.execute("CREATE TABLE IF NOT EXISTS creditstore(id serial PRIMARY KEY,balance int,initialbalance int,month varchar(100),monthlypayment int,monthlyprinciple int,monthlyintrest int);")

app=Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')
@app.route('/invent',methods=['GET','POST'])
def inventory(): 
    curr.execute("SELECT * FROM creditstore;")
    data=curr.fetchall()
    conn.commit()
        
    return render_template('invent.html', invent=data)


@app.route('/enterpp',methods=['GET','POST'])
def purchaseprice():
  if request.method=='POST':
    purchaseprice=int(request.form['pp'])
    month=(request.form['mt'])
    monthly_intrest_rate= 12/12
    downpaymet= 0.1 * purchaseprice
    initialbalance= purchaseprice-downpaymet
    balance=initialbalance
    while balance > 100:
      count=0
      mtpayment = balance*0.05
      mtintrest=balance*monthly_intrest_rate
      nbalance = balance - mtpayment
      mtprinciple=mtpayment-mtintrest
      balance=nbalance
      count=count + 1
      curr.execute("INSERT INTO creditstore(balance,initialbalance,monthlypayment,monthlyprinciple,monthlyintrest,month)VALUES(%s,%s,%s,%s,%s,%s)",(balance,initialbalance,mtpayment,mtprinciple,mtintrest,month))
      conn.commit()
  return render_template('invent.html')
      

month= np.array([])# collect month names from the db


  
  
  
  
  
if __name__=="__main__":
  app.run()



