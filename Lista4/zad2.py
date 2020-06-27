import random
def createTree(tree, height):
    if height == 0:
        return tree

    option = random.randrange(1, 3) # decide if turn right or left
    if option == 1:
        if type(tree[1]) == list:
            tree[1] = createTree(tree[1], height)
            return tree
        if type(tree[2]) == list:
            tree[2] = createTree(tree[2], height)
            return tree
    else:
        if type(tree[2]) == list:
            tree[2] = createTree(tree[2], height)
            return tree
        if type(tree[1]) == list:
            tree[1] = createTree(tree[1], height)
            return tree

    valueR = random.randrange(101)
    valueL = random.randrange(101)
    option = random.randrange(1, 4)
    height -= 1
    if option == 1:
        tree[1] = [valueR, None, None]
        tree[2] = [valueL, None, None]
        return createTree(tree, height)
    elif option == 2:
        tree[2] = [valueL, None, None]
        return createTree(tree, height)
    elif option == 3:
        tree[1] = [valueR, None, None]
        return createTree(tree, height)

def printTree(tree):
    if tree[1]: 
        printTree(tree[1])
    print(tree[0], end=" ")
    if tree[2]:
        printTree(tree[2])

if __name__ == "__main__":
    #height = int(input("Enter height of tree: "))
    height = 4
    if height >= 1:
        root = random.randrange(100)
        height -= 1
        tree = createTree([root, None, None], height)
        print(f'Tree: {tree}\nINORDER: ', end="")
        printTree(tree)

