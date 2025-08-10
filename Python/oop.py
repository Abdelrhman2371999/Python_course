import os 
import time

def clrear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Member :
    def __init__(self, first_name, last_name, age , member_id,status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.member_id = member_id
        self.status = status
    def display(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Status: {self.status}")
        print("--" * 10)

def create_member():
    clrear_screen()
    print("Create a new member")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    member_id = input("Enter member ID: ")
    status = input("Enter status  or press Enter for default (inactive): ")
    if not status:
        status = "inactive"
    return Member(first_name, last_name, age, member_id, status)

#function to search for a member by ID or name or stutus
def search_member(members):
    clrear_screen()
    print("Search for a member")
    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Status")
    choice = input("Enter your choice: ")
    found_member = []
    if choice == '1':
        member_id = input("Enter member ID to search: ")
        for i in members:
            if i.member_id == member_id:
                found_member.append(i)
                break
    elif choice == '2':
        name = input("Enter name to search (first or last): ")
        for i in members:
            if i.first_name == name or i.last_name == name:
                found_member.append(i)
    elif choice == '3':
        status = input("Enter status to search: ")
        for i in members:
            if i.status == status:
                found_member.append(i)
    else:
        print("Invalid choice!")
    if found_member:
        print("Found Members:")
        for member in found_member:
            member.display()
        
# Main program loop    
Members = []

while True:
    clrear_screen()
    print("1. Create Member")
    print("2. Display Members")
    print("3. Exit")
    print("4.search Member")
    choice = input("Enter your choice: ")

    if choice == '1':
        member = create_member()
        Members.append(member)
        print("Member created successfully!")
        time.sleep(2)
    elif choice == '2':
        clrear_screen()
        for i in Members:
            i.display()
        input("Press Enter to continue...")
    elif choice == '3':
        print("Exiting the program...")
        break
    elif choice == '4':
        search_member(Members)
        input("Press Enter to continue...")
    else:
        print("Invalid choice! Please try again.")
        