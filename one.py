def validate_transaction(t_type, amount_str, balance):
    # 1. Check transaction type
    if t_type != "Deposit" and t_type != "Withdraw":
        return False, "type"

    # 2. Check if amount is a number
    try:
        amount = int(amount_str)
    except ValueError:
        return False, "number"

    # 3. Check positive amount
    if amount <= 0:
        return False, "positive"

    # 4. Check maximum limit of 100000
    if amount > 100000:
        return False, "limit"

    # 5. Check sufficient balance for withdrawal
    if t_type == "Withdraw" and amount > balance:
        return False, "balance"

    return True, "Valid"


def main():
    balance = 10000  # Opening balance
    valid_count = 0
    invalid_count = 0

    try:
        # File handling
        infile = open("transactions.txt", "r")
        outfile = open("valid_transactions.txt", "w")

        line_no = 1
        for line in infile:
            line = line.strip()
            if line == "":
                continue

            # Split line in the form of type and amount
            parts = line.split(",")
            t_type = parts[0].strip()
            amount_str = parts[1].strip()

            # Call function
            is_valid, err_type = validate_transaction(t_type, amount_str, balance)

            if is_valid:
                amount = int(amount_str)
                if t_type == "Deposit":
                    balance = balance + amount
                else:
                    balance = balance - amount

                print(f"Line {line_no}: Valid | Balance: {balance}")
                valid_count = valid_count + 1
                outfile.write(line + "\n")  # Write valid transaction directly to file
            else:
                # Print real reason based on error
                if err_type == "type":
                    print(f"Line {line_no}: Invalid - unknown type '{t_type}'")
                elif err_type == "number":
                    print(f"Line {line_no}: Invalid - amount '{amount_str}' is not a number")
                elif err_type == "positive":
                    print(f"Line {line_no}: Invalid - amount must be positive")
                elif err_type == "limit":
                    print(f"Line {line_no}: Invalid - exceeds limit of 100000")
                elif err_type == "balance":
                    print(f"Line {line_no}: Invalid - insufficient balance")

                invalid_count = invalid_count + 1

            line_no = line_no + 1

        infile.close()
        outfile.close()

        # Print final summary
        print(f"Valid: {valid_count} | Invalid: {invalid_count} | Final balance: {balance}")

    except FileNotFoundError:
        print("Error: transactions.txt file not found.")


if __name__ == "__main__":
    main()