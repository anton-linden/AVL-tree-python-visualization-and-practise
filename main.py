import random
import matplotlib.pyplot as plt
import networkx as nx


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        # Perform the normal BST insertion
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def display(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            self.display(root.left, level + 1, "L--- ")
            self.display(root.right, level + 1, "R--- ")

    def add_edges(self, root, graph, pos=None, x=0, y=0, layer=1):
        if root is not None:
            graph.add_node(root.val, pos=(x, y))
            if root.left:
                graph.add_edge(root.val, root.left.val)
                l = x - 1 / layer
                self.add_edges(root.left, graph, x=l, y=y - 1, layer=layer + 1)
            if root.right:
                graph.add_edge(root.val, root.right.val)
                r = x + 1 / layer
                self.add_edges(root.right, graph, x=r, y=y - 1, layer=layer + 1)


def plot_avl_tree(root):
    graph = nx.DiGraph()
    avl_tree = AVLTree()
    avl_tree.add_edges(root, graph)
    pos = nx.get_node_attributes(graph, 'pos')
    labels = {node: node for node in graph.nodes()}

    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=5000, node_color="skyblue", font_size=15,
            font_weight="bold", arrows=False)
    plt.show()


def display_avl_tree(numbers):
    avl_tree = AVLTree()
    root = None
    for number in numbers:
        root = avl_tree.insert(root, number)

    print("\nDisplaying the AVL Tree:")
    avl_tree.display(root)

    # Plot the AVL Tree
    plot_avl_tree(root)


def generate_unique_random_numbers(n, start=1, end=100):
    if n > (end - start + 1):
        raise ValueError("Range is too small to generate the required number of unique numbers.")

    return random.sample(range(start, end + 1), n)


def generate_unique_sorted_random_numbers(n, start=1, end=100, descending=False):
    if n > (end - start + 1):
        raise ValueError("Range is too small to generate the required number of unique numbers.")

    random_numbers = random.sample(range(start, end + 1), n)
    random_numbers.sort(reverse=descending)  # Sort the list in ascending or descending order
    return random_numbers


def get_left_left_rotation(_amount_of_numbers=6):
    return generate_unique_sorted_random_numbers(_amount_of_numbers, start=1, end=100, descending=False)


def get_right_right_rotation(_amount_of_numbers=6):
    return generate_unique_sorted_random_numbers(_amount_of_numbers, start=1, end=100, descending=True)


def get_random_numbers(_amount_of_numbers=6):
    return generate_unique_random_numbers(_amount_of_numbers, start=1, end=100)


def menu():
    while True:
        print("\nMenu:")
        print("1. Left-Left Rotation")
        print("2. Right-Right Rotation")
        print("3. Generate Random Numbers")
        print("4. Display AVL Tree")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            amount = int(input("Enter the number of random numbers to generate: "))
            result = get_left_left_rotation(amount)
            print("Left-Left Rotation Result:", result)
            input("Show solution by pressing enter")
            display_avl_tree(result)
        elif choice == '2':
            amount = int(input("Enter the number of random numbers to generate: "))
            result = get_right_right_rotation(amount)
            print("Right-Right Rotation Result:", result)
            input("Show solution by pressing enter")
            display_avl_tree(result)
        elif choice == '3':
            amount = int(input("Enter the number of random numbers to generate: "))
            result = get_random_numbers(amount)
            print("Random Numbers Result:", result)
            input("Show solution by pressing enter")
            display_avl_tree(result)
        elif choice == '4':
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            display_avl_tree(numbers)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()