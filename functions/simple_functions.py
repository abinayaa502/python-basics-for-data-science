def add(a, b):
    return a + b

def average(numbers):
    return sum(numbers) / len(numbers)

sum_result = add(10, 5)
print("Sum:", sum_result)

scores = [78, 85, 90, 92]
avg_result = average(scores)
print("Average Score:", avg_result)
