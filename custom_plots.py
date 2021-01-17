import numpy as np
import pandas as pd
import os
from os import path
import matplotlib.pyplot as plt
import seaborn as sns
import uuid

data_path = os.path.join("dataset", "asset_member.csv")
df = pd.read_csv(data_path)

def path_renamer():
    file_name = str(uuid.uuid4())+'.png'
    if not path.exists('static/'+file_name):
        return file_name
    else:
        path_renamer()

def plot_feat_count(feature):
    sns.set_style(style="whitegrid")
    plt.xticks(rotation=90)
    sns.barplot(x=df[feature].value_counts().keys(), y=df[feature].value_counts().values)
    file_name = path_renamer()
    plt.savefig("static/"+file_name, bbox_inches='tight')
    return "/static/"+file_name