"""
Check intersection of 2 given lines.
We need to know the orientation of a set of 3 points from both of the lines.
We know it by slopes.

(y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)

"""

import matplotlib.pyplot as plt


class Point:

    points = []

    def __init__(self, xCoordinate, yCoordinate):

        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

        self.checkDuplicatedPoints()

    def checkDuplicatedPoints(self):

        if (self.xCoordinate, self.yCoordinate) not in self.points:
            self.points.append((self.xCoordinate, self.yCoordinate))
            print(f"Point {(self.xCoordinate, self.yCoordinate)} was read")

        else:
            print(f"{(self.xCoordinate, self.yCoordinate)} Point was already given")


def checkXCoordinateOnLine(point1, point2, point3):

    if (point1.xCoordinate <= max(point2.xCoordinate, point3.xCoordinate)) and (
        point1.xCoordinate >= min(point2.xCoordinate, point3.xCoordinate)
    ):

        return True

    return False


def checkYCoordinateOnLine(point1, point2, point3):
    if (point1.yCoordinate <= max(point2.yCoordinate, point3.yCoordinate)) and (
        point1.yCoordinate >= min(point2.yCoordinate, point3.yCoordinate)
    ):

        return True

    return False


def calculateSlopes(point1, point2, point3):

    try:
        firstSlope = float(
            (point2.yCoordinate - point1.yCoordinate)
            * (point3.xCoordinate - point2.xCoordinate)
        )
        secondSlope = float(
            (point2.xCoordinate - point1.xCoordinate)
            * (point3.yCoordinate - point2.yCoordinate)
        )

        slopeCalcuation = firstSlope - secondSlope

        return slopeCalcuation

    except Exception as e:
        print(e)


def getOrientation(point1, point2, point3):

    slopeCalcuation = calculateSlopes(point1, point2, point3)

    if slopeCalcuation > 0:

        return "Clockwise orientation"

    elif slopeCalcuation < 0:

        return "Counterclockwise orientation"

    else:

        return "Collinear orientation"


def checkCollinearAndOtherPointsOnLine(
    orientation, point1=None, point2=None, point3=None
):
    if (
        (orientation == "Collinear orientation")
        and checkXCoordinateOnLine(point1, point2, point3)
        and checkYCoordinateOnLine(point1, point2, point3)
    ):
        return True


def checkIntersection_NonCollinearCase(
    line1Point1, line1Point2, line2Point1, line2Point2
):

    orientation1 = getOrientation(line1Point1, line1Point2, line2Point1)
    orientation2 = getOrientation(line1Point1, line1Point2, line2Point2)
    orientation3 = getOrientation(line2Point1, line2Point2, line1Point1)
    orientation4 = getOrientation(line2Point1, line2Point2, line1Point2)

    if (orientation1 != orientation2) and (orientation3 != orientation4):
        return True
    return False


def checkIntersectionCollinearCase(line1Point1, line1Point2, line2Point1, line2Point2):

    orientation1 = getOrientation(line1Point1, line1Point2, line2Point1)
    orientation2 = getOrientation(line1Point1, line1Point2, line2Point2)
    orientation3 = getOrientation(line2Point1, line2Point2, line1Point1)
    orientation4 = getOrientation(line2Point1, line2Point2, line1Point2)

    orientations = [orientation1, orientation2, orientation3, orientation4]

    for orientation in orientations:
        intersectionTest = checkCollinearAndOtherPointsOnLine(
            orientation, line1Point1, line2Point1, line1Point2
        )
        if intersectionTest:
            return True

    return False


def plotGraph(line1Point1, line1Point2, line2Point1, line2Point2):

    plt.figure()
    line1_xCoordinates = [line1Point1.xCoordinate, line1Point2.xCoordinate]
    line1_yCoordinates = [line1Point1.yCoordinate, line1Point2.yCoordinate]

    plt.plot(line1_xCoordinates, line1_yCoordinates, label="line 1")

    line2_xCoordinates = [line2Point1.xCoordinate, line2Point2.xCoordinate]
    line2_yCoordinates = [line2Point1.yCoordinate, line2Point2.yCoordinate]

    plt.plot(line2_xCoordinates, line2_yCoordinates, label="line 2")
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.title("2 Lines Intersection Test")
    plt.legend()
    plt.show()


def checkIntersection(line1Point1, line1Point2, line2Point1, line2Point2):
    if checkIntersection_NonCollinearCase(
        line1Point1, line1Point2, line2Point1, line2Point2
    ) or checkIntersectionCollinearCase(
        line1Point1, line1Point2, line2Point1, line2Point2
    ):
        print("Intersection!! :)")
    else:
        print("No intersection :(")
    plotGraph(line1Point1, line1Point2, line2Point1, line2Point2)


if __name__ == "__main__":

    line1Point1 = Point(0, 1)
    line1Point2 = Point(8, 1)
    line2Point1 = Point(1, 3)
    line2Point2 = Point(5, 3)

    checkIntersection(line1Point1, line1Point2, line2Point1, line2Point2)

    line1Point1 = Point(10, 0)
    line1Point2 = Point(0, 10)
    line2Point1 = Point(0, 0)
    line2Point2 = Point(10, 10)

    checkIntersection(line1Point1, line1Point2, line2Point1, line2Point2)

    line1Point1 = Point(-5, -5)
    line1Point2 = Point(0, 0)
    line2Point1 = Point(1, 1)
    line2Point2 = Point(10, 10)

    checkIntersection(line1Point1, line1Point2, line2Point1, line2Point2)
