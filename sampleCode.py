'''
Sample Code to find out the uniqueness between two features using Spearman's Correlation Coefficient
This code just takes hctsa_datamatrix as input, and finds the uniqueness of the method number 1 given in datamatrix as compared to other methods
To run this file, One needs to import pandas,scipy and numpy modules

This file gives a runtime Error, because sometimes, the variance is zero for some features. But, It calculates the correlation for other values
'''

from scipy import stats
import pandas as pd

if __name__ == "__main__":
	featureVector = pd.read_csv("hctsa_datamatrix.csv",)
	columnList = list(featureVector.columns)	# For now, I have assumed that the values of the first column are unique 
	rankedArray = list()
	
	for i in range(1,len(columnList)):
		try:
			spearmanValue = stats.spearmanr(featureVector[columnList[0]],featureVector[columnList[i]])[0]
		except:
			print("Nan provided, not calculating correlation with this feature number", i+1)
			continue
		rankedArray.append([i+1,spearmanValue])
	
	rankedArray = sorted(rankedArray,key = lambda x:x[1],reverse = True) #In spearman's correlation, 1 means both functions behave in the same way (i.e both increase/decrease), 0 means no correlation between the two, -1 means the functions behave in opposite ways. Hence, in this case, I have sorted the array in decreasing order of their correlation coefficient 
	for elements in range(len(rankedArray)):
		print("Rank number:",element+1,"feature number:",*rankedArray[element])
	