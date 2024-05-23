import math  # Import the math module for mathematical operations

# Define a function to calculate BMI and categorize it
def utregning(vekt, høyde, alder, system):

    try:
        # Check if weight and height are positive values
        if vekt <= 0 or høyde <= 0:
            raise ValueError("Vekt og Høyde må være positive verdier")  # Raise a ValueError if weight or height is not positive
        
        # Calculate BMI based on the chosen measurement system
        if system in("M", "m"):
            bmi = (vekt / (høyde * høyde)) * 10000  # Calculate BMI using the metric system formula
        else:
            bmi = 703 * (vekt / (høyde * høyde))    # Calculate BMI using the imperial system formula
        
        # Categorize BMI into different categories
        if bmi < 18.5:
            kategori = "Undervektig"  # Categorize as Underweight if BMI is less than 18.5
        elif 18.5 <= bmi < 24.9:
            kategori = "Normal vekt"  # Categorize as Normal weight if BMI is between 18.5 and 24.9
        elif 25 <= bmi < 29.9:
            kategori = "Overvektig"   # Categorize as Overweight if BMI is between 25 and 29.9
        else:
            kategori = "Obese"        # Categorize as Obese if BMI is 30 or higher
        
        # Generate a warning message if age is outside the range 12-25
        if not (12 <= alder <= 25):
            warning = "OBS! Resultatet kan være unøyaktig for aldre utenfor 12-25."  # Warning for inaccurate BMI calculation
        else:
            warning = ""  # No warning if age is within the range
        
        return round(bmi, 2), kategori, warning  # Return the calculated BMI, category, and warning message
    
    except Exception as e:
        return str(e), "", ""  # Return any exception message if encountered


# Prompt the user to choose the measurement system
system = input("Velg målenhet (M for metrisk I for imperial): ")

# Check the chosen system and prompt for weight and height accordingly
if system == 'M' or system == 'm':
    vekt = float(input("Vekt i kg: "))       # Prompt for weight in kilograms
    høyde = float(input("Høyde i cm: "))    # Prompt for height in centimeters
else:
    vekt = float(input("Vekt i lbs: "))      # Prompt for weight in pounds
    høyde = float(input("Høyde i inches: ")) # Prompt for height in inches

alder = int(input("Alder: "))  # Prompt for the age

# Call the 'utregning' function to calculate BMI, category, and warning
result, kategori, warning = utregning(vekt, høyde, alder, system)

# Print the calculated BMI, category, and warning message
print('BMI: ', result)
print('Kategori: ', kategori)
print(warning)
