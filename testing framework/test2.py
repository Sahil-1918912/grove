# imports 
from typing import List

class Parameter:
    def __init__(self, name : str, id : int) -> None:
        self.name : str = name
        self.id = id 
        self.weight : float = 0.0
        self.score : int = 0 
        return None
    
    def __str__(self):
        return f"<param {self.name} weighted {self.weight}>"

    def get_score(self) -> int:
        return self.score
    
    def set_score(self, score : int) -> None:
        self.score = score

    def get_weight(self) -> float:
        return self.weight

    def set_weight(self, weight : float) -> None:
        self.weight = weight

# sub-parameters
class investingInSustainableEnergy(Parameter):
    def __init__(self) -> None:
        super().__init__("investingInSustainableEnergy",101)

class greenStocksProfile(Parameter):
    def __init__(self) -> None:
        super().__init__("greenStocksProfile", 102)

class buyingFromGreenBiz(Parameter):
    def __init__(self) -> None:
        super().__init__("buyingFromGreenBiz",201)

class farmerMarkets(Parameter):
    def __init__(self) -> None:
        super().__init__("farmerMarkets",202)

class investingInLocalBiz(Parameter):
def __init__(self) -> None:
        super().__init__("investingInLocalBiz",203)

# LWMP - local waste management programs
class participationInLWMP(Parameter):
    def __init__(self) -> None:
        super().__init__("participationInLWMP",301)

class kitchenGarden(Parameter):
    def __init__(self) -> None:
        super().__init__("kitchenGarden",401)

class eWasteDisposal(Parameter):
    def __init__(self) -> None:
        super().__init__("eWasteDisposal",402)

class usageOfPublicTransport(Parameter):
    def __init__(self) -> None:
        super().__init__("usageOfPublicTransport",501)

class proportionOfFamilyMembersToVehicles(Parameter):
    def __init__(self) -> None:
        super().__init__("proportionOfFamilyMembersToVehicles",502)

class havingFossilFuelVehicles(Parameter):
    def __init__(self) -> None:
        super().__init__("havingFossilFuelVehicles",503)

class EVOwnershipAndUsage(Parameter):
    def __init__(self) -> None:
        super().__init__("EVOwnershipAndUsage",504)

class mileageOfCar(Parameter):
    def __init__(self) -> None:
        super().__init__("mileageOfCar",601)

class unitsOfElectricityConsumed(Parameter):
    def __init__(self) -> None:
        super().__init__("unitsOfElectricityConsumed",701)

class surveyPoints(Parameter):
    def __init__(self) -> None:
        super().__init__("surveyPoints",702)

class renewableEnergyUsage(Parameter):
    def __init__(self) -> None:
        super().__init__("renewableEnergyUsage",703)

# parameters 
class sustainableInvestment(Parameter):
    def __init__(self) -> None:
        super().__init__("sustainableInvestment",100)
        self.children : List[Parameter] = []
        
class greenBusinesses(Parameter):
    def __init__(self) -> None:
        super().__init__("greenBusinesses",200)
        self.children : List[Parameter] = []

class localSpending(Parameter):
    def __init__(self) -> None:
        super().__init__("localSpending",300)
        self.children : List[Parameter] = []
        
class wasteManagement(Parameter):
    def __init__(self) -> None:
        super().__init__("wasteManagement",400)
        self.children : List[Parameter] = []

class transportPractices(Parameter):
    def __init__(self) -> None:
        super().__init__("transportPractices",500)
        self.children : List[Parameter] = []
        
class carbonFootprint(Parameter):
    def __init__(self) -> None:
        super().__init__("carbonFootprint",600)
        self.children : List[Parameter] = []

class energyEfficiency(Parameter):
    def __init__(self) -> None:
        super().__init__("energyEfficiency",700)
        self.children : List[Parameter] = []
        
# greenScore class starts here 
class greenScore:
    def __init__(self, userID : int) -> None:
        self.userID = userID
        
        # initialising the parameters
        self.s = sustainableInvestment()
        self.g = greenBusinesses()
        self.l = localSpending()
        self.w = wasteManagement()
        self.t = transportPractices()
        self.c = carbonFootprint()
        self.e = energyEfficiency()

        # iniialising the sub-parameters
        self.s_ise = investingInSustainableEnergy()
        self.s_gsp = greenStocksProfile()
        self.g_bfg = buyingFromGreenBiz()
        self.g_fmk = farmerMarkets()
        self.g_ilb = investingInLocalBiz()
        self.l_pil = participationInLWMP()
        self.w_kgr = kitchenGarden()
        self.w_ewd = eWasteDisposal()
        self.t_upt = usageOfPublicTransport()
        self.t_pfv = proportionOfFamilyMembersToVehicles()
        self.t_hff = havingFossilFuelVehicles()
        self.t_evo = EVOwnershipAndUsage()
        self.c_moc = mileageOfCar()
        self.e_uec = unitsOfElectricityConsumed()
        self.e_spt = surveyPoints()
        self.e_reu = renewableEnergyUsage()

    def setup(self) -> bool:
        try:
            self.s.children.extend([
                self.s_ise,
                self.s_gsp
            ])

            self.g.children.extend([
                self.g_bfg,
                self.g_fmk,
                self.g_ilb
            ])

            self.l.children.extend([
                self.l_pil
            ])

            self.w.children.extend([
                self.w_kgr,
                self.w_ewd
            ])

            self.t.children.extend([
                self.t_upt,
                self.t_evo,
                self.t_hff,
                self.t_pfv
            ])

            self.c.children.extend([
                self.c_moc
            ])

            self.e.children.extend([
                self.e_uec,
                self.e_reu,
                self.e_spt
            ])
            return True
        except:
            return False 
        return True 
        
