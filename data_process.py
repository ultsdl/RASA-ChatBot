import pandas as pd
import numpy as np
import os
from os import path
import datetime
import mysql.connector

data_path = os.path.join("dataset", "asset_member.csv")
df = pd.read_csv(data_path)

def population():
    return len(df) 

def CountProperties(feat, query):
    if query=="count":
        output = len([i for i in df["bldg_typ"].unique() if type(i)==str])
        return "There are a total number of {} properties in this LSGD".format(output)
    elif query=="types":
        output = [i for i in df["bldg_typ"].unique() if type(i)==str] 
        return "Types of properties: {}".format(",".join(output))

def CatProperties(feat, cat):
    output = sum(df[feat]==cat)
    return output

def sql_query(user_id):
    mydb = mysql.connector.connect(
        host="database-1.cs2hezz6vd9p.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="testenv116",
        database=user_id)
    
    try:
        cursor = mydb.cursor()
        cursor.execute("""
        SELECT * from info
        """)
        result = cursor.fetchall()
        return result
    finally:
        mydb.close()

def property_count(feat, flag):
    result = df[feat].value_counts()[flag]
    if feat=="elec_conn":
        return "There are {} properties {} electricity".format(result, "without" if flag=="NO" else "with")
    elif feat=="gas_conn":
        return "There are {} properties {} gas connection".format(result, "without" if flag=="NO" else "with")
    elif feat=="bathroom":
        return "There are {} properties {} bathrooms".format(result, "without" if flag=="NO" else "with")
    elif feat=="ownr_occup":
        return "About {}({}%) people of {} in this LSGD were unemployed".format(result, round((result/len(df["ownr_occup"]))*100,2), len(df["ownr_occup"]))

def calc_tax(sender_id, feat, flag):
    if sender_id=="srudeep":
        df1 = pd.read_csv("dataset/calicut.csv")
    else:
        df1 = pd.read_csv("dataset/palakkad.csv")
    if flag=="max":
        output = df1[df1["Tax"]==df1["Tax"].max()]
    elif flag=="min":
        output = df1[df1["Tax"]==df1["Tax"].min()]
    return "{} tax paid was {} by the {} {}".format("Maximum" if flag=="max" else "Minimum", 
    output["Tax"].values[0], 
    output[feat].values[0],
    "property" if feat=="bldg_typ" else "th ward")
    