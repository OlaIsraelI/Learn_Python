name = " ".join(input("Enter your name? ").split()).title()
job = input("What is your dream job? ").title()
programming_language = input("What is your favourite programming language? ")
hours_long = input("HOw many hours do you plan to study today? ")

developer = f"""

============================================

                    {job}

============================================

Hi, {name} welcome to the developer's environment. You are an aspiring {programming_language} developer, and your dream job is {job}, and you plan to study for {hours_long} hours.


============================================

"""

print(developer)