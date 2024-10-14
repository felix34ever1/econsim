from worker import Worker

class Product():
    """Product Class. Used to represent different consumer goods and foodstuffs produced by workplaces.
    """

    def __init__(self):
        self.cost = 1
        self.workplace = None

    def decideAttraction(self,worker:Worker)->int:
        """_summary_ Returns the attraction for the worker to decide this option.

        Args:
            worker (Worker): The worker that is considering this product.

        Returns:
            int: The attraction value, passed to a dictionary containing the item.
        """
        value = 0
        value -= self.cost
        if worker.money>=self.cost:
            return value
        else:
            return -99

    def acquireProduct(self,worker:Worker)->None:
        """_summary_ Method to be used for when a worker wants to buy the item. Price of the item is verified beforehand and product will be removed from market by worker.
        \n This method just modifies on the worker what would change from buying it and gives the workplace that produced it the worker's money.

        Args:
            worker (Worker): The worker that is buying this product.

        Returns:
            None: No Returns
        """
        import workplace

        worker.money-=self.cost
        if isinstance(self.workplace,workplace.Workplace):
            pass
            

class Foodstuff(Product):

    def __init__(self):
        super().__init__()
        self.cost = 1
    
    def decideAttraction(self, worker):
        value = worker.hunger - self.cost
        if worker.money>=self.cost:
            return value
        else:
            return -99

    def acquireProduct(self, worker):
        super().acquireProduct(worker)
        worker.hunger-=10
        if worker.hunger<0:
            worker.hunger = 0

class VariableProduct(Product):

    def __init__(self,variable:int):
        super().__init__()
        self.variable:int = variable
        self.cost = variable

    def decideAttraction(self, worker):

        if worker.money>=self.cost:
            return self.variable
        else:
            return -99

class StopViewingMarket(Product):
    """StopViewingMarket Class, should be identified by workers as the way to stop attempting to buy from the market.

    Args:
        Product (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.cost = 0

    def decideAttraction(self, worker):
        return 0