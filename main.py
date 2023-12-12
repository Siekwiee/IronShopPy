ScrewVal: int = 7
nutVal: int = 4
WasherVal: int = 2

ScrewCount: int = input(f"How many screws do you want to buy? One costs: {ScrewVal} | ")
NutCount: int = input(f"How many nuts do you want to buy? One costs: {nutVal} | ")
WasherCount: int = input(f"How many washers do you want to buy? One costs: {WasherVal} | ")

def hornbach():
    ScrewPrice = int(ScrewCount) * ScrewVal
    NutPrice = int(NutCount) * nutVal
    WasherPrice = int(WasherCount) * WasherVal
    AllCostCt: int = ScrewPrice + NutPrice + WasherPrice
    FinalPrice: int = int(AllCostCt) / int(100)
    print(f"The final price is: {FinalPrice}")
    return

hornbach()

