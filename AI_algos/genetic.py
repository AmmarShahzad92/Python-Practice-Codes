import random 
import string 
 
class GA: 
    def __init__(self, target, populationSize): 
        self.target = target 
        self.length = len(target) 
        self.populationSize = populationSize 
        self.population = {} 
        self.totalFitness = 0 

        for i in range(populationSize): 
            individual = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.length)) 
            fitness = self.calculateFitness(individual) 
            self.population[i] = [individual, fitness] 
            self.totalFitness += fitness 

    def calculateFitness(self, individual): 
        return sum(1 for i in range(self.length) if individual[i] == self.target[i]) 
 
    def updatePopulationFitness(self): 
        self.totalFitness = 0 
        for i in self.population: 
            fitness = self.calculateFitness(self.population[i][0]) 
            self.population[i][1] = fitness 
            self.totalFitness += fitness 
 
    def selectParents(self): 
        rouletteWheel = [] 
        for i in self.population: 
            rouletteWheel += [i] * (self.population[i][1] + 1) 
 
        newPopulation = {} 
        for i in range(self.populationSize): 
            selected = random.choice(rouletteWheel) 
            newPopulation[i] = self.population[selected].copy() 
 
        self.population = newPopulation 
        self.updatePopulationFitness() 
 
    def crossover(self, crossoverProbability): 
        for i in range(0, self.populationSize - 1, 2): 
            if random.random() < crossoverProbability: 
                point = random.randint(1, self.length - 1) 
                p1, p2 = self.population[i][0], self.population[i + 1][0] 
                c1 = p1[:point] + p2[point:] 
                c2 = p2[:point] + p1[point:] 
                self.population[i][0] = c1 
                self.population[i + 1][0] = c2 
        self.updatePopulationFitness() 
 
    def mutate(self, mutationProbability): 
        for i in self.population: 
            individual = list(self.population[i][0]) 
            for j in range(self.length): 
                if random.random() < mutationProbability: 
                    individual[j] = random.choice(string.ascii_lowercase) 
            self.population[i][0] = ''.join(individual) 
        self.updatePopulationFitness() 
 
# ===== MAIN PROGRAM ===== 
 
target = input("Enter target string: ").lower() 
populationSize = 100 
ga = GA(target, populationSize) 
 
generation = 0 
while generation < 100: 
    ga.selectParents() 
    ga.crossover(0.7) 
    ga.mutate(0.01) 
 
    best = max(ga.population.values(), key=lambda x: x[1]) 
 
    print(f"Generation {generation} | Best: {best[0]} | Fitness: {best[1]}") 
 
    if best[1] == len(target): 
        print("Target string matched!") 
        break 
 
    generation += 1















# code 2
import random 
import math 
 
class GA: 
    def __init__(self, individualSize, populationSize): 
        self.population = dict() 
        self.individualSize = individualSize 
        self.populationSize = populationSize 
        self.totalFitness = 0 
        i = 0 
        while i < populationSize: 
            listOfBits = [0] * individualSize 
            listOfLocations = list(range(0, individualSize)) 
            numberOfOnes = random.randint(0, individualSize - 1) 
            onesLocations = random.sample(listOfLocations, numberOfOnes) 
            for j in onesLocations: 
                listOfBits[j] = 1 
            self.population[i] = [listOfBits, numberOfOnes] 
            self.totalFitness += numberOfOnes 
            i += 1 
 
    def updatePopulationFitness(self): 
        self.totalFitness = 0 
        for individual in self.population: 
            individualFitness = sum(self.population[individual][0]) 
            self.population[individual][1] = individualFitness 
            self.totalFitness += individualFitness 
 
    def selectParents(self): 
        rouletteWheel = [] 
        wheelSize = self.populationSize * 5 
        h_n = [] 
        for individual in self.population: 
            h_n.append(self.population[individual][1]) 
        j = 0 
        for individual in self.population: 
            individualLength = round(wheelSize * (h_n[j] / sum(h_n))) 
            j += 1 
            if individualLength > 0: 
                i = 0 
                while i < individualLength: 
                    rouletteWheel.append(individual) 
                    i += 1 
        random.shuffle(rouletteWheel) 
        parentIndices = [] 
        i = 0 
        while i < self.populationSize: 
            parentIndices.append(rouletteWheel[random.randint(0, len(rouletteWheel) - 1)]) 
            i += 1 
        newGeneration = dict() 
        i = 0 
        while i < self.populationSize: 
            newGeneration[i] = self.population[parentIndices[i]].copy() 
            i += 1 
        del self.population 
        self.population = newGeneration.copy() 
        self.updatePopulationFitness() 
 
    def generateChildren(self, crossoverProbability): 
        numberOfPairs = round(crossoverProbability * self.populationSize / 2) 
        individualIndices = list(range(0, self.populationSize)) 
        random.shuffle(individualIndices) 
        i = 0 
        j = 0 
        while i < numberOfPairs: 
            crossoverPoint = random.randint(0, self.individualSize - 1) 
            child1 = self.population[j][0][:crossoverPoint] + self.population[j + 
1][0][crossoverPoint:] 
            child2 = self.population[j + 1][0][:crossoverPoint] + self.population[j][0][crossoverPoint:] 
            self.population[j] = [child1, sum(child1)] 
            self.population[j + 1] = [child2, sum(child2)] 
            i += 1 
            j += 2  
        self.updatePopulationFitness() 
 
    def mutateChildren(self, mutationProbability): 
        numberOfBits = round(mutationProbability * self.populationSize * self.individualSize) 
        totalIndices = list(range(0, self.populationSize * self.individualSize)) 
        random.shuffle(totalIndices) 
        swapLocations = random.sample(totalIndices, numberOfBits) 
        for loc in swapLocations: 
            individualIndex = math.floor(loc / self.individualSize) 
            bitIndex = loc % self.individualSize 
            if self.population[individualIndex][0][bitIndex] == 0: 
                self.population[individualIndex][0][bitIndex] = 1 
            else: 
                self.population[individualIndex][0][bitIndex] = 0 
        self.updatePopulationFitness() 
 
# Initialize parameters 
individualSize, populationSize = 8, 10 
instance = GA(individualSize, populationSize) 
 
# Genetic Algorithm main loop 
i = 0 
while True: 
    instance.selectParents() 
    instance.generateChildren(0.8) 
    instance.mutateChildren(0.03) 
 
    # Print current population and fitness 
    print("Population:", instance.population) 
    print("Total Fitness:", instance.totalFitness) 
    print("Generation:", i) 
 
    # Check if any individual has reached the maximum fitness (all ones) 
    found = False 
    for individual in instance.population: 
        if instance.population[individual][1] == individualSize: 
            found = True 
            break 
    if found: 
        break 
    i += 1 