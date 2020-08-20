import math

def numRoutes(dim):
    steps = dim * 2
    routes = math.floor(math.factorial(steps) / math.factorial(steps/2)**2)
    print(routes)

numRoutes(20)