import pandas as pd
import numpy as np
from datetime import datetime


def write_time(data):
    data=data.lower().split(', ')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    df=pd.read_csv(r"C:\Users\Swift3\Documents\EventManager\Data\CheckInOut.csv")

    new_record = pd.DataFrame({'Team Name': [data[0]], 'Participants': [data[1]], 'Check In/Out': [data[2]], 'Time': [current_time]})
    df = pd.concat([df, new_record], ignore_index=True)

    df.to_csv(r"C:\Users\Swift3\Documents\EventManager\Data\CheckInOut.csv", index=False)

if __name__=="__main__":
    write_time('DevSquad, Pruthu Raut, Check In')
