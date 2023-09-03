import random

# TASK 1
class IslandClass():
    def __init__(self):
        self.grid = [["." for i in range(30)] for j in range(10)]


    def HideTreasure(self):
        self.grid[random.randint(0, 9)][random.randint(0, 29)] = "T"


    def DigHole(self, r, c):
        if self.grid[r][c] == "T":
            self.grid[r][c] = "X"
        else:
            self.grid[r][c] = "O"


    def GetSquare(self, r, c):
        return self.grid[r][c]


    def DisplayGrid(self):
        for row in range(10):
            display_str = ""
            for col in range(30):
                display_str += self.GetSquare(row, col)
            print(display_str)


def menu():
    island = IslandClass()
    island.HideTreasure()
    island.HideTreasure()
    island.HideTreasure()
    
    r, c = input("Row (1-10): "), input("Col (1-30): ")
    # if choice is valid
    if r.isdigit() and c.isdigit() and 1 <= int(r) <= 10 and 1 <= int(c) <= 30:
        island.DigHole(int(r), int(c))
        island.DisplayGrid()
    else:
        print("Invalid input")

menu()







        











