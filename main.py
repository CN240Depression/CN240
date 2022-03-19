import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

import os


df = pd.read_csv("data/legend.csv") #ที่อยู่ของlegend.csv



option = []
for file in os.listdir("notblur/"): #ที่อยู่ของรูปภาพที่ไม่ใช้
    option.append(file)
print(len(option))
test_df = df[df["image"].isin(option)]
test_df["emotion"] = test_df["emotion"].str.upper()
test_df.emotion = test_df.emotion.astype("category")

test_df_ANGER = test_df[test_df["emotion"] == "ANGER"]

print("Anger >" ,test_df_ANGER["emotion"].size)
test_df_CONTEMPT = test_df[test_df["emotion"] == "CONTEMPT"]
print("CONTEMPT >" ,test_df_CONTEMPT["emotion"].size)

test_df_DISGUST = test_df[test_df["emotion"] == "DISGUST"]
print("DISGUST >" ,test_df_DISGUST["emotion"].size)

test_df_FEAR = test_df[test_df["emotion"] == "FEAR"]
print("FEAR >" ,test_df_FEAR["emotion"].size)

test_df_HAPPINESS = test_df[test_df["emotion"] == "HAPPINESS"]
print("HAPPINESS >" ,test_df_HAPPINESS["emotion"].size)

test_df_NEUTRAL = test_df[test_df["emotion"] == "NEUTRAL"]
print("NEUTRAL >" ,test_df_NEUTRAL["emotion"].size)

test_df_SADNESS = test_df[test_df["emotion"] == "SADNESS"]
print("SADNESS >" ,test_df_SADNESS["emotion"].size)

test_df_SURPRISE = test_df[test_df["emotion"] == "SURPRISE"]
print("SURPRISE >" ,test_df_SURPRISE["emotion"].size)

features_cat = ["emotion"]
for f in features_cat:
    plt.rcParams['font.size'] = '20'
    test_df[f].value_counts().sort_index().plot(kind='bar')
    plt.subplots_adjust(bottom=0.20)
    fig1 = plt.gcf()
    plt.title(f)
    plt.grid()
    plt.show()



