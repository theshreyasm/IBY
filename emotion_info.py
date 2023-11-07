import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

directory_path = "dataset/emotion_data"

folder_names = sorted([int(folder) for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))])

for i in folder_names:
    
    df_emotion = pd.read_csv(f"{directory_path}/{i}/emotion.csv")
    df_gaze = pd.read_csv(f"{directory_path}/{i}/gaze.csv")
    
    emotion = {"angry" : df_emotion["angry"],
                        "disgust" : df_emotion["disgust"],
                        "fear" : df_emotion["fear"],
                        "happy" : df_emotion["happy"],
                        "sad" : df_emotion["sad"],
                        "surprise" : df_emotion["surprise"],
                        "neutral" : df_emotion["neutral"]}
    
    emotion_mean = {}
    
    for key, value in emotion.items():
        emotion_mean[key] = value.mean()
    
    dominant_emotion = max(emotion_mean, key=lambda k: emotion_mean[k])
    
    plt.figure(figsize=(26, 11))
    labels = list(emotion_mean.keys())
    values = list(emotion_mean.values())
    plt.pie(values, labels=[None]*len(labels))    
    legend_labels = [f'{label} ({value:.2f}%)' for label, value in zip(labels, values)]
    plt.legend(legend_labels, loc='upper right')
    plt.text(0, -1.1, f'Dominant Emotion: {dominant_emotion}', ha='center', va='center', fontsize=13)
    plt.title(f'Emotions Distribution for Candidate {i}', fontsize=16, fontweight='bold', y=-0.1)
    plt.savefig(f'candidate_details/{i}/emotion.png')
    plt.show()
    
    df = pd.merge(df_emotion, df_gaze, on='image_seq', how='inner')
    df.drop('movie_id_y', axis=1, inplace=True)
    df.rename(columns={'movie_id_x': 'movie_id'}, inplace=True)
    
    df_correlation = df[['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral', 'gaze', 'eye_offset']]
    correlation_matrix = df_correlation.corr()
    
    plt.figure(figsize=(10, 8))
    plt.title(f"Correlation heatmap for Candidate {i}", fontweight = 'bold')
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.savefig(f'candidate_details/{i}/correlation.png')
    plt.show()
    
    gaze = df_gaze["gaze"]
    image_seq = df_gaze["image_seq"]
    percentage_gaze = (sum(gaze) / len(gaze)) * 100
    
    plt.figure(figsize=(28, 20))
    plt.step(image_seq, gaze, where='mid', color='b')
    plt.ylabel("Gaze", fontsize=20)
    plt.xlabel("Image sequence", fontsize=20)
    plt.title(f"Gaze of Candidate {i}", fontsize=28, fontweight='bold')
    explanation_text = "Gaze 1 = Person looked into the camera\nGaze 0 = Person did not look into the camera"
    plt.text(image_seq.min(), -0.20, explanation_text, ha='left',  fontsize=14, color='gray')
    plt.text(image_seq.min(), -0.15, f'Percentage of frames looked into the camera: {percentage_gaze:.2f}%', va='center',  fontsize=14, fontweight='bold')
    plt.yticks([0, 1])
    plt.savefig(f'candidate_details/{i}/gaze.png')
    plt.show()
    
    