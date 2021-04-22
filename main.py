import numpy as np
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import time

class Ship:
    def __init__(self, loc, safe_range=1.0, safe_area_shape=6):
        self.loc = loc
        self.safe_range = safe_range
        self.safe_area_shape = safe_area_shape
        self.safe_area = []
        self.generate_safe_area()
        print('Ship created')
        print('loc:%s  safe_range:%s  safe_area_shape:%s' % (self.loc, self.safe_range, self.safe_area_shape))
        print('safe_area:%s' % self.safe_area)
        print('------')

    def __getitem__(self, item):
        return self.__dict__.get(item, "100")

    def generate_safe_area(self):
        if self.safe_area_shape == 3:
            self.safe_area = [(self.loc[0], self.loc[1] + self.safe_range * 2),
                              (self.loc[0] + self.safe_range * np.sqrt(3), self.loc[1] - self.safe_range),
                              (self.loc[0] - self.safe_range * np.sqrt(3), self.loc[1] - self.safe_range)]
        elif self.safe_area_shape == 4:
            self.safe_area = [(self.loc[0], self.loc[1] + self.safe_range * np.sqrt(2)),
                              (self.loc[0] + self.safe_range * np.sqrt(3), self.loc[1]),
                              (self.loc[0], self.loc[1] - self.safe_range * np.sqrt(2)),
                              (self.loc[0] + self.safe_range * np.sqrt(3), self.loc[1])]
        elif self.safe_area_shape == 6:
            self.safe_area = [(self.loc[0], self.loc[1] + self.safe_range * 2 / np.sqrt(3)),
                              (self.loc[0] + self.safe_range, self.loc[1] + self.safe_range / np.sqrt(3)),
                              (self.loc[0] + self.safe_range, self.loc[1] - self.safe_range / np.sqrt(3)),
                              (self.loc[0], self.loc[1] - self.safe_range * 2 / np.sqrt(3)),
                              (self.loc[0] - self.safe_range, self.loc[1] - self.safe_range / np.sqrt(3)),
                              (self.loc[0] - self.safe_range, self.loc[1] + self.safe_range / np.sqrt(3))]
        else:
            print('safe_area_shape=%s invalid, only support 3,4,6' % self.safe_area_shape)

    def move(self, move_vector):
        self.loc = (self.loc[0] + move_vector[0], self.loc[1] + move_vector[1])
        self.generate_safe_area()



def main():
    shipA = Ship((1, 1), safe_range=0.5)
    shipB = Ship((1.5, 1.5), safe_range=0.5, safe_area_shape=3)



    plt.ion()

    inter_area = []

    for i in range(200):
        plt.clf()
        plt.title("clash")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim(0, 6)
        plt.ylim(0, 6)

        plt.plot(*Polygon(shipA['safe_area']).exterior.xy, color='r')
        plt.plot(*Polygon(shipB['safe_area']).exterior.xy, color='g')
        polyA = Polygon(shipA['safe_area']).convex_hull
        polyB = Polygon(shipB['safe_area']).convex_hull

        if polyA.intersects(polyB):
            plt.plot(*polyA.intersection(polyB).exterior.xy, color='b')

        inter_area.append(polyA.intersection(polyB).area)


        plt.pause(0.01)

        shipA.move((0.01, 0.01))
        shipB.move((0.015, 0))

        plt.ioff()
    plt.close()

    plt.plot(range(len(inter_area)), inter_area, color='b')

    plt.show()

def test1():
    shipA = Ship((1, 1), safe_range=0.5)
    shipB = Ship((2, 2), safe_range=1, safe_area_shape=3)

    plt.ion()

    inter_area = []

    for i in range(200):

        plt.clf()

        plt.subplot(121)
        plt.xlim(0, 6)
        plt.ylim(0, 6)
        plt.plot(*Polygon(shipA['safe_area']).exterior.xy, color='r')
        plt.plot(*Polygon(shipB['safe_area']).exterior.xy, color='g')
        polyA = Polygon(shipA['safe_area']).convex_hull
        polyB = Polygon(shipB['safe_area']).convex_hull

        if polyA.intersects(polyB):
            plt.plot(*polyA.intersection(polyB).exterior.xy, color='b')

        inter_area.append(polyA.intersection(polyB).area)
        plt.subplot(122)
        plt.plot(range(len(inter_area)), inter_area, color='b')

        plt.pause(0.01)

        shipA.move((0.01, 0.01))
        shipB.move((0.015, 0))

        plt.ioff()


def test2():
    shipA = Ship((1, 1), safe_range=0.5)
    shipB = Ship((2, 2), safe_range=1, safe_area_shape=3)

    plt.ion()

    inter_area = []

    for i in range(200):
        plt.clf()

        plt.plot(*Polygon(shipA['safe_area']).exterior.xy, color='r')
        plt.plot(*Polygon(shipB['safe_area']).exterior.xy, color='g')
        polyA = Polygon(shipA['safe_area']).convex_hull
        polyB = Polygon(shipB['safe_area']).convex_hull

        if polyA.intersects(polyB):
            plt.plot(*polyA.intersection(polyB).exterior.xy, color='b')

        inter_area.append(polyA.intersection(polyB).area)

        plt.plot(range(len(inter_area)), inter_area, color='b')

        plt.pause(0.01)

        shipA.move((0.01, 0.01))
        shipB.move((0.015, 0))

        plt.ioff()

if __name__ == '__main__':
    # main()
    test1()
    # test2()
