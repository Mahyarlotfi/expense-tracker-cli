import json


try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

amount = float(input("Please enter amount: "))
category = input("Please enter category: ")
description = input("Please enter description: ")

expense = {
	"amount": amount,
	"category": category,
	"description": description
}

data.append(expense)

with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
