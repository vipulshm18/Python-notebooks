import pandas as pd

states_df = pd.read_csv("50_states.csv")
guessed_state = []
us_state = list(states_df['state'])

continue_asking = True
while continue_asking:
    answer_state = input("State?").title()
    guessed_state.append(answer_state)

    if len(guessed_state) == 3:
        continue_asking = False


for state in guessed_state:
    us_state.pop(us_state.index(state))

print(len(us_state))