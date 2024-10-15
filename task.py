import csv,json

def task_1():
    value = 0;
    with open("task_1.txt") as file:
        for line in file.readlines():
            value += int(line)
    return value

print(task_1())

def task_2():

    # Get input
    order = input("Enter the food codes you want, separated by commas (For example: S4,P3,P7,X2,D4,C1,W2): ")

    # Make dict from csv
    menu = {}
    with open("menu.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            code, item, price = row
            # Store price into dict
            menu[code] = float(price)

    order_codes = [code.strip() for code in order.split(',')]

    # Cal total cost from dict
    total_cost = 0.0
    for code in order_codes:
        if code in menu:
            total_cost += menu[code]
        else:
            # Something was not on the menu, UH OH, ignore it...
            print(f"Item code {code} not found on the menu.")

    return f"Total cost: £{total_cost:0.2f}"

print(task_2())

def task_3():

    # Get input
    name = input("Enter a name: ")

    # Load json file
    with open("contacts.json", 'r') as file:
        contacts = json.load(file)
    
    # Get result from json if its there
    if name in contacts:
        contact = contacts[name]
        return f"Number: {contact['phone']}, Email: {contact['email']}"
    else:
        return "User not found"

print(task_3())