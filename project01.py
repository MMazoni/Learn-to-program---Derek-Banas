customer = []

while True:
    entry = input("Enter customer (Yes/No): ")
    if entry == 'y':
        fName, lName = input("Enter customer name: ").split()

        customer.append({'fName': fName, 'lName': lName})
    elif entry == 'n':
        for i in customer:
            print(i['fName'], i['lName'])
        break
    else:
        print("Type 'y' or 'n' only!")

