#program7
def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]
num = 121
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")