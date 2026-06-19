import json

def delete_expense(expense_id, data):
    for item in data:
        if item["id"] == expense_id:
            data.remove(item)
            break
        
def update_expense(expense_id, data):
    for index, item in enumerate(data):
        if item["id"] == expense_id:
            expense = create_expense(expense_id)
            if expense is None:
                print("Please enter a valid expense")
            else:
                data[index] = expense
            break
            
def create_expense(new_id):
    amount = input("Please enter amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount")
        return None
    category = input("Please enter category: ")
    description = input("Please enter description: ")
    expense = {
            "id": new_id,
	        "amount": amount,
	        "category": category,
	        "description": description
        }
    return expense
        
def write(data):
    with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

# Read file
try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []


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
        else:
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
