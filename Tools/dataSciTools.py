from langchain.tools import tool
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

@tool
def clean_dataset(file_path:str):
    """
    Clean datasets and takes the filepath of csv file as an arguemnet
    Arguement:
        file_path: Path to csv file
    """
    dataFrame = pd.read_csv(file_path)
    dataFrame = dataFrame.dropna()
    #selecting catagorical columns
    catogorical_data = dataFrame.select_dtypes(exclude=['number']).columns

    le = LabelEncoder()

    #endoding catagorical data
    for col in catogorical_data:
        dataFrame[col] = le.fit_transform(dataFrame[col])
    
    os.makedirs("CleanedCSV",exist_ok=True)
    dataFrame.to_csv("CleanedCSV/cleaned.csv")
    return "Dataset is cleaned"


def TrainModel_LinearRegression(dataset:str,target:str):
    """
    Takes dataset file path as an argument and uses that dataset to train
    a Linear Regression model.
    Arguments:
        dataset: Path to CSV file
        target: Target column name
    """
    dataFrame = pd.read_csv(dataset)
    x = dataFrame.drop(columns=[target])
    y = dataFrame[target]
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.4,random_state=69)

    model = LinearRegression()

    model.fit(xtrain,ytrain)
    y_pred = model.predict(xtest)
    r2 = r2_score(ytest, y_pred)
    return f"R2 Score is {r2}"
    
dataSci_Tools = [clean_dataset,TrainModel_LinearRegression]

if __name__ == "__main__":
    clean_dataset(r"D:\ProgrammingStuff\AI Stuff\AI_Assistant\salaries.csv")
