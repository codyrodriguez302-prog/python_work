import time

while True:
      
    hola=input("welcomo to the calories calculator, wanna know how much should you eat Y/N:").strip().upper()
    if hola=="N" or hola=="Y":
          break
    print(("that's not Y or N! Please try again.\n"))
if hola=="N":
    print("ok didnt wanna know either")
elif hola=="Y":
    print("arright lets start, just so you know this program uses metric, not imperial, but ill give you a hand")
    while True:
          chose_1=input("wanna convert pounds into kg: Y/N: ").strip().upper()
          if chose_1=="Y":
                try:
                      pounds=float(input("pounds here:"))
                      kilos=pounds / 2.205
                      print(kilos)
                      break
                except ValueError:
                      print("try again")
          elif chose_1=="N":
                break
          else:
                print("try again")
    while True:
          chose_2=input("wanna convert ft in cm? Y/N:").strip().upper()
          if chose_2=="Y":
                try:
                      feets=float(input("ft here:"))
                      centi=feets * 30.48
                      print(centi)
                      break
                except ValueError:
                      print("try again")
          elif chose_2=="N":
                break
          else:
                print("try again")
    def get_number(prompt):
          while True:
                try:
                      return float(input(prompt))
                except ValueError:
                      print("try again")
    while True:
      kg= get_number("how much do you weight 'kgs':")
      if kg>=float('500'):
            print('what are you, a car? try again')
      else:
            break
    while True:
      tall= get_number("how tall are you'cm':")
      if tall>=float("400"):
            print("sup lebron, try again")
      else:
            break

    while True:
      age= get_number("how old are you'age':")
      if age>= float("150"):
            print("how were dinosaurs, try again")
      else:
            break
    bmr= (10 * kg) + (6.25 * tall) - (5 * age) + 5
    tmb=(10 * kg) + (6.25 * tall) - (5 * age) - 161
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
    while True:
      gender=input("male or female? M/F: ").strip().upper()
      if gender=="M":
            print("allright so the calories that you should consume to maintain your weight are:" + str(bmr * float(activity_multiplier)))
            break
      elif gender=="F":
            print("allright so the calories that you should consume to maintain your weight are:" + str(tmb * float(activity_multiplier))) 
            break
      else: 
            print("try again")
    while True:
        
        goal=input("what are your goals?: \n1 maintain weight\n2 lose weight\n3 gain weight\nasnwer:")

        if goal == "1" or goal == "2" or goal == "3":
            break
    print("try again\n")

if gender == "M":
    if goal == "1":
        print("ok so you should only eat", bmr * float(activity_multiplier))
    elif goal == "2":
        print("ok so you should only eat", bmr * float(activity_multiplier) - 500)
    elif goal == "3":
        print("ok so you should only eat", bmr * float(activity_multiplier) + 500)
    else:
        print("not on the list pal")

elif gender == "F":
    if goal == "1":
        print("ok so you should only eat", tmb * float(activity_multiplier))
    elif goal == "2":
        print("ok so you should only eat", tmb * float(activity_multiplier) - 500)
    elif goal == "3":
        print("ok so you should only eat", tmb * float(activity_multiplier) + 500)
    else:
        print("not on the list pal")

else:
    print("whahappened")
    