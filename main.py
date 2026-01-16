from fastapi import FastAPI
from data import product
from database import getData,add_data,update_data,delete_data
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

app.add_middleware(CORSMiddleware,
                       allow_origins=["http://localhost:3000"],
                       allow_methods=["*"]
)

products=[
    product(id=1,name="laptop",description="Dell Laptop",price=150,quantity=10),
    product(id=2,name="laptop",description="Lenovo Laptop",price=200,quantity=15),
    product(id=3,name="laptop",description="HP Laptop",price=250,quantity=25),
    product(id=4,name="laptop",description="HP Laptop",price=250,quantity=25)
]




@app.get("/products/")
def get_products():
#     return products
    return getData()

# @app.get('/products/{id}')
# def get_products(id:int):
#     products=getData()
#     for i in products:
#         if i.id==id:
#             return i
#     return "404 PRODUCTS NOT FOUND"

@app.post('/products/')
def add_product(product:product):
    # products.append(product)
    # return "Data added successfully"
    return add_data(product)

@app.put("/products/{id}")
def update_product(id:int,product:product):
#     for i in range(len(products)):
#         if products[i].id==id:
#             products[i]=product
#             return "product updated successfully"
#     return "Product not found"
    return update_data(id,product)
    
@app.delete("/products/{id}")
def delete_product(id:int):
    # for i in range(len(products)):
    #     if products[i].id==id:
    #         del products[i]
    #         return "product deleted successfully"
    # return "product not found"
    return delete_data(id)



