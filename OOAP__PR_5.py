class Win_Door:
     def __init__(self, x, y):
          self.square = x * y
class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.height = y
        self.lenght = z   
        self.wd = []
    def square(self):
        return 2 * self.lenght * (self.width + self.height)
    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))
    def workSurface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square
        return new_square
    def roll(self, wr, hr):
        return self.workSurface()/(wr*hr)
class Interface:
    def __init__(self):
        self.parametersRoom = []
        self.parametersWindow = []
        self.parametersDoors = []
        self.parametersRoll = []

        self.parametersRoom.append(float(input("Введите ширину комнаты: ")))
        self.parametersRoom.append(float(input("Введите высоту комнаты: ")))
        self.parametersRoom.append(float(input("Введите длину комнаты: ")))
        countWindow = int(input("Введите количество окон: "))
        for i in range(countWindow):
            self.parametersWindow.append(float(input(f'Введите высоту {i+1} - го окна: ')))
            self.parametersWindow.append(float(input(f'Введите ширину {i+1} - го окна: ')))
        countDoors = int(input("Введите количество дверей: "))
        for i in range(countDoors):
            self.parametersDoors.append(float(input(f'Введите высоту {i+1} - й двери: ')))
            self.parametersDoors.append(float(input(f'Введите ширину {i+1} - й двери: ')))
        self.parametersRoll.append(float(input('Введите ширину рулона: ')))
        self.parametersRoll.append(float(input('Введите длину рулона: ')))



i1 = Interface()
r1 = Room(i1.parametersRoom[0], i1.parametersRoom[1], i1.parametersRoom[2]) 
print(f' Oбщая  площадь квартиры: {r1.square()}')
for i,j in enumerate(range(0,len(i1.parametersWindow),2)):
    r1.addWD(i1.parametersWindow[i], i1.parametersWindow[i+1])  #площадь окон
for i,j in enumerate(range(0,len(i1.parametersDoors),2)):
    r1.addWD(i1.parametersDoors[i], i1.parametersDoors[i+1])  #площадь дверей
print(f'Oбклеиваемая площадь: {r1.workSurface()}') 
print(f'Количество рулонов обой: {r1.roll(i1.parametersRoll[0], i1.parametersRoll[1])}')

