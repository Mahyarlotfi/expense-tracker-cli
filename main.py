import json

while True:
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        

    
    choice = int(input(
        "=====================\n"
        " 1 - Add Expense\n"
        " 2 - View Expense\n"
        " 0 - Exit\n"
        "=====================\n"
        "Enter your choice: "
        ))
    
    if choice == 1:
        ids = [item["id"] for item in data]
        if not ids:
            new_id = 1
        else:
            new_id = max(ids)+1
        amount = float(input("Please enter amount: "))
        category = input("Please enter category: ")
        description = input("Please enter description: ")
        expense = {
            "id": new_id,
	        "amount": amount,
	        "category": category,
	        "description": description
            
        }

        data.append(expense)
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
    elif choice == 2:
        for i in data:
            print(i)
        
    elif choice == 0:
        break
    
