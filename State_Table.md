# Sujood Izhar 8/3/26
State | Description

**Idle** | Waits for a customer to begin a transaction
**Money_Entry** | Accepts and validates the customer's money
**Product_Selection** | Wait for customer to select product in the order for letter then number (A1,A2 or A3)
**Check_Inventory**| Checks if the selected product is in stock
**Out_of_Stock** | Displays an out of stock message 
**Check_Payment** | compares the customer's balance with the product price
**Insufficient_Funds** | Informs the customer that more money is required to make the purchase
**Dispensing** | Dispenses the desired product
**Update_Inventory** | Reduces the selected product's inventory by 1 with each pruchase
**Return_Change** | Calculates and displays any change
**Error** | Handles all misinputs
**Reset** | Clears transaction, returns any money customer put in and returns back to Idle
