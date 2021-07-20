import pandas as pd 


#Importing the dataset  
dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Unsupervised\\Clustering\\Market_Basket_Optimisation.csv')
# print(dataset.head())
# print(dataset.shape)


transactions=[]  
for i in range(len(dataset)):  
    transactions.append([str(dataset.values[i,j])  for j in range(0,20)])  


# pip install apyori
from apyori import apriori  
rules= apriori(transactions= transactions, min_support=0.003, min_confidence = 0.2, min_lift=3, min_length=2, max_length=2)  


result= list(rules)  
print(result)


# Visualizing the rule, support, confidence, lift in more clear way:
for item in result:  
    pair = item[0]   
    items = [x for x in pair]  
    print("Rule: " + items[0] + " -> " + items[1])  
  
    print("Support: " + str(item[1]))  
    print("Confidence: " + str(item[2][0][2]))  
    print("Lift: " + str(item[2][0][3]))  
    print("=====================================") 
