#===== Warehouse Management System ====
import json

warehouse = {}

# add product
def add_product():
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    warehouse[product_id] = {
        "name": product_name,
        "quantity": quantity,
        "price":  price
        
    }

    save_data()
    print("✅ Product Added Successfully.")
        



# view product

def view_product():
  
  if warehouse == {}: 
      print("no product Available.")

  else:
     print("\nProduct list")
     for show,details in warehouse.items() :
        print(show,details)

    

# search product 
def search_product():
       product_id = input("enter the product id ")

       if product_id in warehouse:
           print("product id is found.",warehouse[product_id])

       else:
           print("not found.")




# save data 
def save_data():
   with open("warehouse.json", "w") as file:
       json.dump(warehouse, file, indent=4)

def load_data():
    global warehouse
    try:
        with open("warehouse.json", "r") as file:
            warehouse = json.load(file)
    except FileNotFoundError:
        warehouse = {}       

load_data()      # Load old products first
add_product()    # Add new product
view_product()
search_product()