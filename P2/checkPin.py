database = [['albert', '1234'],
['dilbert', '4242'],
['smith', '7524'],
['johns', '9843']]

username = input("User name:")
pin = input("PIN code:")
if [username, pin] in database: print("Access granted")