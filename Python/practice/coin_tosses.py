import random

coins = {
  'head': 0,
  'tail': 0
}

def coin_tosses():
  print "Starting the program..."
  for i in range(1, 5001):
    if round(random.random()) > 0:
      coin = 'head'
    else:
      coin = 'tail'
    coins[coin] += 1
    print "Attempt #" + str(i) + ": Throwing a coin... It's a " + coin + "! ... Got " + str(coins['head'])  + " head(s) so far and " + str(coins['tail']) + " tail(s) so far"
  print "Ending the program, thank you!" 

coin_tosses()