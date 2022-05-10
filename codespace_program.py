open_file = open("ledger.txt", "a", encoding="utf-8")
##if the file is found, prompt the user for a date
print("What is the date of the transaction?")
date = input("Enter the date: ")
##when the user gives a date, ask for the transaction type
print("What is the transaction type?")
tran_type = input("Enter the transaction type: ")
##when the user gives a transaction type, ask for the amount
print("What is the amount?")
amount = input("Enter the amount: ")
##when the user gives an amount, ask for the description
print("What is the description?")
description = input("Enter the description: ")
##write the date, transaction type, amount, and description to the file
open_file.write(date + "\t" + tran_type + "\t" + amount + "\t" + description + "\n")
##close the file
open_file.close()
