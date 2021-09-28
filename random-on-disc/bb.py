from sys import path
from Point import Point
import pybnb
# define a branch-and-bound problem

from tsp import orderPoints, routeLength, tspNearestNeighbour


class MyProblem(pybnb.Problem):

    def __init__(self, points):
        self.orig = Point(0, 0)
        self.points = points.copy()
        self.path = [self.orig]

    def sense(self):
        return pybnb.minimize

    def objective(self):
        if len(self.path)-2 < len(self.points):
            return self.infeasible_objective()
        else:
            return routeLength(self.path)

    # def bound(self):
    #     print([p.label for p in self.path], [p.label for p in self.points])
    #     pointsNotInPath = [self.orig] + [
    #         point for point in self.points if point not in self.path]

    #     orderedPointsIndices = tspNearestNeighbour(pointsNotInPath)

    #     orderedPoints = orderPoints(orderedPointsIndices, pointsNotInPath)

    #     length = routeLength(self.path + orderedPoints)
    #     print([p.label for p in self.path], [p.label for p in orderedPoints])
    #     print(length)
    #     return length

    def bound(self):
        return 0

    def save_state(self, node):
        node.state = (self.path.copy(), self.points.copy())

    def load_state(self, node):
        (self.path, self.points) = node.state

    def branch(self):

        # print('branch')

        def newChild(nextPoint):
            child = pybnb.Node()
            childPath = self.path.copy()
            childPath.append(nextPoint)
            # print([p.label for p in childPath])
            child.state = (childPath, self.points.copy())
            return child

        if len(self.path) == len(self.points)+1:
            yield newChild(self.orig)
        else:
            for i in range(len(self.points)):
                if self.points[i] not in self.path:
                    yield newChild(self.points[i])


def bnbSolve(points):
    print('============ bnbSolve ============')
    print([p.label for p in points])
    result=pybnb.solve(MyProblem(points), comm = None)
    print('best_node')
    print([p.label for p in result.best_node.state[0]])

    return result.best_node.state[0]
