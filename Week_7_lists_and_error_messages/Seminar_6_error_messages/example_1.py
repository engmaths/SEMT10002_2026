def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

values = []
result = calculate_average(values)
print(result)