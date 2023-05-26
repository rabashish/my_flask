from flask import Flask;
from flask_sqlalchemy import SQLAlchemy
from mysql import connector


app=Flask(__name__)
db=SQLAlchemy()
db1=connector.connect(host='localhost',database='mydb',username='root',password='root')

# @app.route("/createtable")
# def insert():
#     crs=db1.cursor()
#     result=crs.execute("""CREATE TABLE Laptop1 ( 
#                              Id int(11) NOT NULL,
#                              Name varchar(250) NOT NULL,
#                              Price float NOT NULL,
#                              Purchase_date Date NOT NULL,
#                              PRIMARY KEY (Id)) """)
    
#     print("Laptop Table created successfully ")
# if __name__=="__main__":
#     app.debug=True
#     app.run()
import my_routes 

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#    return 'Hello World'

# if __name__ == '__main__':
#    app.run()