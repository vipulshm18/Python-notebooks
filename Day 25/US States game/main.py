import pandas as pd
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_df = pd.read_csv("50_states.csv")
guessed_states = []
us_states = list(states_df['state'])

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                     prompt="What's another State?")).title()
    if answer_state == "Exit":
        break
    if answer_state in list(states_df['state']):
        t = turtle.Turtle()
        t.hideturtle()
        guessed_states.append(answer_state)
        x_cor = states_df[states_df['state']== answer_state]["x"].values[0] #can use .item to get the first element
        y_cor = states_df[states_df['state'] == answer_state]["y"].values[0]
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(answer_state)


missing_states = [state for state in us_states if state not in guessed_states]
missing_states_df = pd.DataFrame(missing_states, columns=["Missing States"])
missing_states_df.to_csv("missing states.csv")

