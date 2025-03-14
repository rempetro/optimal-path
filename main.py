import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
import random


class PointCollector:
    """
    A class to represent the point collector.

    Attributes
    ----------
    num_points : int
        Number of points to collect.
    random_seed : int
        Random seed for generating point positions.
    positions : np.ndarray
        Positions of the base and points.
    distance_matrix : np.ndarray
        Matrix of distances between positions.
    visited_points : set
        Set of visited points.
    connections : list
        List of connections between points.
    operation_count : int
        Number of operations performed.

    Methods
    -------
    __init__(num_points=30):
        Constructs all the necessary attributes for the point collector object.

    generate_positions():
        Generates random positions for points and calculates the distance matrix.

    find_nearest_unvisited_point(current_point):
        Finds the nearest unvisited point from the current point.

    collect_points():
        Collects all points and returns to the base, ensuring each point is visited only once.

    plot_path():
        Plots the optimal path for collecting points and returning to the base.

    get_operation_count():
        Returns the number of operations performed.

    get_random_seed():
        Returns the random seed used.
    """

    def __init__(self, num_points=30):
        """
        Constructs all the necessary attributes for the point collector object.

        Parameters
        ----------
        num_points : int, optional
            Number of points to collect (default is 30).
        """
        self.num_points = num_points
        self.random_seed = random.randint(100000, 999999)
        self.positions = None
        self.distance_matrix = None
        self.visited_points = set()
        self.connections = []
        self.operation_count = 0

    def generate_positions(self):
        """
        Generates random positions for points and calculates the distance matrix.

        Returns
        -------
        None
        """
        np.random.seed(self.random_seed)
        points_positions = np.random.rand(self.num_points, 2) * 100
        base_position = np.array([50, 50])
        self.positions = np.vstack([base_position, points_positions])
        self.distance_matrix = squareform(pdist(self.positions))

    def find_nearest_unvisited_point(self, current_point):
        """
        Finds the nearest unvisited point from the current point.

        Parameters
        ----------
        current_point : int
            Index of the current point.

        Returns
        -------
        int
            Index of the nearest unvisited point.
        """
        distances = self.distance_matrix[current_point]
        nearest_point = None
        min_distance = float('inf')

        for i in range(len(distances)):
            if i not in self.visited_points and distances[i] < min_distance:
                nearest_point = i
                min_distance = distances[i]

        return nearest_point

    def collect_points(self):
        """
        Collects all points and returns to the base, ensuring each point is visited only once.

        Returns
        -------
        None
        """
        current_point = 0
        self.visited_points.add(current_point)

        while len(self.visited_points) < len(self.positions):
            nearest_point = self.find_nearest_unvisited_point(current_point)
            self.operation_count += len(self.distance_matrix[current_point])  # Count the number of distance comparisons

            if nearest_point is not None:
                self.connections.append((current_point, nearest_point))
                self.visited_points.add(nearest_point)
                current_point = nearest_point

        # Connect the last point back to the base
        self.connections.append((current_point, 0))

    def plot_path(self):
        """
        Plots the optimal path for collecting points and returning to the base.

        Returns
        -------
        None
        """
        fig = plt.figure(figsize=(5, 5))

        # Set window title to 'Optimal Path'
        fig.canvas.manager.set_window_title('Optimal Path')
        plt.plot(self.positions[:, 0], self.positions[:, 1], 'go', markersize=5, markerfacecolor='g')
        plt.plot(self.positions[0, 0], self.positions[0, 1], 'ko', markersize=5, markerfacecolor='k')

        for connection in self.connections:
            plt.plot([self.positions[connection[0], 0], self.positions[connection[1], 0]],
                     [self.positions[connection[0], 1], self.positions[connection[1], 1]], 'b-')

        plt.title('Optimal Path')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.grid(True)
        plt.show()

    def get_operation_count(self):
        """
        Returns the number of operations performed.

        Returns
        -------
        int
            Number of operations performed.
        """
        return self.operation_count

    def get_random_seed(self):
        """
        Returns the random seed used.

        Returns
        -------
        int
            Random seed used.
        """
        return self.random_seed


# Example usage:
collector = PointCollector(num_points=50)
collector.generate_positions()
collector.collect_points()
collector.plot_path()

print(f"Random seed used: {collector.get_random_seed()}")
print(f"Number of operations performed: {collector.get_operation_count()}")