import json


def test():
    total_cost = 0
    total_time = 0
    order_summary = ""

    product_list = ['pizza (without cheese)', 'burger (without tomato)', 'hot-dog', 'kk']
    with open("menu.json") as f:
        menu = json.load(f)["items"]
        menu_dict = {item["name"]: item for item in menu}


        for item in product_list:
            choice_product_by_user = item.split(" (")[0].strip().lower()
            for product in menu_dict:
                if choice_product_by_user in menu_dict[product]["name"].lower():
                    product_name = menu_dict[product]["name"]
                    product_price = menu_dict[product]["price"]
                    product_preparation_time = menu_dict[product]["preparation_time"]
                    total_cost += product_price
                    total_time += product_preparation_time
                    print(f"{product_name} with cost: {product_price} with prep time: {product_preparation_time}")
    order_summary = f"{product_list}\nTotal cost: {total_cost}\n Preparation_time: {total_time}"
    print(order_summary)






test()

"""
        # done by list
        product_name_from_menu = {i["name"].lower() for i in menu}
        print(product_name_from_menu)
        for product in product_list:
            if product.split(" (")[0].strip().lower() in product_name_from_menu:
                print(product)
            else:
                print(f"product {product} is not in our list")
"""