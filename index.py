# User details dictionary
users = {}

def add_user():
    user_id = int(input("Enter User_ID: "))
    if user_id in users:
        print("User ID already exists. Try updating the user.")
        return
    name = str(input("Enter User Name: "))
    age = int(input("Enter User Age: "))
    email = str(input("Enter User Email: "))
    
    users[user_id] = {"Name": name, "Age": age, "Email": email}
    print("User added successfully!")
def view_users():
    if not users:
        print("No users found.")
    else:
        for user_id, details in users.items():
            print(f"ID: {user_id}, Name: {details['Name']}, Age: {details['Age']}, Email: {details['Email']}")
def update_user():
    user_id = int(input("Enter User ID to update: "))
    if user_id in users:
        print("Enter new user update:")
        name = str(input(f"New Name ({users[user_id]['Name']}): ")) or users[user_id]['Name']
        age = int(input(f"New Age ({users[user_id]['Age']}): ")) or users[user_id]['Age']
        email = str(input(f"New Email ({users[user_id]['Email']}): ")) or users[user_id]['Email']
        users[user_id] = {"Name": name, "Age": age, "Email": email}
        print("User update successfully!")
    else:
        print("User ID not found.")
def delete_user():
    user_id = int(input("Enter User ID to delete: "))
    if user_id in users:
        del users[user_id]
        print("User delete successfully!")
    else:
        print("User ID not found.")

# Main loop
while True:
    print("\nUser Management System")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        update_user()
    elif choice == '4':
        delete_user()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
