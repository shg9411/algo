import math


class Basket:
    def __init__(self):
        self.area = []
        self.load(None)
        self.unload()

    def load(self, n):
        raise NotImplementedError("load 메소드를 구현해야 합니다.")

    def unload(self):
        raise NotImplementedError("unload 메소드를 구현해야 합니다.")


class Gear:
    def __init__(self, r=0):
        self.__ratio = r

    def setRatio(self, r):
        self.__ratio = r

    def getRatio(self):
        return self.__ratio


class Tire:
    def __init__(self, r=0):
        self.__radius = r

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius


class Bike(Gear, Tire):
    def __init__(self):
        Gear.__init__(self)
        Tire.__init__(self)

    def speed(self):
        return self.getRatio()*2*math.pi*self.getRadius()


class MountainBike(Bike):

    def __init__(self):
        self.setRatio(1)
        self.setRadius(50)

    def setRatio(self, ratio):
        if ratio not in (1, 2, 3):
            raise Exception("기어 설정이 잘못되었습니다.")
        super().setRatio(ratio)


class RoadBike(Bike):

    def __init__(self):
        #기본 기어와 타이어 설정
        super().setRatio(1.5)
        self.setRadius(30)

    def setRatio(self, ratio):
        raise Exception("기어 설정이 불가능합니다.")


class CasualBike(Bike, Basket):

    def __init__(self):
        #기본 기어와 타이어 설정
        self.setRatio(1)
        self.setRadius(40)
        Basket.__init__(self)

    def load(self, n):
        self.area.append(n)

    def unload(self):
        return self.area.pop()
