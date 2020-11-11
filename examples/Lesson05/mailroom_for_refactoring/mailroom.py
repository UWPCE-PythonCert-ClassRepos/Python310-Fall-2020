#!/usr/bin/env python3

# Pre-populated data structure of at least five donors with 1-3 donations each
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

# Prompt to choose from menu of 3 actions
# 1. Send a Thank You
# 2. Create a Report
# 3. Quit
prompt = "\n".join(("Please choose from the following three options:",
        "1 - Send a Tank You",
        "2 - Create a Report",
        "3 - Quit",
        ">>> "))


def check_if_in_list(name, db):
    for n in db:
        if n[0] == name:
            print("That name is already in the list.")
            return True
    return False


def get_name_index(name, db):
    for r, n in enumerate(db):
        if n[0] == name:
            return r
    return None


def get_name_list(db):
    return [names[0] for names in db]


def list_names(name, db):
    if name == 'list':
        for n in get_name_list(donor_db):
            print(n)
    pass


def add_donor_if_needed(name, db):
    if check_if_in_list(name, db) is False:
        db.append((name, []))
    return db


def get_email_text(name, amt):
    line1 = f"Dear {name},"
    line2 = f"Thank you for your gracious donation of ${amt:.2f}."
    line3 = "-The Mailroom"
    return "\n".join((line1, line2, line3))


# Send a Thank You option
def send_thank_you_option():
    name = 'list'
    while name == 'list':
        # Prompt for a Full Name
        name = input("Please enter donor's full name or list to list names:\n>>> ")
        # If user types list show a list of donor names and re-prompt
        list_names(name, donor_db)
    # If user types a name not in the list add that name and use it
    donor_db = add_donor_if_needed(name, donor_db)
    # If user types a name in the list, use it
    # Once a name is selected prompt for a donation amount
    # Convert amount to a number and add that amount to donation history
    donamt = 0
    while donamt == 0:
        try:
            donamt = \
                float(input("Please enter the new donation amount:\n>>> $"))
        except ValueError:
            print("Please enter a valid donation amount in the form of $x.xx.")
    donor_db[get_name_index(name, donor_db)][1].append(donamt)
    # Use string formatting to compose an email thanking the donor
    email = get_email_text(name, donamt)
    # Print email to terminal and return to the original prompt
    print("Here's the email:\n")
    print(email)
    print("\nReturning to main menu.\n")
    pass


def sort_key(donors):
    return donors[1]


def get_sorted_donor_data(donor_db):
    donor_data = list()
    for d, donor in enumerate(donor_db):
        total = sum(donor[1][:])
        gifts = len(donor[1][:])
        avg = total / gifts
        donor_data.append((donor[0], total, gifts, avg))
    donor_data = sorted(donor_data, key=sort_key, reverse=True)
    return donor_data


def print_sorted_data_line(d):
    return f"{d[0]:25}  ${d[1]:11.2f}   {d[2]:9}  ${d[3]:12.2f}"


# Create a Report option
def create_report_option():
    # Print a list of donors sorted by total historical donation amount
    print("Here's the report sorted by total historical donation amount:\n")
    # Include Donor Name, Total Donated, # of Donations, Average Donation
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("------------------------------------------------------------------")
    for d in get_sorted_donor_data(donor_db):
        print(print_sorted_data_line(d))
    # After printing return to the original prompt
    print("\nReturning to main menu.\n")
    pass


# Quit option
def quit_option():
    print("Now Exiting - Thank you for visiting the mailroom!")
    exit() # exit the interactive script


# Main program with while True loop
def main():
    print("Welcome to the mailroom!")
    while True:
        option = 0
        while option == 0:
            try:
                option = int(input(prompt))
            except ValueError:
                print("Please enter a valid option.")
        if option == 1:
            send_thank_you_option()
        elif option == 2:
            create_report_option()
        elif option == 3:
            quit_option()
        else:
            print("That option is not valid!")

# Do checks if name equals main
if __name__ == "__main__":
    main()

    # assert  ==

    # print("Checks passed!")
