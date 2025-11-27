import sys
if len(sys.argv) == 3:
  salary = float(sys.argv[1])
else:
  print("no salary provided.using default salary")
  salary = 50000

bonus = salary * 0.10
total = salary + bonus 

print("bonus amount:",bonus)
print("total salary:",total)
