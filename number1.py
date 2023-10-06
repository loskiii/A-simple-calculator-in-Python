#Collins Omollo
#SCT211-0021/2022
from datetime import date

def calculate_age(year_of_birth):
    today = date.today()
    # Get the current date

    age = today.year - year_of_birth
    # Calculate the age in years
    
    if today.month < month_of_birth or (today.month == month_of_birth and today.day < day_of_birth):
        age -= 1
        # Subtract 1 from the age if the birthdate has not occurred yet this year

    if today.month == month_of_birth:
        months = 0
        # If the birthdate is in the current month, set the number of months to 0
    elif today.month < month_of_birth:
        months = today.month + 12 - month_of_birth
        # Calculate the number of months if the birthdate is in a future month
    else:
        months = today.month - month_of_birth
        # Calculate the number of months if the birthdate is in a past month

    if today.day < day_of_birth:
        days = today.day + 30 - day_of_birth
        # Calculate the number of days if the birthdate is in a future day of the month
        months -= 1
        # Decrease the number of months by 1

    else:
        days = today.day - day_of_birth
        # Calculate the number of days if the birthdate is in a past day of the month

    return age, months, days
    # Return the age, months, and days

# Example usage
year_of_birth = int(input("Enter the year of birth: "))
month_of_birth = int(input("Enter the month of birth (1-12): "))
day_of_birth = int(input("Enter the day of birth (1-31): "))

age, months, days = calculate_age(year_of_birth)
print("Age:", age, "years", months, "months", days, "days")
  