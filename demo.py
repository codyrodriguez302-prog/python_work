import time
class Trip:
    def __init__(self,start,end,):
        self.start=start
        self.end=end
        t="06:00"
    def describe_trip(self,start,end):
        print(f"were traveling from {start} to {end} and we left at {self.t}")
introduction_message="You are about to go on a family trip and your dad gives you the honor to choose whe" \
"re do you wanna go, so where would you like to go: "
while True:
    user1=input("Are you ready to start this adventure? Y/N: ").lower()
    if user1 in ("y"):
        print("ok lets start")
        break
    elif user1 in ("n"):
        print("ok C U Next time")
    else:
        print("only Y or N,Try again")
for letter in introduction_message:
    print(letter, end="", flush=True)
    time.sleep(0.1)