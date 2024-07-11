"""
class Parameter
<string> name of Parameter
<float> weight
<int> score
"""
class Parameter:
    def __init__(self, name : str) -> None:
        self.name : str = name
        self.weight : float = 0.0
        self.score : int = 0 
        return None
    
    def __str__(self):
        return f"<param {self.name} weighted {self.weight}>"

    def getScore(self) -> int:
        return self.score
    
    def setScore(self, score : int) -> None:
        self.score = score

    def getWeight(self) -> float:
        return self.weight

    def setWeight(self, weight : float) -> None:
        self.weight = weight

class Factor(Parameter):
    def __init__(self, name : str, id : int) -> None:
        super().__init__(name)
        self.id = id
        self.children : list[Parameter] = []

    def addParam(self, param : Parameter) -> None:
        self.children.append(param)

    def isEmpty(self) -> bool:
        return len(self.children) == 0

    def numberOfParams(self) -> int:
        return len(self.children)

    def __str__(self) -> str:
        return f"<factor {self.name} with {len(self.children)} children weighted {self.weight}"

"""
7 parameters of greenScore 
1. sustainableInvestment
2. greenBusinesses
3. localSpending
4. wasteManagement
5. transportPractices
6. carbonFootprint
7. energyEfficiency
"""
class greenScore:
    def __init__(self, id:int):
        self.id = id
        self.factors : list[Factor] = []

        self.s = Factor("sustainableInvestment", 1)
        self.g = Factor("greenBusinesses", 2)
        self.l = Factor("localSpending", 3)
        self.w = Factor("wasteManagement", 4)
        self.t = Factor("transportPractices", 5)
        self.c = Factor("carbonFootprint", 6)
        self.e = Factor("energyEfficiency", 7)

    
    def setup_sustainableInvestment(self):
        pass

    def setup_greenBusinesses(self):
        pass

    def setup_localSpending(self):
        pass 

    def setup_wasteManagement(self):
        pass

    def setup_transportPractices(self):
        pass

    def setup_carbonFootprint(self):
        pass 

    def setup_energyEfficiency(self):
        pass
