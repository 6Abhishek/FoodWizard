from clear import clear

def display_menu(meal_type):
    match (meal_type):
        case 1:
            
            breakfast_menu = {"Idli": 40,
        "Dosa": 60,
        "Poha": 30,
        "Paratha": 50,
        "Upma": 35,
        "Vada": 25,
        "Aloo Puri": 45}
            i = 1
            print(f"\nMenu for Breakfast:")
            for item, price in breakfast_menu.items():
                print(f"{i}. {item}: ₹{price}")
                i += 1
            i = 1
            return breakfast_menu
        case 2:
            lunch_menu = {
                "Thali": 120,
                "Paneer Butter Masala": 150,
                "Dal Tadka": 100,
                "Butter Naan": 40,
                "Veg Biryani": 130,
                "Roti": 10,
                "Jeera Rice": 70} 
            i = 1
            print(f"\nMenu for Lunch:")
            for item, price in lunch_menu.items():
                print(f"{i}. {item}: ₹{price}")
                i += 1
            i = 1
            return lunch_menu
   
        case 3:
            dinner_menu = {
                "Masala Dosa": 70,
                "Chicken Curry": 180,
                "Fish Fry": 200,
                "Mutton ": 250,
                "Chapati": 15,
                "Palak Paneer": 160,
                "Curd Rice": 80}   
            i = 1
            print(f"\nMenu for Dinner:")
            for item, price in dinner_menu.items():
                print(f"{i}. {item}: ₹{price}")
                i += 1
            i = 1
            return dinner_menu
        case _:
            print("Invalid meal type.")
            
            return 

def take_order(menu):
    order = []
    total = 0
    list_menu = list(menu)
    choice = input("Enter choice(s):").split()
    for key in choice:
        order.append(list_menu[int(key)-1])
        total += menu[list_menu[int(key)-1]]
    return order, total


def display_bill(order, total):
    clear()
    print("\nYour Order:")
    i = 1
    for item in order:
        print(f'{i}. {item}')
        i+=1
    i = 1
    print(f"\nTotal: ₹{total}")
    
    print("\n\nThank you for choosing FOODWIZARD. \nEnjoy your meal! \nWe look forward to serving you again.\n\n")
    




# Driver code
print("\n**************** WELCOME TO FOODWIZARD ****************\n")
print("Enter 1 for Breakfast\nEnter 2 for Lunch\nEnter 3 for Dinner")
meal_type = int(input("\nChoose a meal type: "))
clear()
print("\n**************** WELCOME TO FOODWIZARD ****************\n")
menu = display_menu(meal_type)
if menu:
    try:
        order, total = take_order(menu)
        display_bill(order, total)
    except:
        print("\nInvalid choice(s)\n")

 
    