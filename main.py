import turtle
import pandas

FONT = ('Arial', 8, 'normal')
ALIGN = 'Center'

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
correct = 0
data = pandas.read_csv("50_states.csv")
w = data.to_records()


# creating dict of my structure for easier searching
def create_my_dict():
    states_dict = {"State": [], "cords": []}
    for states in range(50):
        states_dict['State'].append(w[states][1].lower())

        # Makes coords into a tuple for easier turtle.goto
        states_dict['cords'].append((w[states][2], w[states][3]))

    return states_dict


def find_state(state):
    # uses states name to get index in dict
    index = data_dict['State'].index(state)
    return index


def find_cords(state_index):
    # uses states index to get cords in dict
    cords = data_dict['cords'][state_index]
    return cords


def write_state(state_cords, state):
    pen.goto(state_cords)
    pen.write(arg=state.title(), align=ALIGN, font=FONT)


# how to access single item from row
# state_data = data[data.state == 'Alabama']
# print(state_data)
# print(state_data.y.item())

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data_dict = create_my_dict()

# # example of how to access data
# print(data_dict['State'][42], data_dict['cords'][42])

correct_list = []

while correct < 50:
    answer_state = screen.textinput(title=f"{correct}/50 states correct", prompt="Whats another state name? ").lower()
    if answer_state == 'exit':
        break
    if answer_state in data_dict['State'] and answer_state not in correct_list:
        correct_list.append(answer_state)
        index = find_state(answer_state)
        cords = find_cords(index)
        write_state(cords, answer_state)
        correct += 1

states_to_learn_list = [states for states in data_dict['State'] if states not in correct_list]

# for  states in data_dict['State']:
#     if states not in correct_list:
#         states_to_learn_list.append(states)
pandas.DataFrame(states_to_learn_list).to_csv("states_to_learn")
# states_to_learn_df=pandas.DataFrame(states_to_learn_list)
# states_to_learn_df.to_csv("states_to_learn")
screen.exitonclick()
