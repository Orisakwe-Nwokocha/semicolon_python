import re
def reverse_string(str):
    return str[::-1]

def palindrome(args):
    modified_string = re.sub('[^a-zA-Z0-9]', '', args[0].casefold())
    reversed_string = reverse_string(modified_string)

    if reversed_string == modified_string:
        return True
    else:
        return False
