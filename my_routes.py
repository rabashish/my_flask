import json
import time
from flask import jsonify, request
from sqlalchemy.sql import select
from sqlalchemy import Column, Integer, MetaData, String, Table, and_, bindparam, create_engine, text
from my_init import app,db,db1
from mysql.connector import Connect

engine=create_engine("mysql://root:root@localhost/mydb",echo = True)
meta = MetaData()
students = Table(
         
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String(25)), 
   Column('lastname', String(25)), 
    )
@app.route('/newtable')
def newtable():
    crs=db1.cursor()
    result=crs.execute("""CREATE TABLE Address ( 
                             Id int(11) NOT NULL,
                             Address varchar(250) NOT NULL,
                             State varchar(15) NOT Null,
                             Foreign Key()
                             PRIMARY KEY (Id)) """)
   
    meta.create_all(engine)
    return("Laptop Table created successfully ")


@app.route("/indexfromroute/o")
def indexfromroute():
    conn=engine.connect()
    # s=text("select students.id,students.name,students.lastname from students where students.name between :x and :y")
    # s = s.bindparams(x='a')
    # s = s.bindparams(y='p')
    s = select([students.columns.name])
    rs=conn.execute(s)
    result=rs.fetchall()
    for i in result:
       print(i)
    return json.dumps( [dict(ix) for ix in result] ) #CREATE JSON


@app.route("/insert")
def insertvalues():
    #  name=request.args.get("name")
    #  age=request.args.get("age")
    #  crs=db1.cursor(prepared=True)
    #  query="insert into users (Name,Age) values (%s,%s) "
    #  tuple=(name,age)
    # #  result=crs.execute("insert into users (Name,Age) values ('{0}','{1}'),('{0}a','{1}') ".format(name,age))
    #  start_time=time.time()
    #  result=crs.execute(query,tuple)
    #  end_time=time.time()
    #  print(end_time-start_time)

    #  tuple=(name+"1",age+"1")
    #  start_time=time.time()
    #  result=crs.execute(query,tuple)
    #  end_time=time.time()
    #  print(end_time-start_time)
    #  db1.commit()
    #  crs.close()
    #  db1.close()
    try:
        conn=engine.connect()
        ins=students.insert().values(name='std23',lastname='lana23')
        text="insert into student values (demo,std)"
        results=conn.execute()
        
        print(results)
        conn.commit()
        return "inserted successfully"   
    except Exception as e:
           print(e)
@app.route('/updateordelete')
def updateOrdelete():
     isupdate=request.args.get("isupd")
     isdelete=request.args.get("isdel")
     name=request.args.get("name")
     age=request.args.get("age")
     id=request.args.get("id")
     crs=db1.cursor()
    #  if isdelete==True:
    #     crs.execute("delete from  users where id ={0} ".format(id))
    #  if isupdate==True :
     crs.execute("update users set name='{0}',age={1} where id={2}".format(name,age,id))    
     db1.commit()
     return  (" update delete")   


@app.route("/drop/<tablename>")
def drop_table(tablename):
    crs=db1.cursor()
    result=crs.execute("""Drop table {0} """.format(tablename))
            