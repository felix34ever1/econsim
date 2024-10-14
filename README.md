# econsim
Simulation of economics under capitalist system. Python.


## System Explanation
The simulation works on quantum of time known in program as a 'day'.
Each quanta consists of several phases:
1. Work Phase - Workplaces calculate products and pay workers.
2. Upkeep Phase - Workers suffer from hunger etc.
3. Distribution Phase - Workers attempt to acquire what is necessary for survival.
4. Consideration Phase - Workplaces consider their wages and prices and workers consider the viability of starting their own workplaces or leaving for elsewhere.

## Worker
Each worker represents one individual in the economy. Workers have several statistics, some representing their performace, and others representing their needs.
A worker usually gets paid from a workplace an agreed amount when they join. They may instead become capitalists by starting their own workplace.

## Workplace
A workplace is a system that allows workers to add their labour (sometimes to resources) and produce value by producing a product. Be this raw or manufactured.
Workplaces have a sell price for their product and negotiate a wage price with their workers when hiring them.

## Decision Making
Workers and workplaces can make decisions to decide their futures, this is based on an algorithm. Each possible decision is ranked by an algorithm for deciding its weight.
For example in the production phase, a worker may decide what to buy, with three options: Food, Water, Nothing. Each attached option will have an algorithm attached to it. For example
Food will consider: Worker Hunger - Cost, water may consider Worker Thirst - Cost and Nothing will simply have a neutral value. If a worker was hungry they would attempt to buy the food, when Nothing is chosen, the process stops.

## Adaptive Decisions
Each generation of workers and capitalists (who will start with a workplace) will be able to change their natural weights of opinion. 
Take the food equation earlier, it may now ne re-written as Worker Hunger * W0 - Cost*W1 where W0 and W1 are weights with a value increased or decreased at random between sets.
At the moment there is no decided marker for success other than survival, but factors of success may be chosen, for example wealth at the end may decree which workers pass onto
the next generation.