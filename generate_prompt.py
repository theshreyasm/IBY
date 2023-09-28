import os

folder_path = "dataset/transcripts"
files = sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0]))

prompt = "I am hiring individuals for my company called I am Beside You. Given below are the transcripts of video resumes of 10 individuals applying for the job."

for i, file_name in enumerate(files, start=1):
    
    file_path = f"{folder_path}/{file_name}"
    
    with open(file_path, 'r') as file:
        transcript = file.read()
        
    prompt = prompt + "\n" + f"{i}." + transcript
    
prompt += "\nI want to read these transcripts and extract the essential details of each candidate such as candidate name, education, work experience, relevant skills and any other details you deem important. Additionally, I want you to judge the language proficiency of each candidate keeping in mind factors like vocabulary, flow of thoughts, and grammar and then categorize the proficiency out of great, good, satisfactory, bad, very bad. Create a csv file containing the candidate name, education, work experience, relevant skills, other details, language proficiency of each candidate. In entries of education, work experience, relevant skills and other details, if there are more than one sentence, I want the delimiter to be “.” And not “,”"
    
file_path = "prompt.txt"

with open(file_path, 'w') as file:
    file.write(prompt)