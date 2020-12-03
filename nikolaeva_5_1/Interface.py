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
