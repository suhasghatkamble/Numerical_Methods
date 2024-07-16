# Find approximate value of the cube root of 27
guess = 0.0
cube = 27
increment = 0.1
epsilon = 0.1 # Error Tolerance

# Finding the approximate value
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    
    # Checking the approximate value
    if abs(guess**3 - cube) >= epsilon:
        print("Failed on the cube root of", cube,", guess",guess,", subtraction",abs(guess**3 - cube))
    else:
        print(guess, "is close to the cube root of", cube)