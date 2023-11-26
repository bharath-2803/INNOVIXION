phoneBook = {}


def getInputs():
    print("Select operation")
    print("===========================\n")
    print("""
        1. Add contact
        2. Edit contact
        3. Delete contact
        4. Search contact
        5. List contact
        6. Exit
        """)

    userInput = int(input("Enter your operation : "))

    if userInput == 1:
        insertData()
    elif userInput == 2:
        editData()
    elif userInput == 3:
        deleteData()
    elif userInput == 4:
        searchData()
    elif userInput == 5:
        listData()
    elif userInput == 6:
        exit()
    else:
        print("Invalid operation")


def insertData():
    name = input("Enter the name : ")
    number = input("Enter the number : ")
    blood_group = input("Enter the blood group (optional, press Enter to skip): ")

    contact_info = {'Number': number, 'Blood Group': blood_group}
    phoneBook[name] = contact_info

    print("===============\n")
    print("Contact added successfully\n")
    print("===============\n")
    getInputs()


def deleteData():
    name = input("Enter the name : ")

    if name in phoneBook:
        del phoneBook[name]
        print("===============\n")
        print(f"{name} deleted successfully\n")
        print("===============\n")
        getInputs()

    elif name not in phoneBook:
        print("===============\n")
        print(f"{name} not found\n")
        print("===============\n")
        while True:
            op = input("Do you want to continue this operation? (Y/N): ")
            if op.lower() == 'y':
                deleteData()
                break
            elif op.lower() == 'n':
                getInputs()
                break
            else:
                print("Invalid selection")


def editData():
    name = input("Enter the name : ")

    if name in phoneBook.keys():
        newNumber = input("Enter the new number : ")
        newBloodGroup = input("Enter the new blood group (optional, press Enter to skip): ")

        phoneBook[name]['Number'] = newNumber
        if newBloodGroup:
            phoneBook[name]['Blood Group'] = newBloodGroup

        print("===============\n")
        print("Contact information updated successfully\n")
        print("===============\n")
    else:
        print("===============\n")
        print(f"{name} not found\n")
        print("===============\n")
    getInputs()


def searchData():
    searchRes = input("Enter the name you want to search : ")

    if searchRes in phoneBook.keys():
        print("===============\n")
        print(f"{searchRes} :--> {phoneBook[searchRes]}\n")
        print("===============\n")
        getInputs()
    else:
        print("===============\n")
        print(f"{searchRes} not in this phone book\n")
        print("===============\n")
        getInputs()


def listData():
    if phoneBook:
        print("===============")
        count = len(phoneBook)
        print(f"You have {count} contacts\n")
        for item in phoneBook.keys():
            print(f"{item} :--> {phoneBook[item]}\n")
        print("===============\n")
        getInputs()


def main():
    getInputs()


main()
