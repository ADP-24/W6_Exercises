def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state}, {zip}")

display_mailing_label("Anthony Perez", "123 Abbey rd", "london", "UK", "NW8 9AY")

print()

def add_numbers(*args):
    results = sum(args)
    print(f"{' + '.join(map(str, args))} = {results}")

add_numbers(5, 10, 15)
add_numbers(1, 2, 3, 4, 5)

def display_receipt(total_due, amount_paid):
    change_due = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if change_due >= 0:
        print(f"Change Due: ${change_due:.2f}")
    else:
        remaining_balance = abs(change_due)
        print(f"Remaining Balance: ${remaining_balance:.2f}")

display_receipt(50.00, 75.00)
print()
display_receipt(50.00, 30.00)