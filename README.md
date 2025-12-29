#----------------------Basic Step------------------------

Step 1: Download the file in zip format.<br>
Step 2: Extract the file in folder naming MSR.<br>
Step 2: Combine files from folders similarity and similarity2 into single folder i.e part_0.pkl to part_12.pkl into single folder (COMBINING_FOLDERS)<br>
Step 3: after combining the folders combine all the file i.e part_0.pkl to part_12.pkl and rename the whole file to similarity.pkl (COMBINING_FiLES)<br>
Step 4: Add similarity.pkl file in main directory i.e MSR<br>

#===================Code to combine========================
for this create a file named Combine.py<br>
import pickle<br>

# Initialize an empty list to store the chunks<br>
combined_data = ['part_0.pkl', 'part_1.pkl','part_2.pkl','part_3.pkl','part_4.pkl','part_5.pkl','part_6.pkl','part_7.pkl','part_8.pkl','part_9.pkl','part_10.pkl','part_11.pkl','part_12.pkl', ]<br>

# Loop through the part files and load their data<br>
for i in range(num_parts):  # Replace 'num_parts' with the actual number of parts
    with open(f'part_{i}.pkl', 'rb') as f:
        chunk = pickle.load(f)
        combined_data.extend(chunk)
        
# Save the combined data to a single .pkl file
with open('similarity.pkl', 'wb') as f:
    pickle.dump(combined_data, f)

#==========================How to run the code----------------------------------

Step 1 : open terminal in vs code <br>
Step 2 : Change the directory by typing the following command "cd music_recommendation"<br>
Step 3 : Do migrations by typing the following command "python manage.py makemigrations"  <br>
Step 4 : Do migrate by typing the following command "python manage.py migrate"<br>
Step 5 : Now run the server by typing the following command "python manage.py runserver"<br>
Step 5 : copypaste the Url in the Browser   <br>



