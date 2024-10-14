import random

## Worker Class

class Worker():
    """-Worker Class-
    \nA Worker, with randomised stats.
    """

    def __init__(self):
        """_summary_
        Generates worker with random name from name list and random performance characteristic
        """
        # ID
        with open("fnames.txt","r") as f:
            names = f.readlines()
            self.name = names[random.randint(0,len(names)-1)].removesuffix("\n")

        # Needs
        self.hunger = 0
        self.money = 0

        # Performance
        self.performance = round(random.random(),2)
        self.salary = 0

        # Employment status
        self.employed_at:object = None

    def considerEmployment(self):
        pass

    def checkMarket(self,market:set):
        """Looks at all market items, calculates attractiveness, and picks items to buy, until choosing the one stopViewingMarket item after which the worker stops.

        Args:
            market (set): The marketplace with all items on it
        """

        import product
        market:set[product.Product] = market
        if len(market) == 0:
            return None
        
        market.add(product.StopViewingMarket())
        most_attractive_product:product.Product = None
        while not isinstance(most_attractive_product,product.StopViewingMarket):
            # Searches through all products, comparing to the current most attractive and updating.
            most_attractive_product = None
            most_attractive_attraction = -1
            for _product in market:
                attraction = _product.decideAttraction(self)
                if most_attractive_product == None:
                    most_attractive_product = _product
                    most_attractive_attraction = attraction
                else:
                    if attraction > most_attractive_attraction:
                        most_attractive_product = _product
                        most_attractive_attraction = attraction
                    
            # Purchase the product and go again. This removes the product from the list.
            market.remove(most_attractive_product)
            most_attractive_product.acquireProduct(self)
            print(f"{self.name}: {most_attractive_product}")


if __name__ == "__main__":
    w = Worker()

    print(w.name+str(w.performance))