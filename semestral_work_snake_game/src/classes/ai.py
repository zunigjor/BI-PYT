import numpy as np
import random

from semestralka.src.config import gameconfig as gc


class Maze:
    """Maze class. Generates a hamiltonian cycle for the snake."""
    def __init__(self):
        self.board = np.empty((gc.GRID_WIDTH, gc.GRID_HEIGHT), dtype=object)
        self.generate_simple_ham_cycle()
        # self.generate_random_ham_cycle() // TODO

    def get_directions_board(self):
        return self.board

    # SIMPLE HAMILTONIAN CYCLE #########################################################################################
    def generate_simple_ham_cycle(self):
        """Generates a simple hamiltonian cycle."""
        for h in range(gc.GRID_HEIGHT):
            self.board[h][0] = gc.UP  # "UP"
        self.board[0][0] = gc.RIGHT  # "RIGHT"
        for h in range(1, gc.GRID_HEIGHT):
            for w in range(gc.GRID_WIDTH):
                if h == 1 or h == gc.GRID_WIDTH - 1:
                    self.board[w][h] = gc.DOWN  # "DOWN"
                else:
                    if w % 2 == 0:
                        self.board[w][h] = gc.RIGHT  # "RIGHT"
                    else:
                        self.board[w][h] = gc.LEFT  # LEFT
        for h in range(gc.GRID_HEIGHT):
            if h % 2 == 0:
                self.board[h][1] = gc.RIGHT  # "RIGHT"
                self.board[h][gc.GRID_WIDTH - 1] = gc.DOWN  # "DOWN"
            else:
                self.board[h][1] = gc.DOWN  # "DOWN"
                self.board[h][gc.GRID_WIDTH - 1] = gc.LEFT  # LEFT
        self.board[gc.GRID_HEIGHT - 1][1] = gc.LEFT  # LEFT
        return
    ####################################################################################################################
    # TODO random hamiltonian cycle generation
    class Node:
        """Node used in random hamiltonian cycle"""
        def __init__(self):
            self.visited = False
            self.up = False
            self.down = False
            self.left = False
            self.right = False
            self.can_go_up = True
            self.can_go_down = True
            self.can_go_left = True
            self.can_go_right = True
            self.up_weight = random.choice([1, 2, 3, 4])
            self.down_weight = random.choice([1, 2, 3, 4])
            self.left_weight = random.choice([1, 2, 3, 4])
            self.right_weight = random.choice([1, 2, 3, 4])

    def create_empty_graph(self):
        """Creates an empty weighed graph."""
        graph_w = int(gc.GRID_WIDTH / 2)
        graph_h = int(gc.GRID_HEIGHT / 2)
        graph = np.empty((graph_w, graph_h), dtype=object)
        for w in range(graph_w):
            for h in range(graph_h):
                graph[w][h] = self.Node()
        for w in range(graph_w):
            graph[0][w].can_go_up = False
            graph[graph_h - 1][w].can_go_down = False
        for h in range(graph_h):
            graph[h][0].can_go_left = False
            graph[h][graph_w - 1] = False
        return graph

    def make_min_tree(self, graph):
        """Creates a min span tree on a graph. Uses Prim (Jarnik's) algorithm"""
        # start at top left corner of the 2d graph
        start = graph[0][0]
        start.visited = True
        start_x = 0
        start_y = 0
        num_of_visited_nodes = 1
        total_nodes = int(gc.GRID_HEIGHT / 2 * gc.GRID_HEIGHT / 2)
        visited_nodes = [start]

        # TODO Prim (Jarnik's) algorithm

        return graph

    def draw_around_span_tree(self, maze):
        """"""
        # TODO
        pass

    def generate_random_ham_cycle(self):
        """
        Generates a random hamiltonian cycle.
        Uses Jarnik's algorithm to create a minimal spanning tree.
        The spanning tree groups four nodes of the original board into a single node.
        Then the algorithm draws around the tree to generate a hamiltonian cycle.
        Inspiration:
        https://codeforces.com/blog/entry/79788
        """
        empty_graph = self.create_empty_graph()  # empty graph with weighted vertices

        min_span_tree = self.make_min_tree(empty_graph)  # min span tree to draw around

        self.draw_around_span_tree(min_span_tree)

        return


def get_new_direction(snake, food, maze):
    """
    Returns a new direction for the snake.
    @:return gc.UP or gc.DOWN or gc.LEFT or gc.RIGHT
    """
    # return random.choice([gc.UP, gc.DOWN, gc.LEFT, gc.RIGHT])

    snake_head_x = int(snake.get_head()[0] / gc.SQUARE_SIZE)
    snake_head_y = int(snake.get_head()[1] / gc.SQUARE_SIZE)
    snake_tail_x = int(snake.get_tail()[0] / gc.SQUARE_SIZE)
    snake_tail_y = int(snake.get_tail()[1] / gc.SQUARE_SIZE)

    food_x = int(food.get_postion()[0] / gc.SQUARE_SIZE)
    food_y = int(food.get_postion()[1] / gc.SQUARE_SIZE)

    next_dir = maze.get_directions_board()[snake_head_y][snake_head_x]

    return next_dir
