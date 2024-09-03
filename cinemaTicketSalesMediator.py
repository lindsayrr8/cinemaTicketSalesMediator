
# This program pre-sells a limited number of cinema tickets.
# Each buyer may buy up to 4 tickets &
# No more than 20 total tickets may be sold.

# Prompts user for desired num of tickets and
# displays remaining num of tickets.
# Repeats til all tickets are sold
# then displays total num of buyers.


TICKETS = 20      # total tickets available for purchase
buyTickets = 0    # num of tix being bought by that customer
ticketQuant = 0   # total num of tix already bought
numBuyers = 0     # num of passes thru loop until tickets all sold


# Dialogue program purpose to user.
print(" ")
print("This program sells 20 advance cinema tickets (Limit 4 per customer). ")
print(" ")

# Prompt user to input ticket amount for purchase.
buyTickets = input("Enter the number of tickets to purchase: ")
buyTickets = int(buyTickets)

# Condition loop to catch invalid input (purchase inputs greater than 4.)
while buyTickets >= 5:
      print("Error: Limit of 4 tickets per customer. Please try again. ")
      print("The number of tickets remaining is: ", TICKETS)
      buyTickets = input("Enter the number of tickets to purchase: ")
      buyTickets = int(buyTickets)

# Enter loop to prompt user to buy tickets until depleted.    
while buyTickets > 0 and buyTickets <= 4 and ticketQuant < 21:
      ticketQuant = buyTickets
      TICKETS = TICKETS - ticketQuant
      numBuyers = numBuyers + 1
      
# Exit loop when tickets are depleted; display results to user.
      if TICKETS == 0:
         print("The number of tickets remaining is: ", TICKETS)
         print(" ")
         print("The total number of buyers is: ", numBuyers)
         break
      
# Continue ticket purchase loop.
      print("The number of tickets remaining is: ", TICKETS)
      buyTickets = input("Enter the number of tickets to purchase: ")
      buyTickets = int(buyTickets)

# Catch invalid inputs within the loop (purchase inputs greater than 4.)
      while buyTickets >=5:
        print("Limit of 4 tickets per customer. Please try again.")
        print("The number of tickets remaining is: ", TICKETS)
        buyTickets = input("Enter the number of tickets to purchase: ")
        buyTickets = int(buyTickets)
        continue










          
