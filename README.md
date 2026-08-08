# INFR2810U-Project-Group36

**Final project repository Option #3 Vending machine**

**Group Members:**

Robert "Jack" Lidster (101016640)

Shafin Islam

Syed Sujood Izhar (100787918)

**Overview of Project:**

  This project is to show how a vending machine works via the Python and circuit diagram. 

  This controller simulates the operation of a vending machine by accepting currency from the operator, validating the amount, allowing the user to select a product and calculating any change. To run the project the customer must enter a dollar amount     between $0.25 and $20.00, then they must confirm the amount. After confirming, the amount the vending machine will check the products inventory, then dispense the product of choice, return any change that its due, update inventory or let the users       know if they have fallen short at any step. 

  The program uses Tkinter to create a GUI with buttons and boxes which allows for a more user friendly interface. 

**Products**

  The vending machine contains 4 main products:

          A1 |   Soda   | $1.50

          A2 |  Water   | $0.75

          B1 |  Candy   | $2.00

          B2 | Pretzels | $1.25

  Each product starting with a total inventory of 10 per product, and as sales are made the total inventory will decrease

**How the Controller Works**

1. The vending machine begins in a IDLE state

2. The customer enters an amount between $0.25 and $20.00

3. The machine validates the entered amount and creates a balance for the customer

4. The customer selects the product of their choosing and enters the corresponding code (A1,A2,B1,B2)

5. The vending machine takes the code and checks product stock

6. Then the machine compares the customer balance with the product price

7. If the balance is less then the product price, the customer is given a sign that they need additional money is required

8. If balance = product price, the machine dispenses the product

9. The selected product's inventory is reduced by 1

10. Any required change is calculated and given to the customer

11. The machine resets and goes back into IDLE state
