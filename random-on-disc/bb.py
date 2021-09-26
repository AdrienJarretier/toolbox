from Point import Point
import pybnb
# define a branch-and-bound problem

from tsp import routeLength, tspNearestNeighbour


class MyProblem(pybnb.Problem):

    def __init__(self, points):
        self.points = points.copy()
        print('WARNING REMOVE COPY HERE')
        self.path = []

    def sense(self):
        return pybnb.minimize

    def objective(self):
        return routeLength(self.path)

    def bound(self):
        orderedPointsIndices = tspNearestNeighbour(self.path)

        print(orderedPointsIndices)

        orderedPoints = []
        for i in range(len(orderedPointsIndices)):
            orderedPointIndex = orderedPointsIndices[i]
            point = self.points[orderedPointIndex-1]
            orderedPoints.append(point)

        length = routeLength(orderedPoints)
        print('length :', length)
        return length

    def save_state(self, node):
        node.state = self.path

    def load_state(self, node):
        self.path = node.state

    def branch(self):

        for i in range(len(self.points)):
            if self.points[i] not in self.path:
                child = pybnb.Node()
                child.state = self.path.append(self.points[i])
                yield child


def solve(points):
    result = pybnb.solve(MyProblem(points), comm=None)
    print(result.solution_status)
