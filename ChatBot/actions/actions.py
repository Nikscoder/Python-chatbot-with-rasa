# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
import json
from typing import Any, Text, Dict, List

from dask.order import order
from jsonpickle.util import items
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckHours(Action):
    def name(self):
        return "action_check_hours"

    def run(self, dispatcher, tracker, domain):
        ### dispatcher – the dispatcher which is used to send messages back to the user.
        # Use dispatcher.utter_message() or any other rasa_sdk.executor.CollectingDispatcher method
        #day = tracker.get_slot("day")
        try:
            with open("opening_hours.json") as f:
                items = json.load(f)["items"]
        except:
            dispatcher.utter_message(text="Sorry, our opening hours list is currently unavailable!")
        days = []
        for day in items:
            open_time = items[day]["open"]
            close_time = items[day]["close"]
            days.append(f"{day} - from: {open_time} to: {close_time}")
        hours_message = "\n".join(days)
        dispatcher.utter_message(hours_message)
        return []


class ActionListMenu(Action):
    def name(self):
        return "action_list_menu"

    def run(self, dispatcher, tracker, domain):
        try:
            with open("menu.json") as f:
                menu = json.load(f)["items"]
        except:
            dispatcher.utter_message(text=f"Sorry, our menu list currently unavailable !")

        menu_details = []
        for item in menu:
            menu_name_item = item["name"]
            menu_price_item = item["price"]
            menu_preparation_time_item = item["preparation_time"]
            menu_details.append(f"{menu_name_item} - {menu_price_item} PLN (preparation time: {menu_preparation_time_item} min)")

        menu_message = "\n".join(menu_details)
        dispatcher.utter_message(text=f"Here is our menu:\n{menu_message}")
        return []



# action to add more product to order by the customer
class ActionAddToOrder(Action):
    def name(self) -> Text:
        return "action_add_to_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # receive the product name from user (order_item) with special request(special_request)
        order_item = tracker.get_slot("order_item")
        special_request = tracker.get_slot("special_request")
        #List with orders
        current_order = tracker.get_slot("order_items") or []

        if order_item:
            with open("menu.json") as f:
                item_found = False
                menu = json.load(f)["items"]
                for i in menu:
                    if i["name"].lower() == order_item.lower():
                        item_found = True
                        break

                if item_found:
                    item = order_item
                    if special_request:
                        item +=f" (without {special_request})"
                    current_order.append(item)
                    dispatcher.utter_message(text=f"Added to order: {item}\nYour cart: {current_order}")
                else:
                    dispatcher.utter_message(text=f"Sorry, we do not have such {order_item} on the menu. Please select another item.")
                    return []

        #dispatcher.utter_message(template="utter_ask_add_more")
        return [SlotSet("order_items", current_order), SlotSet("order_item", None), SlotSet("special_request", None)]


class ActionsShowOrder(Action):
    def name(self) -> Text:
        return "action_show_order"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order_items = tracker.get_slot("order_items") or [] # users_chooise_of_products

        if not order_items:
            dispatcher.utter_message(text="Your curt is empty")
            return []

        total_cost = 0
        total_time = 0
        order_summary = ""

        with open("menu.json") as f:
            menu = json.load(f)["items"]
            menu_dict = {item["name"]: item for item in menu}

            for item in order_items:
                choice_product_by_user = item.split(" (")[0].strip().lower() # to delete section "special_request"
                for product in menu_dict:
                    if choice_product_by_user in menu_dict[product]["name"].lower():
                        product_name = menu_dict[product]["name"]
                        product_price = menu_dict[product]["price"]
                        product_preparation_time = menu_dict[product]["preparation_time"]
                        total_cost += product_price
                        total_time += product_preparation_time
                        #order_summary += f"{product_name} - {product_price} PLN (preparation time is: {product_preparation_time}mins)"
                #else:
                 #   dispatcher.utter_message(text=f"Item '{product_name}' not found in the menu")
        #order_summary += f"{product_name} - {product_price} PLN (preparation time is: {product_preparation_time}mins)"
        dispatcher.utter_message(text=f"Summarize of order:\n Products: {order_items}\n Total cost: {total_cost}\n Total preparation time: {total_time}")
        #dispatcher.utter_message(template="utter_ask_pickup_or_delivery")

            #store the total cost in slot to use later
        return [SlotSet("total_cost", total_cost)]






