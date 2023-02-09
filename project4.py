import random

actual_rolled = random.randint(1,6)
num_of_roles = 1
num_of_trials = 0


while num_of_trials < 1000:
    while actual_rolled != 6:
        actual_rolled = random.randint(1,6)
        num_of_roles = num_of_roles +1 


    if actual_rolled == 6:
        num_of_roles = num_of_roles +0
    num_of_trials = num_of_trials + 1
    actual_rolled = random.randint(1,6)   
    num_of_roles = num_of_roles +1  
print (num_of_roles/num_of_trials)
    

    