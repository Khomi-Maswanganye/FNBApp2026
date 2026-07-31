contacts = [
    {"name":"Khomi",
     "phone":"0823654998",
     "email":"khomithebest@gmail.com"

     },
      {"name":"Khwezi",
          "phone":"023659874",
          "email":"khwezitheweirdo@gmail.com"
     
          },
           {"name":"Katlego",
               "phone":"069874452",
               "email":"katlegooborang@gmail.com"
          
               },
                {"name":"tiyani",
                    "phone":"06398745632",
                    "email":"tiyaniwatibyela@gmail.com"
               
                    },
]

def add_contact():
    name = input("Enter name:")
    phone = input("Enter phone number:")
    email = input("Enter email address")
    contacts.append({
        "name":name,
        "phone":phone,
        "email":email

    })
    

    return name + " has been successfully added. "

def search_contact(name):
    for person in  contacts:
        if person["name"] == name:
            print(person)
        else:
            print("None")

def delete_contact(name):
    for person in contacts:
        if person["name"] == name:
            person.remove(name)
            return f"{person} has been removed"

def view_all():
    for all in contacts:
     print(f"Name: {all["name"]}")
     print(f"Name: {all["name"]}")
     print(f"Name: {all["name"]}")
     print()

option = ""

while option != "5":
    print("Option 1: Add ")
    print("Option 2: Search ")
    print("Option 3: Delete ")
    print("Option 4: View ")
    print("Option 5: Exit ")

    option = input("Choose:")

    if option == "1":
        add_contact()
        
    elif option =="2":
        search_contact(input())
    elif option == "3":
        delete_contact(input())
    elif option == "4":
        view_all()
    else:
        print("goodbye")

