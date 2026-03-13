class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_next_node(self, link_node):
        self.link_node = link_node

    def get_next_node(self):
        return self.link_node

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No more room!")

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This stack is empty.")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        return None

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def print_items(self):
        pointer = self.top_item
        print_list = []
        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print(self.name + " Stack:", print_list)


print("\nLet's play Towers of Hanoi!!")

# Create stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = [left_stack, middle_stack, right_stack]

# Get number of disks
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3:\n"))

# Fill left stack
for i in range(num_disks, 0, -1):
    left_stack.push(i)

# Optimal moves
num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in", num_optimal_moves, "moves")

# Function to get user input
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]

    while True:
        for i in range(len(stacks)):
            print("Enter", choices[i], "for", stacks[i].get_name())

        user_input = input("").upper()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

        print("Invalid choice. Try again.")


# Game loop
num_user_moves = 0

while right_stack.get_size() != num_disks:

    print("\nCurrent Stacks")
    for stack in stacks:
        stack.print_items()

    while True:
        print("\nMove FROM:")
        from_stack = get_input()

        print("\nMove TO:")
        to_stack = get_input()

        if from_stack == to_stack:
            print("Invalid move. Same stack!")
        elif from_stack.is_empty():
            print("Invalid move. Stack is empty!")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("Invalid move. Bigger disk cannot go on smaller disk!")

print("\nYou solved the puzzle in", num_user_moves, "moves.")
print("Optimal number of moves was", num_optimal_moves)