import random

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def create_tree(self, root, height_aim, height=1, level=1):
        if height == height_aim:
            return root

        if self.children:
            rand_child = random.randrange(round(1.5 * len(self.children)))
            if rand_child < len(self.children): # go deep
                return self.children[rand_child].create_tree(root, height_aim, height, level + 1)
        
        # add new child
        value = random.randrange(101)
        self.children.append(Node(value))
        level += 1
        if level > height:
            return root.create_tree(root, height_aim, height + 1, 1)
        else:
            return root.create_tree(root, height_aim, height, 1)

    def print_tree_nice(self,level=1):    # for debugging only
        print('\t' * level, end="")
        print(self.value)
        for c in self.children:
            c.print_tree_nice(level + 1)

    def print_tree_inorder(self):
        if self.children:
            self.children[0].print_tree_inorder()
        print(self.value)
        for x in self.children[1:]:
            x.print_tree_inorder()

if __name__ == "__main__":
    #height = int(input("Enter height of tree: "))
    height = 4
    root = Node(random.randrange(101))
    root.create_tree(root,height)
    root.print_tree_inorder()

