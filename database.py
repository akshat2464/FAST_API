import mysql.connector as sql
from data import product

conn=sql.connect(host="localhost",user="root",password="Darling69")
conn.autocommit=True
curr=conn.cursor()
curr.execute("use data")

def getData():
    products=[]
    curr.execute("select* from fastdata")
    data=curr.fetchall()
    for i in data:
        products.append(product(id=i[0],name=i[1],description=i[2],price=i[3],quantity=i[4]))

    return products

def add_data(product:product):
    query=f"insert into fastdata values\
    ({product.id},'{product.name}','{product.description}',{product.price},{product.quantity});"
    curr.execute(query)
    
    return "record added successfully"

def update_data(id:int,product:product):
    query=f"update fastdata set name='{product.name}',description='{product.description}',price={product.price},quantity={product.quantity}\
        where id={id}"
    curr.execute(query)
    return "record updated"

def delete_data(id:int):
    query=f"delete from fastdata where id={id}"
    curr.execute(query)
    return "data deleted"