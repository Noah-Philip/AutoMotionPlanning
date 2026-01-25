import sim_loop as sim


def mazeSolve(cells, start, end):
    path = []
    found = mazeSolveRecursive(cells, start[0], start[1], cells[start[0]][start[1]], end, path, set())
    if found:
        path.reverse()
        return path
    return None

def mazeSolveRecursive(cells, row, col, lastZ, end, path, visited=None):
    if not inRange(cells, row, col):
        return False

    if visited is None:
        visited = set()

    if (row, col) in visited:
        return False
    
    currZ = cells[row][col]
    if(abs(lastZ - currZ) > sim.stepSize):
        return False
    
    visited.add((row, col))
    

    if (row, col) == end:
        path.append((row, col))
        return True
    
    if (mazeSolveRecursive(cells, row + 1, col, currZ, end, path, visited) or
        mazeSolveRecursive(cells, row - 1, col, currZ, end, path, visited) or
        mazeSolveRecursive(cells, row, col + 1, currZ, end, path, visited) or
        mazeSolveRecursive(cells, row, col - 1, currZ, end, path, visited)):
        path.append((row, col))
        return True
    return False

def inRange(cells, row, col):
    if row < 0 or row >= len(cells) or col < 0 or col >= len(cells[0]):
        return False
    return True