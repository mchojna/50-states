import turtle
import pandas as pd
import csv

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("State Guessing Game")

states = pd.read_csv("50_states.csv")
states_dict = states.to_dict()
guess_list = []
score_num = 0
round_num = 1
to_learn = []

while score_num < 50:
    guess = screen.textinput(f"[{round_num} Round] {score_num}/50 States Correct ", "What is another state name?")
    if guess.lower() == "exit":
        break
    elif guess.title() not in guess_list:
        for num in states_dict["state"]:
            if guess.title() == states_dict["state"][num]:
                text = turtle.Turtle()
                text.hideturtle()
                text.penup()
                text.color("black")
                text.setposition(x=states_dict["x"][num], y=states_dict["y"][num])
                text.write(arg=states_dict["state"][num], align="center", font=("Calibre", 10, "normal"))

                score_num += 1
                guess_list.append(guess.title())
        round_num += 1

if score_num == 50:
    print(f"Congratulations! You managed to complete the whole map in only {round_num} rounds!")
else:
    for num in states_dict["state"]:
        check = 0
        for item in guess_list:
            if item == states_dict["state"][num]:
                check = 0
                break
            else:
                check = 1
        if check == 1:
            to_learn.append(states_dict["state"][num])

df = pd.DataFrame(data=to_learn, columns=["state"])
print(df.to_csv("states_to_learn.csv"))



