welcome= "welcome to the calori calculator, lets start by calculating how many calories does your body consumes at complete rest"

print(welcome.title())
kg = float(input("how much do you weight: "))
cm = float(input("how tall are you: "))
y = float(input("how old are you: "))

# 
result = 10 * kg + 6.25 * cm - 5 * y + 5

# 
print("Result:", result)