import os

candidate_details_folder = "candidate_details"

if not os.path.exists(candidate_details_folder):
    os.makedirs(candidate_details_folder)
    
for i in range(1,11):
    
    full_path = os.path.join(candidate_details_folder, str(i))
    if not os.path.exists(full_path):
        os.makedirs(full_path)
