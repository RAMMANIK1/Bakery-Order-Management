def order(items, customer_id):
    customer_orders = orders_by_customer.get(customer_id, [])
    for i in range(items):
        customer_orders.append(input("Your order: "))
    orders_by_customer[customer_id] = customer_orders
    bill(customer_id)  # Recalculate total bill after adding new orders


def replace_order(customer_id):
    old_order = input("Enter the order you want to replace: ")
    if old_order in orders_by_customer.get(customer_id, []):
        orders_by_customer[customer_id].remove(old_order)
    else:
        print("Sorry, order is not available.")
    new_order = input("Please provide a new order: ")
    orders_by_customer[customer_id].append(new_order)
    bill(customer_id)  # Recalculate total bill after replacing order


def cancel_order(customer_id):
    print("Which order do you want to cancel? ")
    dt = input()  
    if dt in orders_by_customer.get(customer_id, []):
        orders_by_customer[customer_id].remove(dt)
    else:
        print("Sorry, order is not available.")

def bill(customer_id):
    total = 0
    print(f"Customer ID: {customer_id}")
    print("Your Orders:")
    for item in orders_by_customer.get(customer_id, []):
        if item in bakery_menu:
            price = bakery_menu[item]
            total += price
            print(f"- {item}: ${price}")
        else:
            print(f"Item '{item}' not found in the menu.")
    print("Your Total Bill: $", total)
    customers_details[customer_id] = {'orders': orders_by_customer[customer_id], 'total': total}

def main():
    print("Would you like to place an order? (Y/N): ")
    user_input = input().upper()

    if user_input == "Y":
        customer_id = input("Enter your customer ID: ")
        print("\nPlease enter the number of items you would like to order: ")
        items = int(input())
        order(items, customer_id)

        while True:
            print("\n1. Cancel an order")
            print("2. Replace an order")
            print("3. View bill")
            print("4. Add More Order")
            choice = input("Enter your choice: ")

            if choice == '1':
                cancel_order(customer_id)
            elif choice == '2':
                replace_order(customer_id)
            elif choice == '3':
                bill(customer_id)
                break
            elif choice == '4':
                print("Please provide no of items you would like to order this time: ")
                item2 = int(input())
                order(item2, customer_id)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    bakery_menu = {
        'Cake': 120.0,
        'Cookie': 42.0,
        'Coffee': 53.5,
        'Tea': 42.5,
        'Sandwich': 50.0,
        'Juice': 60.0,
        'Croissant': 52.5,
        'Muffin': 21.5,
        'Bagel': 32.0,
        'Donut': 15.75,
        'Brownie': 42.2,
        'Pie': 40.5,
        'Scone': 22.0,
        'Cupcake': 22.25,
        'Pancake': 33.0,
        'Waffle': 24.0,
        'Toast': 21.0,
        'Omelette': 46.0,
        'Quiche': 35.0,
        'Salad': 47.0
    }
    print("")
    print("❤️❤️❤️❤️❤️ Welcome to Bunny's Bakery ❤️❤️❤️❤️❤️")
    print("\n")
    print("Here is the Menu:😀😀")
    print("\n")
    for item, price in bakery_menu.items():
        print(f"{item}: ${price}",end = "\t")

    print("\n")
    orders_by_customer = {}
    customers_details = {}
    main()
