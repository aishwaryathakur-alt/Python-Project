# Project Summary & Test Cases
Bank Transaction Validator - reads the transaction from the text file, validates against banking rules, updates the balance and gives output.

I faced problem as too many rules are there confusion also came. So, carefully I have to see rules write the code according to it. Sometimes error came in between, but I tried again to remove that error.

## Test Case Execution Summary 
(Opening Balance = 10000)

### Test Case 1: Normal Input
- Input: 
  Deposit,5000
  Withdraw,2000
- Output: 
  Line 1: Valid | Balance: 15000
  Line 2: Valid | Balance: 13000
  Valid: 2 | Invalid: 0 | Final balance: 13000

### Test Case 2: Boundary / Minimum Input
- Input: 
  Withdraw,10000
- Output: 
  Line 1: Valid | Balance: 0
  Valid: 1 | Invalid: 0 | Final balance: 0

### Test Case 3: Invalid Input
- Input: 
  Withdraw,20000
  Deposit,-500
  Transfer,100
  Deposit,abc
- Output: 
  Line 1: Invalid - insufficient balance
  Line 2: Invalid - amount must be positive
  Line 3: Invalid - unknown type 'Transfer' 
  Line 4: Invalid - amount 'abc' is not a number
  Valid: 0 | Invalid: 4 | Final balance: 10000

### Test Case 4: Different Valid Scenario
- Input: 
  Deposit,150000
  Deposit,50000
  Withdraw,60000
- Output: 
  Line 1: Invalid - exceeds limit of 100000
  Line 2: Valid | Balance: 60000
  Line 3: Valid | Balance: 0
  Valid: 2 | Invalid: 1 | Final balance: 0