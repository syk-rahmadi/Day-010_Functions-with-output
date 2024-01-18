# Functions with outputs

def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}".title()
    return full_name #return is the end of the function


format_name("ada", "lovelace")
print(format_name("ada", "lovelace"))

format_string = format_name("ada", "lovelace")
print(format_string)
