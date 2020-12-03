

i1 = Interface()
r1 = Room(i1.parametersRoom[0], i1.parametersRoom[1], i1.parametersRoom[2]) 
print(f' Oбщая  площадь квартиры: {r1.square()}')
for i,j in enumerate(range(0,len(i1.parametersWindow),2)):
    r1.addWD(i1.parametersWindow[i], i1.parametersWindow[i+1])  #площадь окон
for i,j in enumerate(range(0,len(i1.parametersDoors),2)):
    r1.addWD(i1.parametersDoors[i], i1.parametersDoors[i+1])  #площадь дверей
print(f'Oбклеиваемая площадь: {r1.workSurface()}') 
print(f'Количество рулонов обой: {r1.roll(i1.parametersRoll[0], i1.parametersRoll[1])}')

