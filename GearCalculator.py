gearRatios = [8, 12, 14, 16, 20, 24, 28, 36, 40, 56, 60]
gearRatioAllCalcs = [] # raw gear ratio in decimal form
gearRatioAllList = [] # gear ratio pairs in string form



# populate lists of all possible gear ratios with corresponding gear pairs
for i in gearRatios:
    for j in gearRatios:
        gearRatioAllCalcs.append(i / j)
        gearRatioAllList.append(str(i) + "-" + str(j))

# collect gear ratio to search for
getRatio = input("Input gear ratio in decimal.  Remember leading 0: ")
gearRatio = float(getRatio)

# search calcs for gear ratio and print gear pair
gearPairIndex = gearRatioAllCalcs.index(gearRatio)

try: 
    print("The gear pair you could use are: " + gearRatioAllList[gearPairIndex])
except ValueError:
    print("Not possible with these gears")   


# to do; X: = completed
# --------
# X: populate 2 lists of all possible pairs; one as decimals, the otheras text pairs
# X: ask for gear ratio to search for and return the corresponing gear pair
# X: handle for values not in the list
# deal with multiple gear pairs for same gear ratio
#  


# tests; can be commented out as passed
# ---------
# print(gearRatioAllCalcs) # long list of comma-seperated decimals
# print(gearRatioAllList) # long list of comma-seperated string pairs in format '1-1'
# print(str(len(gearRatioAllCalcs)) + "-" + str(len(gearRatioAllList))) # list lengths should be =
# print(gearRatio) # should be whatever number entered; no quotation marks0.09
# print(type(gearRatio)) # should be <class 'float'>
# print(gearPairIndex) # should return position in list of gearRatio
# print(gearRatioAllList[gearPairIndex]) # should return gear ratio pair