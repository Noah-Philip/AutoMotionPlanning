import sim_loop as loop 

if __name__ == "__main__":
    #Runs the simulation loop
    loop.simulationLoop

    start = (loop.startX, loop.startY)
    end = (loop.endX, loop.endY)


    canReach = loop.mazeSolve(loop.cells, start, end)

    print("Can I reach the end?!: ", canReach)
