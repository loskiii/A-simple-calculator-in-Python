#Collins Omollo
#SCT211-0021/2022
def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    # Calculate BMI by dividing weight (in kg) by height (in meters) squared
    return bmi

def get_weight_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "normal weight"
    elif bmi >= 25 and bmi < 30:
        return "overweight"
    else:
        return "obese"

# Example usage
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
weight_status = get_weight_status(bmi)

print("Your BMI is:", round(bmi, 2))
print("Weight status:", weight_status)
