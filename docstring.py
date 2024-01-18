# Already used functions with outputs
length = len(format_name)


# Return as an early exit
def format_name(first_name, last_name):
    """''Take a first and last name and format it to return the title case version of the name."""
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"
    full_name = f"{first_name} {last_name}".title()
    return full_name
