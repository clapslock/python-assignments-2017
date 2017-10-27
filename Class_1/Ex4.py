
while True:
    user_input = int(input("Please enter n (n>=2): "))
    if user_input >= 2:
        break
    else:
        continue

number_of_tree_levels = user_input -1
x = 1
tree_segment = "x"

for outer_loop_var in range(0, number_of_tree_levels):
    tree_segment = "x"
    x += 1
    for inner_loop_var in range(0, x):
        print (tree_segment)

        tree_segment += " x"