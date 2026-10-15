"""
name = "cd"
score = 7
score = score + 3
print(str(name) + " has", str(score) + " points")
"""
"""
def greet(name):
    message= "hellow, " + name + "!"
    return message
result = greet("nataly")
print (result)
"""
"""
def Letter_grade(score):
    if score >= 90:
        return ("a")
    elif score >= 80:
        return("b")
    elif score >= 70:
        return("c")
    elif score >= 60:
        return("d")
    else:
         return("f")

letter= Letter_grade(45)
print(letter)
"""
#program that ill fix eventually
"""
import pandas as pd
from datetime import datetime

class expenses_of_me:

    def __init__(my):
        my.expenses = pd.DataFrame(columns=["date", "category", "amount", "description"])

    def add_expense(my, category: str, amount: float, description: str = "" ):
        new_mamada= pd.DataFrame([{
            "date": datetime.now().strftime("%Y-%m-%D %H-%M"),
            "category": category,
            "amount": float(amount),
            "description": description
        }])
        my.expenses= pd.concat([my.expenses, new_mamada], ignore_index=True)
        print(f"added expenses: ${amount} for '{description}' under [{category}]")

    def category_info(my):
        if my.expenses.empty:
            print ("you have nothing")
            return None
        info= my.expenses.groupby("category")['amount'].sum().reset_index()
        info= info.sort_values(by= "category", ascending=False)
        return info

    def save_on_csv(my, filename: str= "my_expenses.cvs"):
        my.expenses.to_csv(filename, index=False)
        print("succese on saving data on", {filename})
        
if __name__ == "__main__":
    tracker=expenses_of_me

    tracker.add_expense("food", 20, 32)
    print("\n--- Spending Summary by Category ---")
    print(tracker.category_summary().to_string(index=False))
    tracker.save_on_csv()
    """

#here is chapter 3 work so far 
"""
names= ["mark", "jose,", "sofia,", "derek"]
print(f"i really like to see {names[0].title()}")

names[0]= "calavasa"
print(f"i really like {names[0]}")
names.append("papas")
print(names)
games=[]
games.append("cod 2")
games.append("sus")
games.append("amongus")
print(games)
games.insert(0, "pvp")
print(games)
del games[0]
print(games)
pop_games=games.pop()
print(games)
print(pop_games)
last_played= games.pop()
print(f'the last game i played was {last_played}')
games=["xd", "papa", "gg"]
games.remove("papa")
print(games)
expensive= "xd"
games.remove(expensive)
print(f"\n {expensive.title()} is too expensive for me")
games.insert(0,"galaga")
games.append("mine")
print(games)
del games[0]
print(games)
games.remove("mine")
print(games)
print(*games)
games.insert(0, "csgo")
games.append("gay")
print(*games, sep=", ")
print(games)
print(sorted(games))
print(f"heres the og list {games} \n and here is the sorted list {sorted(games)}")
games.reverse()
print(f"we can also do this in reverse {games}")
"""
