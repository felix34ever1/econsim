import worker
import product

class Workplace():
    '''Workplace class, hosts workers and pays them. Uses them to produce product. Ran by one capitalist who funds the workplace.'''

    def __init__(self,owner:worker,productconstructor:product.Product):
        """Creates the workplace

        Args:
            owner (worker): The worker who is creating this workplace. Must be unemployed to create.
            productconstructor (function): The type of product that is gonna be made. This is the contructor method for that product.
        """
        self.owner:worker.Worker = owner
        self.productconstructor:function = productconstructor

        self.workers:list[worker.Worker] = [] # Stores all workers inside
        self.storehouse:set[product.Product] = set()
        
        self.weights:list[float] = [0.0,1.0,0.0]

    def decideAttraction(self, worker:worker.Worker)->int:
        """The business takes into consideration if it wants to hire the worker and outputs the salary they are willing to pay

        Args:
            worker (worker.Worker): The worker considering to join the workforce.

        Returns:
            int: The salary that the company is willing to pay.
        """

        givensalary = self.owner.money*self.weights[0]+self.weights[1]+worker.performance*self.weights[2]
        if givensalary<0:
            givensalary = 0
        return int(givensalary)
        

    def produce(self):
        """Creates an amount of products in the storehouse based on employees performance and pays each employee.
        """
        productivity = 0.0

        # For each worker, calculate performance and pay workers.
        for worker in self.workers:
            productivity+=worker.performance

            # Pay Worker if can afford
            if self.owner.money-worker.salary>=0:
                self.owner.money-=worker.salary
                worker.money+=worker.salary
            # Otherwise worker should get really unhappy

        for i in range(int(productivity)):
            new_product:product.Product = self.productconstructor()
            new_product.workplace = self
            self.storehouse.add(self.productconstructor())


if __name__ == "__main__":
    # Create a workplace, generating a worker first for its owner, it is a foodstuff producer
    w1 = worker.Worker()
    w1.money += 50
    wp1 = Workplace(w1,product.Foodstuff)
    print(wp1.owner.name+str(wp1.productconstructor()))
    
    # Give the factory some workers and set their salary to 1
    for i in range(5):
        wx = worker.Worker()
        wx.salary = 1
        wp1.workers.append(wx)

    
    wp1.produce()
    print(str(wp1.storehouse))
    print(w1.money)