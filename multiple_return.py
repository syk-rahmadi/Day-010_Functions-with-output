# Multople return

def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"
    full_name = f"{first_name} {last_name}".title()
    return full_name #return is the end of the function

print(format_name(input("What is your first name? "), input("What is your Last name? ")))

