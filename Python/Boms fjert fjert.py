def count_up_to(max_number, num_digits):
    if max_number < 0 or num_digits < 1:
        print("Invalid input")
        return
    
    max_value = 10 ** num_digits - 1
    if max_number > max_value:
        print(f"Input number {max_number} exceeds the maximum value of {max_value} for {num_digits} digits.")
        return
    
    for i in range(max_number + 1):
        print(str(i).zfill(num_digits))

# Example usage:
max_number = int(input("Enter the maximum number: "))
num_digits = int(input("Enter the number of digits: "))
count_up_to(max_number, num_digits)
