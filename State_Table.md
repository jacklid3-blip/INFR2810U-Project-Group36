# Sujood Izhar 8/3/26
Vending Machine Controller State Design 

State | Description

**Idle** | Waits for a customer to begin a transaction

**Money_Entry** | Accepts and validates the customer's money

**Product_Selection** | Wait for customer to select product in the order for letter then number (A1,A2 or A3)

**Check_Inventory**| Checks if the selected product is in stock

**Out_of_Stock** | Displays an out of stock message, goes back to IDLE

**Check_Payment** | compares the customer's balance with the product price

**Insufficient_Funds** | Informs the customer that more money is required to make the purchase

**Dispensing** | Dispenses the desired product

**Update_Inventory** | Reduces the selected product's inventory by 1 with each purchase

**Return_Change** | Calculates and displays any change

**Error** | Handles all misinputs

**Reset** | Clears transaction, returns any money customer put in and returns back to Idle

-------------------------------------------------------------------------------------------

Idle --> Customer starts transaction--> display product buttons --> Product_Selection

Product_Selection --> A1 is pressed --> Store Coke as the selected product --> Check_Inventory

Product_Selection--> A2 is pressed--> store water as the selected product --> Check_Inventory

Product_Selection--> A3 is pressed--> store snack as the selected product --> Check_Inventory

Product_Selection --> Invalid product input--> display an invalid selection message --> Error

Check_Inventory--> Selected product is greater than 0 --> Display the product price and payment instructions --> Money_Entry

Check_Inventory--> Selected product stock equal 0 --> display an out of stock message--> Out_Of_Stock

Out_Of_Stock--> Cusotmer returns to product selection--> display product buttons again--> Product_Selection

Money_Entry--> Valid money entered --> Add the amount to the current balaance--> Check_Payment

Money_Entry--->Invalid money is entered--> Display an invalid money message --> Error

Check_Payment--> Balance is less than product price --> Display remaining  amount required --> Insufficient_Funds

Check_Payment--> Balance equals product price --> Approve the purchase --> Dispensing

Check_Payment--> Balance is greater than product price-->  Calculate the change and approve the purchase --> Return_Change, Dispensing

Insufficient_Funds--> Customer adds more money --> Add money to the current balance --> Check_Payment

Insufficient_Funds--> customer cancels--> return inserted money --> Reset

Dispensing --> Product is ready to be dispensed --> Display "Dispensing Product" --> Update_Inventory

Update_Inventory--> Product has been dispensed --> Return_Change

Return_Change--> Change is greater that $0.00 --> Display and return the change--> Reset

Return_Change--> Change equals $0.00 --> Display "No Change Required" --> Reset

Error --> Error occurred during during product selection --> Display product buttons again --> Product_Selection

Error --> Error occurred during money entry --> Display payment instruction again--> Money_Entry

Reset --> Transaction information is cleared--> Reset balance and selected product --> Idle

-------------------------------------------------------------------------------------------

**Truth Table**

1.Product Select

| Valid Selection| Stock Available | Controller Output | Next State |
| 0 | 0 | Display "Invalid Selection" | Product Selection|


