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
        if len(self.path) <= 1 or self.path[0] != self.path[-1]:
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
        return self.unbounded_objective()

    def save_state(self, node):
        node.state = (self.path.copy(), self.points.copy())

    def load_state(self, node):
        (self.path, self.points) = node.state

    def branch(self):

        # print('branch')

        def newChild(nextPoint, remainingPoints):
            child = pybnb.Node()
            childPath = self.path.copy()
            childPath.append(nextPoint)
            # print([p.label for p in childPath])
            child.state = (childPath, remainingPoints)
            return child

        if len(self.points) == 0 and self.path[0] != self.path[-1]:
            yield newChild(self.orig, [])
        else:
            for i in range(len(self.points)):
                if self.points[i] not in self.path:
                    remainingPoints = self.points.copy()
                    remainingPoints.pop(i)
                    yield newChild(self.points[i], remainingPoints)


def bnbSolve(points):
    print('============ bnbSolve ============')
    print([p.label for p in points])
    result = pybnb.solve(MyProblem(points), comm=None)
    print('best_node')
    print([p.label for p in result.best_node.state[0]])

    return result.best_node.state[0]
