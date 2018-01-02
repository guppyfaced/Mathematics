import random

#initial values
safe_gain_losses = 1000
safe_losses_risky_gains = 1000
risky_losses_safe_gains = 1000
risky_gain_losses = 1000

#plays it safe
for i in range(1, 101):
    safe_gain_losses += 500
    safe_gain_losses -= 500
#Takes the risk on the gains
for i in range(1, 101):
    safe_losses_risky_gains -= 500
    #Coin toss choice - same in all the other bits
    j = random.choice([1,0])
    if j == 1:
        safe_losses_risky_gains += 1000
#Takes the risk on the losses
for i in range(1, 101):
    risky_losses_safe_gains += 500
    j = random.choice([1,0])
    if j == 1:
        risky_losses_safe_gains -= 1000

#risk taker
for i in range(1, 101):
    j = random.choice([1,0])
    if j == 1:
        risky_gain_losses += 1000
    k = random.choice([1,0])
    if k == 1:
        risky_gain_losses -= 1000


print(f"Safe gains and losses over 100 runs resulted in: ${safe_gain_losses}")
print(f"Risky gains and safe losses over 100 runs resulted in: ${safe_losses_risky_gains}")
print(f"Safe gains and risky losses over 100 runs resulted in: ${risky_losses_safe_gains}")
print(f"Risky gains and losses over 100 runs resulted in: ${risky_gain_losses}")