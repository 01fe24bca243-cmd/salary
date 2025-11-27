import sys

if len(sys.argv) == 2:
    salary = float(sys.argv[1])
else:
    print("No salary provided. Using default salary...")
    salary = 50000   # default salary

bonus = salary * 0.10
total = salary + bonus

print("Bonus Amount:", bonus)
print("Total Salary:", total)
