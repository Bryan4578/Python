# Ticket sale 
seats = list(range(1, 21))
def display_seats(seats):
    print("\nAvalable seat:")
    print(seats)
def ticket_purchase():
    while True:
        display_seats(seats)
        seat_number = int(input("Please enter the seats number you want to purchase (or '0' to finish): "))
        
        if seat_number == 0:
            print("Thank you for your purchase!")
            break
        elif seat_number not in seats:
            print("Sorry, that seat is either taken or doest exist. Please choose another seat.")
        else:
            seats.remove(seat_number)
            print(f"Seat {seat_number} has been successfully purchased.")
ticket_purchase()
