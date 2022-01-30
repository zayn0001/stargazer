import csv
import pandas as pd
import glob   
import constellation.methods as methods
import math

const_pngs = glob.glob("c:/Users/Mishal/Desktop/constellations/*.png")




predictors = []
outcomes = []
north = []
south = []
i = 1
#constdicts = {}
for png in const_pngs:
    #for rotation in range(0, 460, 20):    
    #constdicts[i] = png.split("\\")[-1].split(".png")[0]
    predictors.append(methods.get_normed_predictors(png))
    outcomes.append(i)
    north.append(methods.checknorth[png.split("\\")[-1].split(".png")[0]])
    south.append(methods.checksouth[png.split("\\")[-1].split(".png")[0]])
    i = i+1

def getconstdict():
    constdicts = {}
    i=1
    for png in const_pngs:
    #for rotation in range(0, 460, 20):    
        constdicts[i] = png.split("\\")[-1].split(".png")[0]
        i = i+1
    return constdicts


noofpredictors = math.factorial(methods.NO_OF_POINTS)/(math.factorial(methods.NO_OF_POINTS-2)*2)
noofpredictors = int(noofpredictors)
with open("constellation//content//mlforconsts.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["predictor"]*noofpredictors)
    csvwriter.writerows(predictors)

data = pd.read_csv("constellation//content//mlforconsts.csv")
data["north"] = north
data["south"] = south
data["outcomes"] = outcomes


data.to_csv('constellation//content//data.csv', index=False)

columns = data.drop(["outcomes"], axis=1).columns
#data["outcomes"] = [1]*len()
