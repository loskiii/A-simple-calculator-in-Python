#Collins Omollo
#SCT211-0021/2022
def calculate_bill(total_bill, tip_percentage, num_people):
    tip_amount = total_bill * (tip_percentage / 100)
    # Calculate the tip amount based on the total bill and tip percentage

    total_amount = total_bill + tip_amount
    # Calculate the total amount including the tip

    amount_per_person = total_amount / num_people
    # Calculate the amount each person should pay by dividing the total amount among the number of people

    return round(amount_per_person, 2)
    # Return the amount each person should pay rounded to two decimal points

# Example usage
total_bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people: "))

amount_per_person = calculate_bill(total_bill, tip_percentage, num_people)
print("Amount per person: $", amount_per_person)
