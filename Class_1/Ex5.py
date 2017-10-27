
space_filler = " "
original_space_filler_value = ""

while True:
    user_input = int(input("Please enter n (n>=1): "))
    if user_input >= 1:
        original_space_filler_value = " " * (user_input * 2 + 1)
        break
    else:
        continue

number_of_tree_levels = user_input
x = 1
tree_segment = ""

for outer_loop_var in range(0, number_of_tree_levels):
    left_tree_segment = ""
    right_tree_segment = ""
    x += 1
    space_filler = original_space_filler_value
    for inner_loop_var in range(0, x):
        print (space_filler, left_tree_segment, "x", right_tree_segment)
        space_filler = space_filler[:-1]
        left_tree_segment += "x"
        right_tree_segment += "x"