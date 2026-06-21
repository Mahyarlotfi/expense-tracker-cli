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