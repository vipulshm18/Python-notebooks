# import turtle
# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# print(timmy)
#
# my_screen = turtle.Screen() #object.method
# my_screen.exitonclick()
#


from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])
table.align = "l"

print(table)