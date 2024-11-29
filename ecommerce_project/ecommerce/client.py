import requests

BASE_URL = "http://127.0.0.1:5000"

def add_product(name, description, price):
    url = f"{BASE_URL}/products"
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.json())

def get_products():
    url = f"{BASE_URL}/products"
    response = requests.get(url)
    if response.status_code == 200:
        print("Product list:")
        for product in response.json():
            print(product)
    else:
        print("Failed to retrieve products:", response.json())


if __name__ == "__main__":
    # Add new products
    add_product("Laptop", "A powerful laptop", 1200.00)
    add_product("Smartphone", "A high-end smartphone", 800.00)

    # Retrieve and print all products
    get_products()
