import time
import sys

def countdown_timer(hours, minutes, seconds, milliseconds):
    # Calculate the total time in seconds
    total_seconds = (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000)
    
    # Ensure the total time is positive
    if total_seconds <= 0:
        print("Invalid input. Time should be greater than zero.")
        return
    
    while total_seconds > 0:
        # Calculate the remaining time components
        remaining_hours = int(total_seconds // 3600)
        remaining_minutes = int((total_seconds % 3600) // 60)
        remaining_seconds = int(total_seconds % 60)
        remaining_milliseconds = int((total_seconds % 1) * 1000)
        
        # Display the remaining time on the same line
        sys.stdout.write(f"Time Remaining: {remaining_hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}.{remaining_milliseconds:03d}\r")
        sys.stdout.flush()
        
        # Wait for 1 second
        time.sleep(1)
        
        # Decrement the total time
        total_seconds -= 1
    
    print("\nTime's up!")

# Get user input for the countdown time
try:
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    milliseconds = int(input("Enter milliseconds: "))
    
    countdown_timer(hours, minutes, seconds, milliseconds)
except ValueError:
    print("Invalid input. Please enter valid numeric values for time components.")
