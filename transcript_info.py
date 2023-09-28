import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

folder_path = "dataset/transcript_data"

if not os.path.isdir(folder_path):
    print("Invalid folder path. Please provide a valid folder path.")
    exit()
    
files = sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0]))

for i, file_name in enumerate(files, start=1):
    
    df = pd.read_csv(f"{folder_path}/{file_name}")
    
    speech_sentiment = {"positive" : df["positive"],
                        "negative" : df["negative"],
                        "neutral" : df["neutral"],
                        "confident" : df["confident"],
                        "hesitant" : df["hesitant"],
                        "concise" : df["concise"],
                        "enthusiastic" : df["enthusiastic"]}
    
    speech_speed = df["speech_speed"]
    
    speech_sentiment_mean = {}
    
    for key, value in speech_sentiment.items():
        speech_sentiment_mean[key] = value.mean()
    
    plt.figure(figsize=(6, 7))
        
    plt.bar(speech_sentiment_mean.keys(), speech_sentiment_mean.values())
    plt.xlabel("Speech Sentiment")
    plt.title(f"Mean speech sentiment values of candidate {i}")
    plt.xticks(rotation = 20)
    plt.savefig(f'candidate_details/{i}/speech_sentiment.png')
    plt.show()
    
    plt.plot(speech_speed)
    plt.title(f"Speech speed of candidate {i} throughout the video")
    plt.savefig(f'candidate_details/{i}/speech_speed.png')
    plt.show()
    
    