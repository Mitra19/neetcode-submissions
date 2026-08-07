class Meal:
    def __init__(self,cost=0.0,takeOut=False,main="",drink=""):
        self.cost = cost
        self.takeOut = takeOut
        self.main = main
        self.drink = drink

    def getCost(self) -> float:
        return self.cost

    def setCost(self, cost: float) -> None:
        self.cost = cost

    def getTakeOut(self) -> bool:
        return self.takeOut

    def setTakeOut(self, takeOut: bool) -> None:
        self.takeOut = takeOut

    def getMain(self) -> str:
        return self.main

    def setMain(self, main: str) -> None:
        self.main = main

    def getDrink(self) -> str:
        return self.drink

    def setDrink(self, drink: str) -> None:
        self.drink = drink


class MealBuilder:
    
    def __init__(self):
        self.cost = 0.0
        self.takeOut = False
        self.main = ""
        self.drink = ""

    def addCost(self, cost: float) -> 'MealBuilder':
        self.cost = cost
        return self

    def addTakeOut(self, takeOut: bool) -> 'MealBuilder':
        self.takeOut = takeOut
        return self

    def addMainCourse(self, main: str) -> 'MealBuilder':
        self.main = main
        return self

    def addDrink(self, drink: str) -> 'MealBuilder':
        self.drink = drink
        return self

    def build(self) -> Meal:
        return Meal(self.cost,self.takeOut,self.main,self.drink)

