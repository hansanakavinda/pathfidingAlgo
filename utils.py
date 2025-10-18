from grid import Start, End

def success_criteria(path):
    if not path:
        return False
    return path[0] == Start and path[-1] == End

def cost_calculation(path):
    if not path:
        return float('inf') 
    return len(path) - 1