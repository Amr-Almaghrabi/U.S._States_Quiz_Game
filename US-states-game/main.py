import turtle
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

Moree = turtle.Turtle()
Moree.penup()
Moree.hideturtle()
Moree.speed("fastest")

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
states_x_coordinates = data["x"].to_list()
states_y_coordinates = data["y"].to_list()

screen.title("U.S. States Quiz")

correct_guesses = []

missed_states = []


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 U.S. States Quiz", prompt="Enter another state: ")
    if answer_state.title() == "Exit":
        break

    if answer_state.title() in states:
        Moree.goto(states_x_coordinates[states.index(answer_state.title())], states_y_coordinates[states.index(answer_state.title())])
        Moree.write(answer_state.title(), align="center", font= ("courier", 8 , "normal"))
        correct_guesses.append(answer_state.title())

    else:
        print("fail")


for i in states:
    if i in correct_guesses:
        pass
    elif i not in correct_guesses:
        missed_states.append(i)


states_to_learn = {
    "States to learn": missed_states,
}

df = pandas.DataFrame(states_to_learn)

df.to_csv("States_to_learn")

screen.exitonclick()
