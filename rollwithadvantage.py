import random

dicesize            = 20
number_of_scenarios = 300000     # number of scenarios to run
dict_stored_results = {}        # location of stored results

# Run a single scenario
def fRunSingleScenario():
    dice1 = random.randrange(1,dicesize+1)
    dice2 = random.randrange(1,dicesize+1)
    return max(dice1, dice2)


# add to dictionary, or increase dictionary count by one
def fAddToDictionary(accepted_key):
    if accepted_key in dict_stored_results:
        dict_stored_results[accepted_key] += 1
    else:
        dict_stored_results[accepted_key] = 1

#------------------------------------------------------
#----------------Code Starts Here----------------------
#------------------------------------------------------
for one_scenario in range(number_of_scenarios):
    limit = fRunSingleScenario()
    fAddToDictionary(str(limit).zfill(2))

# Re-order the dictionary keys alphabetically
dict_stored_results = dict( sorted(dict_stored_results.items(), key=lambda x: x) )


# Display how many each combination got, as well as a percentage against total scenarios
print("After {:,} scenarios:".format(number_of_scenarios))
for each_key, each_value in dict_stored_results.items():
    print(" {key:} {val:>8,} {pct:>9.3%} "
        .format(key = each_key,
                val = each_value,
                pct = each_value/number_of_scenarios
            )
    )
