class animaltype:
    def __init__(self, name):
        self.name = (name)
    def makeNoise(self):
        print(self.name, " говорят: Кря!")
    def action(self):
        print('Если животное - ', self.name, '- кормим и собираем яйца')
    def weightcount(self):
        pass

class gooseclass(animaltype):
    def goosenames(self):
        global goosename1
        goosename1='Серый'
        global goosename2
        goosename2='Белый'
        print (f'В деревне живут {self.name} с именами: {goosename1} и {goosename2}')
    def weightcount(self):
        global gooseweight1
        gooseweight1=5
        global gooseweight2
        gooseweight2=6
        print(f'{self.name} весят: {goosename1} - {gooseweight1}кг, {goosename2} - {gooseweight2}кг')
class cowclass(animaltype):
    def cownames(self):
        global cowname
        cowname='Манька'
        print (f'В деревне живёт {self.name} с именем: {cowname}')
    def makeNoise(self):
        print(self.name, " говорит: Му-му!")
    def weightcount(self):
        global cowweight
        cowweight=1000
        print(f'{self.name} весит: {cowname} - {cowweight}кг')
    def action(self):
        print('Если животное - ', self.name, '- кормим и доим')
class sheepclass(animaltype):
    def sheepnames(self):
        global sheepname1
        sheepname1='Барашек'
        global sheepname2
        sheepname2='Кудрявый'
        print (f'В деревне живут {self.name} с именами: {sheepname1} и {sheepname2}')
    def makeNoise(self):
        print(self.name, " говорят: Беее!")
    def weightcount(self):
        global sheepweight1
        sheepweight1=200
        global sheepweight2
        sheepweight2=220
        print(f'{self.name} весят: {sheepname1} - {sheepweight1}кг, {sheepname2} - {sheepweight2}кг')
    def action(self):
        print('Если животное - ', self.name, '- кормим и стрижём')
class chickenclass(animaltype):
    def chickennames(self):
        global chickenname1
        chickenname1='Ко-ко'
        global chickenname2
        chickenname2='Кукареку'
        print (f'В деревне живут {self.name} с именами: {chickenname1} и {chickenname2}')
    def makeNoise(self):
        print(self.name, " говорят: Кукареку!")
    def weightcount(self):
        global chickenweight1
        chickenweight1=3
        global chickenweight2
        chickenweight2=4
        print(f'{self.name} весят: {chickenname1} - {chickenweight1}кг, {chickenname2} - {gooseweight2}кг')
class goatclass(animaltype):
    def goatnames(self):
        global goatname1
        goatname1='Рога'
        global goatname2
        goatname2='Копыта'
        print (f'В деревне живут {self.name} с именем: {goatname1} и {goatname2}')
    def makeNoise(self):
        print(self.name, " говорят: Бе-бе-бе-бе-бе!")
    def weightcount(self):
        global goatweight1
        goatweight1=300
        global goatweight2
        goatweight2=350
        print(f'{self.name} весят: {goatname1} - {goatweight1}кг, {goatname2} - {goatweight2}кг')
    def action(self):
        print('Если животное - ', self.name, '- кормим и доим')
class duckclass(animaltype):
    def ducknames(self):
        global duckname
        duckname='Кряква'
        print (f'В деревне живёт {self.name} с именем: {duckname}')
    def weightcount(self):
        global duckweight
        duckweight=4
        print(f'{self.name} весит: {duckname} - {duckweight}кг')


def gooseingormation():
        goose=gooseclass('Гуси')
        goose.goosenames()
        goose.makeNoise()
        goose.action()
        goose.weightcount()
def cowinformation():
        cow=cowclass('Корова')
        cow.cownames()
        cow.makeNoise()
        cow.action()
        cow.weightcount()
def sheepinformation():
        cow=sheepclass('Овцы')
        cow.sheepnames()
        cow.makeNoise()
        cow.action()
        cow.weightcount()
def chickeninformation():
        chicken=chickenclass('Курицы')
        chicken.chickennames()
        chicken.makeNoise()
        chicken.action()
        chicken.weightcount()
def goatinformation():
        goat=goatclass('Козы')
        goat.goatnames()
        goat.makeNoise()
        goat.action()
        goat.weightcount()
def duckinformation():
        duck=duckclass('Утка')
        duck.ducknames()
        duck.makeNoise()
        duck.action()
        duck.weightcount()

def wholeinformation():
    gooseingormation()
    cowinformation()
    sheepinformation()
    chickeninformation()
    goatinformation()
    duckinformation()
wholeinformation()

def wholeweightfunction(weightlist):
    theSum = 0
    for i in weightlist:
        theSum = theSum + i
    return theSum
print('Общая сумма веса всех животных =',wholeweightfunction([gooseweight1, gooseweight2, cowweight, sheepweight1, sheepweight2, chickenweight1, chickenweight2, goatweight1, goatweight2, duckweight]),'кг')


def maxweightfunction ():
    namelist=[goosename1, goosename2, cowname, sheepname1, sheepname2, chickenname1, chickenname2, goatname1, goatname2, duckname]
    weightlist=[gooseweight1, gooseweight2, cowweight, sheepweight1, sheepweight2, chickenweight1, chickenweight2, goatweight1, goatweight2, duckweight]
    biggestname=(sorted(list((zip(weightlist,namelist))))[-1][-1])
    biggestweight = (sorted(list((zip(weightlist, namelist))))[-1][0])
    print('Самый тяжёлый зверь - ',biggestname, '-', biggestweight, 'кг')

maxweightfunction()
