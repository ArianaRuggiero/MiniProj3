import math
#from scipy import sem, t

#1 Population Mean
def populationMean(dataSet): 
    data = [float(s) for s in dataSet.split(',')]

    mean = sum(data) / len(data)
    
    return mean

#2 Median
def median(dataSet):
    data = [int(s) for s in dataSet.split(',')]

    listLength = len(data)
    sortedList = sorted(data)
    index = (listLength - 1) // 2
    if (listLength % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.0


#3 Mode 
def mode(dataSet):
    data = [int(s) for s in dataSet.split(',')]
    n = len(data)
    getMode = {}

    for l in data:
        getMode[l] = getMode.get(l,0) + 1

    maxValue = max(list(getMode.values()))
    modeValue = [a for a, v in getMode.items() if v == maxValue]

    if len(modeValue) == n:
        return 0
    else:
        return modeValue[0]

# print(str(mode(dataSet)))

#4 Population Standard Deviation
def populationStandardDeviation(dataSet):
    # CSVlues are supposed to be the values that are given
    u = 0
    #This is the Mean
    Top = 0
    # This is the top half of the equation
    Set = 0
    # This the bottom half of the equation
    Ans = 0
    # This is the Answer
    u = sum(dataSet)/len(dataSet)

    for i in dataSet:
        Top +=(i-u)**2

    Set = Top/len(dataSet)

    Ans = math.sqrt(Set)

    return Ans

#5 Variance of population proportion
def variancePopulationProportion(dataSet):
    data = [int(s) for s in dataSet.split(',')]

    mean = sum(data) / len(data)
    populationProportion = 1 / len(data)
    print('populationProportion: ', populationProportion)
    if populationProportion != 0:
        varianceOfPopulation = sum((xi - mean) ** 2 for xi in data) / populationProportion
    else:
        varianceOfPopulation = 0            

    return varianceOfPopulation

# print('Variance of Population Proportion: ', str(variancePopulationProportion(dataSet)))

#6 Z-Score
def zScore(dataSet):
    data = [int(s) for s in dataSet.split(',')]
    mean = sum(data) / len(data)
    std = math.sqrt(sum([(val - mean)**2 for val in data])/(len(data) - 1))
    scores = []
    for num in data:
        # calculates the z-score of each number in the dataset
        zScore = (num - mean)/std
        scores.append(zScore)
    return scores

# zScore(dataSet)
#7 Standardized Score
def standardizedScore(dataSet):
    data = [int(s) for s in dataSet.split(',')]

    mean = sum(data) / len(data)
    std = math.sqrt(sum((val - mean) ** 2 for val in data))/(len(data))

    scores = []

    for num in data:
        standardizedScore = (num - mean)/std
        scores.append(standardizedScore)
    return scores

#    print("Standardized Scores of dataset:", standardizedScore(dataSet)) 

#8 Population Correlation Coefficient 
def populationCorrelationCoefficient(dataSet):
    data = [int(s) for s in dataSet.split(',')]

    # data.pop()

    halfOfLength = int((len(data)) / 2)
    endOfList = int(len(data))
    dataX = data[halfOfLength:endOfList]
    print('dataX: ', dataX)

    print('len(data): ', len(data))

    dataY = data[0:halfOfLength]
    print('dataY: ', dataY)

    Ex = sum(dataX)
    Ey = sum(dataY)
    Exy = 0
    Ex2 = 0
    Ey2 = 0
    n = len(dataX)

    if n != len(dataY):
        cake ='The two data sets that you have entered do not have the same number of numbers.'
        return 0
    else:
        for i in range(len(dataX)):
            Exy += dataX[i]* dataY[i]
            Ex2 += dataX[i] ** 2
            Ey2 += dataY[i] ** 2

        Top = 0
        Top = (n*Exy) - (Ex*Ey)
        Bottom = 0
        Bottom = math.sqrt((n*Ex2-Ex**2)* (n*Ey2-Ey**2))
        ans = Top/Bottom
        return ans

#9 Confidence Interval
def confidenceInterval(dataSet):
    confidence = .95
    n = len(dataSet)
    m = sum(dataSet) / n
    std = math.sqrt(sum([(val - m)**2 for val in dataSet])/(len(dataSet) - 1))
    std_err = std / math.sqrt(n)
    t = m / std_err
    h = std_err * t * float(1 + confidence) / float(2., n - 1)

    start = m + h
    end = m - h

    return start, end

# print ("Confidence Interval:", confidenceInterval(dataSet))

#10 Population Variance
def variance(dataSet):
    data = [int(s) for s in dataSet.split(',')]
    mean = sum(data) / len(data)

    variance = sum((xi - mean) ** 2 for xi in data) / len(data)
    return variance

# print('Population Variance: ', str(variance(dataSet)))

#11 P Value
def pValue(dataSet):
    set1 = dataSet[0:9]
    set2 = dataSet[9:18]

    mean_1 = sum(set1)/len(set1)
    mean_2 = sum(set2)/len(set2)

    n1 = len(set1) - 1
    std_err_1 = (math.sqrt(sum([(val - mean_1) ** 2 for val in set1]))/(n1)) / math.sqrt(len(set1))

    n2 = len(set2) - 1
    std_err_2 = (math.sqrt(sum([(val - mean_2) ** 2 for val in set2]))/(n2)) / math.sqrt(len(set2))

    std_err_diff = math.sqrt(std_err_1 ** 2 + std_err_2 ** 2)

    t_statistic = (mean_1 - mean_2) / (std_err_diff)

    deg_of_freedom = len(set1) + len(set2) - 2

    alpha = 0.05

    critical_value = t.ppf(1.0 - alpha, deg_of_freedom)

    pValue = (1 - t.cdf(abs(t_statistic), deg_of_freedom)) * 2

    if pValue > alpha:
        return("p-value is less than alpha. Null hypothesis accepted: means are equal.")
    else:
        return("p-value is greater than alpha. Null hypothesis rejected: means are not equal.")

#12 Proportion
def proportion(dataSet):
    try:
        ans = []
        total = sum(dataSet)

        for i in dataSet:
            temp = i/total
            ans.append('{:.4f}'.format(temp))
        return ans

    except:
        return "Pay attention, also I can not divide by zero :("

#13 Sample Mean
def sampleMean(dataSet):   
    shortendDataSet = dataSet[0:5]
    smean = sum(dataSet) / len(dataSet)

    return smean
# print ("Sample Mean:", sampleMean(dataSet))

#14 Sample Standard Deviation
def standardDeviation(dataSet):
    mean = sum(dataSet) / len(dataSet)
    std = math.sqrt(sum([(val - mean)**2 for val in dataSet])/(len(dataSet) - 1))

    return std
#15 Variance of sample proportion
def varianceSampleProportion(dataSet):
    mean = sum(dataSet) / len(dataSet)
    varianceSampleProportion = sum((xi - mean) ** 2 for xi in dataSet) / (len(dataSet) - 1)

    return varianceSampleProportion

    print("Variance of Sample Proportion is:", varianceSampleProportion)


