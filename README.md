#Title - Bank Transaction Validator ( PS:31)

Aishwarya Thakur  ERP-RU-26-00817
Section- 1K
- Language: Python 3

## Overview
 The program reads banking transactions from a text file named `transactions.txt`, validates against banking rules prints whether the transaction is valid or invalid (reason), update amount accordingly and gives output. 

## Concepts Used
- Functions
- Conditions
- Exceptions
- File Handling

## Rules 
1. Opening balance starts at 10000. 
2. Transaction type must be either `Deposit` or `Withdraw`. 
3. Amount must be a positive number up to `100000` per transaction. 
4. Withdrawal amount cannot must not be greater than current amount . 

## How to Run:-
1. Keep `one .py` and `transactions.txt` in the same folder. 
2. Open the terminal  in that folder. 
3. Run the program using the command
   ```bash
   python one.py