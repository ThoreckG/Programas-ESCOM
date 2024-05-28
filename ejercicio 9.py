class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.path = []

    def is_safe(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 1

    def find_path(self, x, y):
        if x == self.rows - 1 and y == self.cols - 1:
            self.path.append((x, y))
            return True
        
        if self.is_safe(x, y):
            self.path.append((x, y))
            
            if self.find_path(x + 1, y):
                return True
            
            if self.find_path(x, y + 1):
                return True
            
            self.path.pop()
        
        return False

    def get_path(self):
        if self.find_path(0, 0):
            return self.path
        else:
            return "No path found"

# Ejemplo de uso:
# 1 representa las celdas en las que el robot puede moverse.
# 0 representa las celdas bloqueadas.
grid = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

robot = Robot(grid)
path = robot.get_path()
print("Path from top-left to bottom-right:")
print(path)
