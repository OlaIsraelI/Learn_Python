#Movie Ticket Receipt

movie_title = input("what is the title of the Movie: ").title()
ticket_price = float(input("What is the ticket price: "))
tickets_bought = int(input("How many tickets did you buy: "))

calculate = ticket_price * tickets_bought

print(f"You bought {tickets_bought} tickets, for {ticket_price} for the movie, {movie_title}. Your total cost is {calculate}")