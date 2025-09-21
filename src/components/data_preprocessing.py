import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # new feature - card_id creation
    df["card_id"] = df["User"].astype(str) + "_" + df["Card"].astype(str)

    # new feature
    df["Hour"] = df["Time"].str [0:2]
    df["Minute"] = df["Time"].str [3:5]

    # datatype conversion
    df["Amount"]=df["Amount"].str.replace("$","")
    df["Amount"]=df["Amount"].astype(float)

    #drop irrelevant features
    df = df.drop(["Time","User","Card"],axis=1)
    df = df.drop(["Zip","Merchant State"],axis=1)

    # Handle missing values
    df["Errors?"]= df["Errors?"].fillna("No error")
    
    # change the 'is fraud?' column to binary 
    df["Is Fraud?"] = df["Is Fraud?"].apply(lambda x: 1 if x == 'Yes' else 0)

    #label encoding
    df["Merchant City"]=LabelEncoder().fit_transform(df["Merchant City"])
    df["Use Chip"]=LabelEncoder().fit_transform(df["Use Chip"])
    df["Errors?"]=LabelEncoder().fit_transform(df["Errors?"])
   
    return df