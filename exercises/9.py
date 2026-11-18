#Multi-Line Portfolio Profile

handle = input("What is your name? ").strip().title
primary_language = input("What Language do you write? ").strip().title()
years_experience = input("How long have you been writing? ")
is_available = input("Are you available for a programming role? (yes/no) ").strip().lower() == "yes"

portfolio = f""" 

===========================================

            DEVELOPER PORTFOLIO

===========================================

Hello, I'm {handle}, I'm a software developer with experience using the {primary_language} programming language. I have {years_experience} of experience. 

Currently available for gigs: {is_available}

===========================================
"""

print(portfolio)