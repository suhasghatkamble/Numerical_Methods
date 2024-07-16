import numpy as np
import matplotlib.pyplot as plt
import copy


org_deck = ['1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S',
            '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
            '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D']

def kingking(deck):
    for i in range(len(deck) - 1):
        if deck[i][0] == 'K' and deck[i+1][0]=='K':  #check if there is King-King combination 
            return True
        
def MonteCarlo(n):
    count = 0.0
    for i in range(n):
        deck=copy.deepcopy(org_deck)
        np.random.shuffle(deck)            # Shuffle a deck
        if kingking(deck):                  # Check if there is King-King combination
            count=count + 1                 # if found then increase a count
        print(count/n*100)                  # Get a success %%
        return count/n*10
# Simulate 
result = []
for i in range(1,7):
    result.append(MonteCarlo(10**i))
    
# Actual probability value = 21.7376%
plt.xscale('log')
plt.plot([10**i for i in range(1, 7)], result)
plt.scatter([10**i for i range(1, 7)], result)