def readInput(filename: str = 'input.txt'):
    with open(filename, 'r') as f:
        return f.read().splitlines()
