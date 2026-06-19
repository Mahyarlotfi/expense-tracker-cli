import json

amount = float(input("Please enter amount: "))
category = input("Please enter category: ")
description = input("Please enter description: ")

expense = {
	"amount": amount,
	"category": category,
	"description": description
}

with open("expenses.json", "w", encoding="utf-8") as file:
	json.dump(expense, file, indent=4)