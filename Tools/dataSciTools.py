from langchain.tools import tool
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

def clean_dataset(file_path:str):
    dataFrame = pd.read_csv(file_path)

    #selecting catagorical columns
    catogorical_data = dataFrame.select_dtypes(exclude=['number']).columns

    le = LabelEncoder()


    for col in catogorical_data:
        dataFrame[col] = le.fit_transform(dataFrame[col])
    
    os.makedirs("CleanedCSV",exist_ok=True)
    dataFrame.to_csv("CleanedCSV/cleaned.csv")
    return "Dataset is cleaned"



if __name__ == "__main__":
    clean_dataset(r"D:\ProgrammingStuff\AI Stuff\AI_Assistant\salaries.csv")
