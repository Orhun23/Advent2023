def process_line(line):
    digits = [char for char in line if char.isdigit()]
    if digits:
        if len(digits) == 1:
            combined_number = int(digits[0] * 2)
        else:
            combined_number = int(digits[0] + digits[-1])
        return combined_number
    return 0

def process_csv(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            combined_number = process_line(line)
            total_sum += combined_number

    return total_sum

# Specify the path to your input.csv file
csv_file_path = 'input.csv'

# Call the function and get the result
result_sum = process_csv(csv_file_path)

print(f"Sum of combined numbers: {result_sum}")
