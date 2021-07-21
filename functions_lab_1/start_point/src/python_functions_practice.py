def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string_to_check):
    return len(string_to_check)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(number1, number2):
    return int(number1) + int(number2)

def calendar(month):
    months = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "july",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    return months[str(month)]

def number_to_full_month_name(number):
    month = calendar(number)
    return month

def number_to_short_month_name(number):
    month = calendar(number)
    short_month = month[0:3]
    return short_month


