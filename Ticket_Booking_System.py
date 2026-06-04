print("_________________YOUR PERSONAL TICKET BOOKING SYSTEM__________________\n")

start_choice = input("Would you like to proceed with your booking ? (y/n): ")

if start_choice == "n":
    print("Thank you..Please visit again 🙏")

elif start_choice == "y":

    screen_choice = {
        "1": "INOX BANJARA HILLS",
        "2": "INOX JUBILEE HILLS",
        "3": "INOX PUNJAGUTTA",
        "4": "INOX HITECH-CITY"
    }

    print("\nAvailable Screens:")
    for key, value in screen_choice.items():
        print(f"{key}. {value}")

    my_choice = input("\nEnter the screen number: ")

    if my_choice in screen_choice:

        print(f"\nWelcome to {screen_choice[my_choice]}!")
        print("\nHere are the seats available for your booking:\n")

        seats = [
            ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"],
            ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"],
            ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"],
            ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"],
            ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"]
        ]

        for row in seats:
            print(" ".join(row))

        booking1 = input("\nPlease enter seat numbers separated by commas (Example: A1,A2,A3): ")
        selected_seats = booking1.upper().split(",")
        all_seats = []
        for row in seats:
            all_seats.extend(row)

        valid = True

        for seat in selected_seats:
            if seat.strip() not in all_seats:
                valid = False
                print(f"{seat} is not a valid seat.")
                break

        if valid:
            num_seats = len(selected_seats)
            seat_selection_type = input("\nDo you want recliners or normal seats? (r/n): ")
            if seat_selection_type == "r":
                total_cost = num_seats * 350

            elif seat_selection_type == "n":
                total_cost = num_seats * 200

            else:
                print("Invalid seat type.")
                total_cost = 0

            print(f"\nTicket Cost: ₹{total_cost}")

            snack_total = 0
            snack_choice = input("\nWould you like to add snacks? (y/n): ")

            if snack_choice == "y":
                while True:
                    print("\n========== SNACK MENU ==========")
                    print("1. Popcorn")
                    print("2. Fries")
                    print("3. Cooldrink")
                    print("4. Puff")
                    print("5. Finish Order")

                    snack_option = input("\nEnter your snack choice: ")
                    if snack_option == "1":
                        flavour = input("Choose popcorn flavour (caramel/masala/peri-peri): ")
                        qty = int(input("Number of packets: "))
                        if flavour == "caramel":
                            snack_total += qty * 125

                        elif flavour == "masala":
                            snack_total += qty * 110

                        elif flavour == "peri-peri":
                            snack_total += qty * 150

                        else:
                            print("Invalid flavour.")

                    elif snack_option == "2":
                        qty = int(input("Number of fries packets: "))
                        snack_total += qty * 130

                    elif snack_option == "3":
                        qty = int(input("Number of cooldrinks: "))
                        snack_total += qty * 80

                    elif snack_option == "4":
                        qty = int(input("Number of puffs: "))
                        snack_total += qty * 60

                    elif snack_option == "5":
                        break

                    else:
                        print("Invalid snack choice!")

            grand_total = total_cost + snack_total

            print("\n===================================")
            print("          BOOKING SUMMARY")
            print("===================================")
            print(f"Screen        : {screen_choice[my_choice]}")
            print(f"Seats Booked  : {', '.join(selected_seats)}")
            print(f"Number Seats  : {num_seats}")
            print(f"Ticket Cost   : ₹{total_cost}")
            print(f"Snack Cost    : ₹{snack_total}")
            print(f"Grand Total   : ₹{grand_total}")
            print("===================================")
            print("Enjoy Your Movie 🎬🍿")

    else:
        print("Invalid screen number.")

else:
    print("Please enter either y or n.")