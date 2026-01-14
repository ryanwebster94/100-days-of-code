# Coffee Machine Program Requirements

## 1. User Prompt
- Prompt the user by asking:  
  **“What would you like? (espresso/latte/cappuccino):”**
- Check the user’s input to decide what to do next.
- The prompt should reappear after each action is completed (e.g., after a drink is dispensed) to serve the next customer.

---

## 2. Turn Off the Coffee Machine
- Entering **“off”** at the prompt turns off the coffee machine.
- This is a secret command for maintainers.
- When **“off”** is entered, the program should end execution immediately.

---

## 3. Print Report
- When the user enters **“report”**, generate a report showing the current resource values.

**Example:**
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

yaml
Copy code

---

## 4. Check Resources Sufficient
- When a drink is selected, the program must check if enough resources are available.
- If a required resource is insufficient, stop the process and print an error message.

**Examples:**
- If water is insufficient:  
  *“Sorry there is not enough water.”*
- The same logic applies for milk or coffee.

---

## 5. Process Coins
- If sufficient resources are available, prompt the user to insert coins.
- Coin values:
  - Quarters = $0.25
  - Dimes = $0.10
  - Nickles = $0.05
  - Pennies = $0.01
- Calculate the total value of inserted coins.

**Example Calculation:**
1 quarter + 2 dimes + 1 nickel + 2 pennies
= 0.25 + (0.10 × 2) + 0.05 + (0.01 × 2)
= $0.52

yaml
Copy code

---

## 6. Check Transaction Successful
- Verify that the inserted money is sufficient for the selected drink.

### Insufficient Funds
- If the user inserts less money than required:
  - Print:  
    *“Sorry that's not enough money. Money refunded.”*
  - Do not deduct resources or add profit.

### Successful Transaction
- If enough money is inserted:
  - Add the drink cost to the machine’s money total.
  - Reflect this change in the next **“report”** output.

**Example Report After Sale:**
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

yaml
Copy code

### Excess Money
- If the user inserts more money than required:
  - Return change.
  - Print:  
    *“Here is $X.XX dollars in change.”*
  - Round the change to 2 decimal places.

---

## 7. Make Coffee
- If the transaction is successful and resources are sufficient:
  - Deduct the required ingredients from the machine’s resources.

### Example

**Report Before Purchasing Latte:**
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0

markdown
Copy code

**Report After Purchasing Latte:**
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

markdown
Copy code

- After deducting resources, display a confirmation message:
  - *“Here is your latte. Enjoy!”* (based on the selected drink)