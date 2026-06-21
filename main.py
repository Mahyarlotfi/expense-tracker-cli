from app.storage import read_file, write
from app.expense import (
    delete_expense,
    create_expense,
    update_expense
    )

    
data = read_file()

while True:
    choice = input(
        "=====================\n"
        " 1 - Add Expense\n"
        " 2 - View Expense\n"
        " 3 - Delete Expense\n"
        " 4 - Update Expense\n"
        " 0 - Exit\n"
        "=====================\n"
        "Enter your choice: "
        )
        
    if not choice.isdigit():
        print("Invalid input, please enter a number")
        continue
    else:
        choice = int(choice)
    
    if choice == 1:
        ids = [item["id"] for item in data]
        if not ids:
            new_id = 1
        else:
            new_id = max(ids)+1
        expense = create_expense(new_id)
        if expense is None:
            continue
        data.append(expense)
        write(data)
            
    elif choice == 2:
        for i in data:
            print(i)
    
    elif choice == 3:
        try:
            delete_id = int(input("Please enter your id: "))
            delete_expense(delete_id, data)
            write(data)
        except ValueError:
            print("Please enter a valid id")
        
        
    elif choice == 4:
        try:
            update_id = int(input("Please enter your id: "))
            update_expense(update_id, data)
            write(data)
        except ValueError:
            print("Please enter a valid id")
        
        
    elif choice == 0:
        break
