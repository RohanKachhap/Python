def calculate_bmi(weight, height):
    if height <= 0:
        return None
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms (kg): "))
            if weight <= 0:
                print("Weight must be a positive number. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.")

    while True:
        try:
            height = float(input("Please enter your height in meters (m): "))
            if height <= 0:
                print("Height must be a positive number. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for height.")

    bmi = calculate_bmi(weight, height)

    if bmi is None:
        print("Height must be greater than zero for BMI calculation.")
    else:
        category = classify_bmi(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
