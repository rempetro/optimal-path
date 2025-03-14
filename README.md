# Point Collector

**Point Collector** is a Python program designed to simulate the optimal collection of points in a two-dimensional space and return to the base. Its main features include generating random point positions, identifying the nearest unvisited point, and visualizing the optimal path.

## Features

- **Random Point Generation**  
  Randomly generates positions for a specified number of points within a two-dimensional space.

- **Path Optimization**  
  Ensures that all points are visited only once before returning to the base.

- **Graphical Visualization**  
  Displays the optimal path graphically, allowing easy interpretation.

- **Operation Statistics**  
  Tracks the number of operations performed during the process and provides information about the random seed used for reproducibility.

## Visualization

The program generates a visual representation of the optimal path for point collection and return, similar to the example shown below:

<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/005.png" alt="Optimal Path for 5 Points" width="200px">
<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/010.png" alt="Optimal Path for  5 Points" width="200px">
<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/015.png" alt="Optimal Path for 15 Points" width="200px">
<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/020.png" alt="Optimal Path for 5 Points" width="200px">
<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/025.png" alt="Optimal Path for 25 Points" width="200px">
<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/050.png" alt="Optimal Path for 50 Points" width="200px">
<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/500.png" alt="Optimal Path for 500 Points" width="200px">
<img src="https://raw.githubusercontent.com/rempetro/optimal-path/refs/heads/main/examples/5000.png" alt="Optimal Path for 500 Points" width="200px">

## Usage

1. **Create an Instance**  
   Initialize the `PointCollector` class with the desired number of points:
   ```python
   collector = PointCollector(num_points=30)

2. **Generate Point Positions**  
   Randomly generate positions for the specified number of points:
   ```python
   collector.generate_positions()
   
3. **Collect Points**  
   Visit all points and return to the base:
   ```python
   collector.collect_points()
   
4. **Visualize the Path**  
   Display the optimal path on a graphical plot:
   ```python
   collector.plot_path()
   
5. **Retrieve Statistics**  
   Access information about the random seed and the number of operations performed:
   ```python
   print(f"Random seed used: {collector.get_random_seed()}")
   print(f"Number of operations performed: {collector.get_operation_count()}
