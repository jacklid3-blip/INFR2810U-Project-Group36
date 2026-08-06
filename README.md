# INFR2810U-Project-Group36
Final project repository
Names: Robert "Jack" Lidster, Shafin Islam
Final selected Project: Option 3# Vending machine
Overview of Project: This project is to show how a vending machine works via the code or circut diagram. 
Explanation: We have chosen to do a Vending Machine Controller using Python. Devoloped by Rober "Jack" Lidster, Syed Sujood Izhar and Shafin Islam, this controller simulates the operation of a vending machine by accepting currency from the operator, validating the amount, allowing the user to select a product and calculating any change. To run the project you must enter money amount between $0.25 and $20.00, then confirming the amount. After confirming, you must then select a product available. The machine will then display your change or an error if you have insufficient funds. The program uses Tkinter to create a GUI with buttons and boxes which allows for a more user friendly interface. 

entry_money_func(): This functions checks the amount of money enetered and displays it, if the value is invalid, an error is displayed instead.

select_product(): this function handles the product selection, checks if the user has enough money and calculates change.

dispense_product(): This product simulated the product being dispensed by displaying a message.

mainloop(): This function keeps the GUI running and waiting for a user input.