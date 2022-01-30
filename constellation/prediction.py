from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import csv
import pandas as pd
#from constellation.creation import constdict
import constellation.methods as methods
import constellation.creation as creation
import glob
from sklearn.ensemble import RandomForestClassifier

#data = pd.read_csv("data1.csv", index_col=False)
#predictors = data.drop(["outcomes"], axis=1)
#northdata = data[data["north"]==True]
#southdata = data[data["south"]==True]
#northpredictors = northdata.drop(["outcomes"], axis=1)
#southpredictors = southdata.drop(["outcomes"], axis=1)
#outcomes = data["outcomes"]
#Noutcomes = northdata["outcomes"]
#Soutcomes = southdata["outcomes"]
#knn = KNeighborsClassifier(n_neighbors = 1)
#knnN = KNeighborsClassifier(n_neighbors = 1)
#knnS = KNeighborsClassifier(n_neighbors = 1)
#standardpredictors = preprocessing.scale(predictors)
#knn.fit(predictors, outcomes)
#knnN.fit(northpredictors, Noutcomes)
#knnS.fit(southpredictors, Soutcomes)



#sk_predictions = knn.predict(predictors)
#print(sk_predictions)
#print(accuracy_score(sk_predictions, outcomes))

#testdata = []
#testnorth = []
#testsouth = []
#test = methods.get_normed_predictors("c:/Users/Mishal/Desktop/testing.png",0)
#testpngs = glob.glob("c:/Users/Mishal/Desktop/testpics/*.png")
# for png in testpngs:
#     testdata.append(methods.get_normed_predictors(png))
#     testnorth.append(methods.checknorth[png.split("\\")[-1].split("test.png")[0]])
#     testsouth.append(methods.checksouth[png.split("\\")[-1].split("test.png")[0]])
#         #print(basics2.get_normed_predictors("c:/Users/Mishal/Desktop/testing.png", rotation))


# test2 = methods.get_normed_predictors("c:/Users/Mishal/Desktop/constellations/ursa_major.png")
# test2.append(1)
# test2.append(0)
# test2 = [test2]
# #testing = [test]
# df2 = pd.DataFrame(test2)
# df2 = df2.T
def runthis(url, hemisphere):
    #url = "C://Users//Mishal//Desktop//testpics//andromedatest.png"
    #hemisphere = "north"

    testdata = methods.get_normed_predictors(url)
    testdata = [testdata]
    testnorth = hemisphere == "north"
    testsouth = hemisphere == "south"
    testnorth = [testnorth]
    testsouth = [testsouth]
    df = pd.DataFrame(testdata)
    df["north"] = [testnorth]
    df["south"] = [testsouth]
    #df.columns = creation.columns
    df = pd.DataFrame(testdata)
    df["north"] = testnorth
    df["south"] = testsouth
    df.columns = creation.columns
    #print(df["north"]==True)

    data = pd.read_csv("constellation//content//data.csv", index_col=False)
    predictors = data.drop(["outcomes"], axis=1)
    
    outcomes = data["outcomes"]
    print(predictors)
    print(outcomes)
    if hemisphere == 'north':
        predictors = predictors[data['north']==True]
        outcomes = outcomes[data['north']==True]
    elif hemisphere == 'south':
        predictors = predictors[data['south']==True]
        outcomes = outcomes[data['south']==True]
    print(predictors)
    print(outcomes)

    #knn = KNeighborsClassifier(n_neighbors = 1)
    #knn.fit(predictors, outcomes)

    clf = RandomForestClassifier(max_depth=4, random_state=0, n_estimators=30)
    clf.fit(predictors, outcomes)
    probab2 = list(clf.predict_proba(df)[0])
    probab = list(clf.predict_proba(df)[0])
    print(probab)
    probab.sort(reverse=True)
    pred1 = clf.predict(df)[0]
    pred2 = list(outcomes)[list(probab2).index(probab[1])]
    pred3 = list(outcomes)[list(probab2).index(probab[2])]
    pred4 = list(outcomes)[list(probab2).index(probab[3])]
    if pred2 == pred1: 
        pred2 = list(outcomes)[list(probab2).index(probab[1])+1]
    constdict = creation.getconstdict()
    print(probab)
    print([pred1, pred2, pred3, pred4])
    return [constdict[pred1],constdict[pred2], constdict[pred3], constdict[pred4]]


# clf = RandomForestClassifier(max_depth=4, random_state=0, n_estimators=30)
# clf.fit(predictors, outcomes)
# print(clf.predict(df))
# print(accuracy_score(clf.predict(df), range(1,11)))
# secondmost = []
# thirdmost = []
# for i in range(len(knn.predict(df))):
#     listofelem = list(clf.predict_proba(df)[i])
#     listofelem.sort(reverse=True)
#     element = listofelem[1]
#     third = listofelem[2]
#     #print(element)
#     secondmost.append(list(clf.predict_proba(df)[i]).index(element))
#     thirdmost.append(list(clf.predict_proba(df)[i]).index(third))
# print(secondmost)
# print(accuracy_score(secondmost, range(1,11)))
# print(thirdmost)
# print(accuracy_score(thirdmost, range(1,11)))


# n = 0
# for i in range(len(secondmost)):
#     if knn.predict(df)[i] == outcomes[i] or clf.predict(df)[i] == outcomes[i] or secondmost[i] == outcomes[i] or thirdmost[i] == outcomes[i]:
#         n = n + 1/len(secondmost)
# print(n)
