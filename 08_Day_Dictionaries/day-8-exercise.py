"""
Level: Basic
Problem 1: You are working on a web application that allows users to create and
 manage their own to-do lists.
 You want to implement a feature that allows users to
 filter their to-do list by category.
 You decide to use a dictionary to store the categories and the corresponding to-do items.
"""

# Sample dictionary containing to-do items and their categories
todo_items = {
    "Shopping": ["Buy milk", "Buy eggs", "Buy bread"],
    "Work": ["Finish project report", "Send email to client", "Attend meeting"],
    "Personal": ["Go for a run", "Read a book"]
}


# Function to filter to-do items by category
def filter_by_category(category):
    if category in todo_items:
        print(f"Category: {category}")
        print("Items:")
        for item in todo_items[category]:
            print(f"- {item}")
    else:
        print("Invalid category.")


# Example usage of the filter_by_category function
filter_by_category("Shopping")

"""
Level: Advanced
Problem 2: You are working on a web application that allows users to 
track their daily calorie intake. 
You want to implement a feature that allows users to 
calculate the total number of calories consumed from 
different food items. You decide to use a dictionary 
to store the food items and their corresponding calorie values.
"""
# Sample dictionary containing food items and their calorie values
food_calories = {
    "Banana": 105,
    "Apple": 95,
    "Orange": 62,
    "Yogurt": 150,
    "Brown rice": 216,
    "Avocado": 322,
    "Salmon fillet": 233,
    "Almonds": 163
}


# Function to calculate total calories consumed from a list of food items
def calculate_total_calories(food_list):
    total_calories_consumed = 0
    for food in food_list:
        if food in food_calories:
            total_calories_consumed += food_calories[food]
        else:
            print(f"Warning: {food} is not in the food database.")
    return total_calories_consumed


# Example usage of the calculate_total_calories function
my_food_list = ["Banana", "Apple", "Chicken", "Brown rice"]
total_calories = calculate_total_calories(my_food_list)
print(f"Total calories consumed: {total_calories}")

"""
Level: Complex
Problem 3: You are working on a web application that allows users 
to book appointments with doctors. 
You want to implement a feature that allows users to v
iew the available appointment slots for each doctor. 
You decide to use a dictionary to store the doctor names and 
their corresponding appointment schedules.
"""
# Sample dictionary containing doctor names and their appointment schedules
doctor_schedules = {
    "Dr. Smith": {
        "Monday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Tuesday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Wednesday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Thursday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"],
        "Friday": ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"]
    },
    "Dr. Johnson": {
        "Monday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Tuesday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Wednesday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Thursday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
        "Friday": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"]
    },
    "Dr. Patel": {
        "Monday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Tuesday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Wednesday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Thursday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"],
        "Friday": ["8:00 AM", "9:00 AM", "10:00 AM", "1:00 PM", "2:00 PM"]
    }
}


# Function to display the available appointment slots for a given doctor and day
def display_appointment_slots(doctor, day):
    if doctor in doctor_schedules:
        if day in doctor_schedules[doctor]:
            print(f"Available appointment slots for {doctor} on {day}:")
            for slot in doctor_schedules[doctor][day]:
                print(f"- {slot}")
        else:
            print(f"{doctor} does not have any appointments available on {day}.")
    else:
        print(f"{doctor} is not available for appointments.")


# Example usage of the display_appointment_slots function
display_appointment_slots("Dr. Johnson", "Friday")
