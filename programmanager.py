from worker import Worker
from product import Product, Foodstuff, VariableProduct

class ProgramManager():
    """Creates the program manager. 
    \nOnly one should exist, it holds everything, and runs the day cycle going through all phases.
    """

    def __init__(self,pop_size:int):
        """_summary_

        Args:
            pop_size (int): _description_
        """

        # Generate Workers
        self.worker_list:list[Worker] = []
        for i in range(pop_size):
            self.worker_list.append(Worker())

        # Create marketplace
        self.marketplace:set[Product] = {Foodstuff(),Product()}
        # Market place is a set that should be managed only by external commands. Consider making it its own class for the sake of objectification.
        # getMarket() - Returns market to workers to browse.
        # accessInMarket(specific product) - Accesses from the market.
    
    def getMarket(self)->set[Product]:
        return self.marketplace

    def doDay(self):
        self.workPhase()
        self.upkeepPhase()
        self.distributionPhase()
        self.considerationPhase()

    def workPhase(self):
        pass

    def upkeepPhase(self):
        pass

    def distributionPhase(self):
        """ Take all products from stores, give workers a chance to buy from market."""

        # Workers are given the market in their checkMarket phase and will consider items and then buy and remove them from market themselves.
        for worker in self.worker_list:
            worker.checkMarket(self.marketplace)

    def considerationPhase(self):
        pass

if __name__ == "__main__":
    PM = ProgramManager(10)
    for worker in PM.worker_list:
        print(worker.name+" "+str(worker.performance))
    PM.doDay()