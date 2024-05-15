class lightonoff:

    def __init__(thisGrid):#creating grid
        thisGrid.grid = [[1 for _ in range(3)] for _ in range(3)]  


    def isSolved(thisGrid):
        return all(
            thisGrid.grid[i][j] == 0 for i in range(3) for j in range(3))


    def start(thisGrid):
        
        while not thisGrid.isSolved():
            thisGrid.displayGrid()
           
            x, y = map(int, input("Enter row and column. Do a space between the numbers:): ").split())
            if 0 <= x < 3 and 0 <= y < 3:
                thisGrid.togleLight(x, y) 

        print("YOU WON!!")

        thisGrid.displayGrid()

    def displayGrid(thisGrid):
        for row in thisGrid.grid:
            print(' '.join(str(cell) for cell in row))
        print()


    def togleLight(thisGrid, x, y):
        #  function to switch lights 
        def change_Number(i, j):

            if 0 <= i < 3 and 0 <= j < 3:
                thisGrid.grid[i][j] = 1 - thisGrid.grid[i][j]
                
        change_Number(x, y)
        change_Number(x - 1, y) # UPPER
        change_Number(x + 1, y)  # down
        change_Number(x, y - 1)  
        change_Number(x, y + 1)  
        
if True:
    lightGame = lightonoff()

    lightGame.start()