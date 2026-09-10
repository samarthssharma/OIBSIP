# BMI Calculator 
print("Welcome to the BMI Calculator")
print("-----------------------------")

while True:
    try:
        # Ask for weight and height
        weight_input = input("Please enter your weight in kg: ")
        weight = float(weight_input)
        
        height_input = input("Please enter your height in meters (for example, 1.75): ")
        height = float(height_input)
        
        # Check if they typed a negative number or zero
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers. Let's try again.\n")
            continue 
            
        # If the numbers are good, stop asking and move on
        break
        
    except ValueError:
        # If they type letters instead of numbers, this catches the error
        print("Error: That doesn't look like a valid number. Let's try again.\n")

# Calculate BMI: weight divided by height squared
bmi = weight / (height * height)

# Round it to 2 decimal places like the instructions asked
bmi_rounded = round(bmi, 2)

# Figure out the health category using simple if/else statements
if bmi < 18.5:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal"
elif bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Show the final result to the user
print("\n--- Your Results ---")
print(f"Your BMI is: {bmi_rounded}")
print(f"Category: {category}")
print("--------------------")