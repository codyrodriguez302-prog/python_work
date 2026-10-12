while True:
      
    hola=input("welcomo to the calories calculator, just so you know this only works for males, wanna know how much should you eat Y/N:").upper()
    if hola=="N" or hola=="Y":
          break
    print(("that's not Y or N! Please try again.\n"))
if hola=="N":
    print("ok didnt wanna know either")
elif hola=="Y":

    print("arright lets start")
    def get_number(prompt):
        while True:
              try:
                    return float(input(prompt))
              except ValueError:
                    print("try again\n")
    kg= get_number("How much do you weight 'kgs': ")
    tall= get_number("how tall are you'cm':")
    age= get_number("how old are you'age':")

    bmr= (10 * kg) + (6.25 * tall) - (5 * age) + 5
    while True:
          
        activity_level= input("how much exercise do you do, including walking or running 'just answer a number' \n1 little to no exercise\n2 light exercise\n3 moderate exercise\n4 hard exercise\n5 Very hard exercise or physical job\nanswer:")
        if activity_level=="1" or activity_level=="2" or activity_level=="3" or activity_level=="4" or activity_level=="5":
              break
        print("try again\n")
    if activity_level == "1":
            activity_multiplier = 1.2
    elif activity_level == "2":
            activity_multiplier = 1.375
    elif activity_level == "3":
            activity_multiplier = 1.55
    elif activity_level == "4":
            activity_multiplier = 1.725
    elif activity_level == "5":
            activity_multiplier = 1.9
    else:
        activity_multiplier = 1.0

    print("allright so the calories that you should consume to maintain your weight are:" + str(bmr * float(activity_multiplier)))
    while True:
              
        goal=input("what are your goals?: \n1 maintain weight\n2 lose weight\n3 gain weight\nasnwer:")

        if goal=="1" or goal=="2" or goal=="3":
              break
        print(" try again\n")
    if goal=="1":
        print("ok so you should only eat", bmr * float(activity_multiplier))
    elif goal=="2":
        print("ok so you should only eat", bmr * float(activity_multiplier) - 500)
    elif goal=="3":
        print(("ok so you should only eat", bmr * float(activity_multiplier) + 500))
    else:
            print("not on the list pal")    
else:
    print("thats not Y or N")