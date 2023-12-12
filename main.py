import random
import math

class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class TreeNode:
    def __init__(self, hero=None, parent=None):
        self.hero = hero
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

def mcts(hero_list, iterations):
    root = TreeNode()
    
    for _ in range(iterations):
        node = root
        # Selection phase
        while not all(child.visits > 0 for child in node.children) and not node.hero:
            unvisited_children = [child for child in node.children if child.visits == 0]
            if unvisited_children:
                node = random.choice(unvisited_children)
            else:
                exploration_weight = 1.0  # You can adjust this exploration parameter
                best_child = max(node.children, key=lambda child: (child.value / child.visits) + exploration_weight * math.sqrt(math.log(node.visits) / child.visits))
                node = best_child

        # Expansion phase
        if not node.hero:
            untried_heroes = [hero for hero in hero_list if hero not in [child.hero for child in node.children]]
            if untried_heroes:
                selected_hero = random.choice(untried_heroes)
                new_node = TreeNode(hero=selected_hero, parent=node)
                node.children.append(new_node)
                node = new_node

        # Simulation phase
        if not node.hero:
            # Handle the case where node.hero is None
            simulated_result = simulate_game(random.choice(hero_list))
        else:
            simulated_result = simulate_game(node.hero)  # Replace with your game simulation function
        backpropagate(node, simulated_result)

    # Return the hero with the highest value-to-visits ratio
    best_hero = max(root.children, key=lambda child: child.value / child.visits).hero
    return best_hero

def simulate_game(hero):
    # Replace this with your game simulation logic.
    # You can define how the game's outcome is determined based on hero power.
    return random.random() * hero.power

def backpropagate(node, result):
    while node:
        node.visits += 1
        node.value += result
        node = node.parent

if __name__ == "__main__":
    hero_list = [
        Hero("Hero1", 10),
        Hero("Hero2", 20),
        Hero("Hero3", 15),
        Hero("Hero4", 25)
    ]

    iterations = 1000
    best_hero = mcts(hero_list, iterations)
    print(f"The best hero to choose is {best_hero.name} with power {best_hero.power}")
