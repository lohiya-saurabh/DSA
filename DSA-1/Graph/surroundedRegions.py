class Graph():
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.visitedRegions = set()
        self.activeRegions = []
        self.board = [[]]
        self.surroundedRegions = []

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.rows, self.cols = len(board), len(board[0])
        self.board = board
        for i in range(self.rows):
            for j in range(self.cols):
                currPoint = str(i) + "-" + str(j)
                self.activeRegions = []
                if board[i][j] == "O" and currPoint not in self.visitedRegions:
                    currentActiveRegion = [[i, j]]
                    self.captureNeighboursOfActiveRegion(currentActiveRegion)

        for point in self.surroundedRegions:
            board[point[0]][point[1]] = "X"
        print(board)

    def captureNeighboursOfActiveRegion(self, currentActiveRegion):
        currentRegionInfiltered = False

        while len(currentActiveRegion) != 0:
            neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            [i, j] = currentActiveRegion.pop()
            curr_point = str(i) + "-" + str(j)
            if curr_point in self.visitedRegions:
                continue
            self.visitedRegions.add(curr_point)
            self.activeRegions.append([i, j])
            for n in neighbours:
                cx = i + n[0]
                cy = j + n[1]
                neighbour = str(cx) + "-" + str(cy)
                if cx >= 0 and cx < self.rows and cy >= 0 and cy < self.cols:
                    if neighbour not in self.visitedRegions and self.board[cx][cy] == "O":
                        currentActiveRegion.append([cx, cy])
                else:
                    currentRegionInfiltered = True

        while len(self.activeRegions) != 0:
            point = self.activeRegions.pop()
            curr_point = str(point[0]) + "-" + str(point[1])
            if not currentRegionInfiltered:
                self.surroundedRegions.append([point[0], point[1]])


graph = Graph()
graph.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"],
            ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
