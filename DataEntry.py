import pandas as pd 
import numpy as np

def write(data):
    print(data)
    data=data.lower().split(', ')
    print(data)
    df=pd.read_csv(r"C:\Users\Swift3\Documents\EventManager\Data\Data.csv")
    print(data[2].capitalize())
    df.loc[(df["Team Names"]==data[0]) & (df["Participants"]==data[1]),[data[2].capitalize()]] = 'Y'
    
    df.to_csv(r"C:\Users\Swift3\Documents\EventManager\Data\Data.csv", index=False)

if __name__=="__main__":
    write("agri genius, gargi hawaldar, Lunch")