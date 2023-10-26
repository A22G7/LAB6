#Group 1
#Louise Price
#Ana Arosemena

def encode(password):

    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit

    return encoded_password


#variable
selection= ""

while selection!="3":
    print("\nMenu")
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


    selection=input("\nPlease enter an option:")

    if selection=="1":
        password = input("Please enter your password to encode:")
        encode(password)
        print("Your password has been encoded and stored")



























































