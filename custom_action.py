import numpy as np
import pandas as pd
from os import path
import datetime

def save_data(sender, message, response):
    time = datetime.datetime.now()
    if not path.exists("dataset/data_dump.csv"):
        df = pd.DataFrame([{"Time":time, "Sender_ID":sender, "Quary":message, "Response": response}])
        df.to_csv("dataset/data_dump.csv", index=False)
    else:
        df = pd.DataFrame([{"Time":time, "Sender_ID":sender, "Quary":message, "Response": response}])
        df.to_csv("dataset/data_dump.csv", mode='a', header=False, index=False)

def register_complaint(sender, message, response):
    time = datetime.datetime.now()
    if not path.exists("dataset/complaint_box.csv"):
        df = pd.DataFrame([{"Time":time, "Sender_ID":sender, "Quary":message, "Response": response}])
        df.to_csv("dataset/complaint_box.csv", index=False)
    else:
        df = pd.DataFrame([{"Time":time, "Sender_ID":sender, "Quary":message, "Response": response}])
        df.to_csv("dataset/complaint_box.csv", mode='a', header=False, index=False)

