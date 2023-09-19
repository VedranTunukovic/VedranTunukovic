import os
import shutil
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


path_to_samples = r'C:\Users\Vedran\Desktop\results'
path_to_new_folder = r"C:\Users\Vedran\Desktop\extracted_results"
        

def Task1():
    ### Open every subfolder and create new one where only certain stuff is copied
    
    for sample_folder in os.listdir(path_to_samples):
        print("Opening sample ", sample_folder)
        
        subfolder_path = os.path.join(path_to_samples, sample_folder)
        
        # Open each subfolder
        for file_name in os.listdir(subfolder_path):
            
            # Check for the ID of the sample and create a new corresponding folder
            if file_name.endswith(".html"):
                continue
            
            if file_name.startswith("._"):
                continue
            
            else:
                subfolder = os.path.join(subfolder_path, file_name)
                
                ### For creation of new folder
                folder_name = os.path.splitext(file_name)[0]
                id = folder_name[-3:]
                new_folder_path = os.path.join(path_to_new_folder, id)
                os.makedirs(new_folder_path, exist_ok=True)

            ### Open subfolder
            for new_file_name in os.listdir(subfolder):
                              
                ### Locate InDel.stat.xls file
                if new_file_name == "InDel.stat.xls":
                    for_file = os.path.join(subfolder, new_file_name)
                    for_file_2 = os.path.join(new_folder_path, new_file_name)
                    shutil.copyfile(for_file, for_file_2)
                    
                if new_file_name == "QC_stat.xls":
                    for_file = os.path.join(subfolder, new_file_name)
                    for_file_2 = os.path.join(new_folder_path, new_file_name)
                    shutil.copyfile(for_file, for_file_2)
               
                ### Locate  chrManno.xls file
                if "chrManno.xls" in new_file_name:
                    if new_file_name.startswith("._"):
                        continue
                    else:
                        for_file = os.path.join(subfolder, new_file_name)
                        for_file_2 = os.path.join(new_folder_path, new_file_name)
                        shutil.copyfile(for_file, for_file_2)
                    
                ### Locate significant.snp_indel.xls file
                if "significant.snp_indel.xls" in new_file_name:
                    if new_file_name.startswith("._"):
                        continue
                    else:
                        for_file = os.path.join(subfolder, new_file_name)
                        for_file_2 = os.path.join(new_folder_path, new_file_name)
                        shutil.copyfile(for_file, for_file_2)
                     
                ### Locate significant.snp_indel.xls file
                if "sv.xls" in new_file_name:
                    if new_file_name.startswith("._"):
                        continue
                    else:
                        for_file = os.path.join(subfolder, new_file_name)
                        for_file_2 = os.path.join(new_folder_path, new_file_name)
                        shutil.copyfile(for_file, for_file_2)
                        
                ### Locate significant.snp_indel.xls file
                if "R1.clean_fastqc.html" in new_file_name:
                    if new_file_name.startswith("._"):
                        continue
                    else:
                        for_file = os.path.join(subfolder, new_file_name)
                        for_file_2 = os.path.join(new_folder_path, new_file_name)
                        shutil.copyfile(for_file, for_file_2)
                        
                ### Locate significant.snp_indel.xls file
                if "R2.clean_fastqc.html" in new_file_name:
                    if new_file_name.startswith("._"):
                        continue
                    else:
                        for_file = os.path.join(subfolder, new_file_name)
                        for_file_2 = os.path.join(new_folder_path, new_file_name)
                        shutil.copyfile(for_file, for_file_2)
                
    return


#%%
path_to_samples = r'C:\Users\Vedran\Desktop\results'
path_to_new_folder = r"C:\Users\Vedran\Desktop\all_results"
        

def Task2():
    ### Copy all files
    
    for sample_folder in os.listdir(path_to_samples):
        print("Opening sample ", sample_folder)
        
        subfolder_path = os.path.join(path_to_samples, sample_folder)
        
        # Open each subfolder
        for file_name in os.listdir(subfolder_path):
            
            # Check for the ID of the sample and create a new corresponding folder
            
            ### Skip html report
            if file_name.endswith(".html"):
                continue
            
            ### Skip hidden files
            if file_name.startswith("._"):
                continue
            
            else:
                subfolder = os.path.join(subfolder_path, file_name)
                
                ### For creation of new folder
                folder_name = os.path.splitext(file_name)[0]
                id = folder_name[-3:]
                new_folder_path = os.path.join(path_to_new_folder, id)
                os.makedirs(new_folder_path, exist_ok=True)

            ### Open subfolder
            for new_file_name in os.listdir(subfolder):
                
                ### Skip readme file
                if new_file_name == "readme.txt":
                    continue
                    
                if new_file_name.startswith("._"):
                    continue
                
                    
                for_file = os.path.join(subfolder, new_file_name)
                for_file_2 = os.path.join(new_folder_path, new_file_name)
                shutil.copyfile(for_file, for_file_2)
                
    return

#%% Task 3

### Change snips accordingly
snips = [" AQP4"]
         # " DNAJC6",
         # " FBXO7",
         # " GBA",
         # " LRP10",
         # " MAPT",
         # " LRRK2",
         # " PLA2G6",
         # " PARK7",
         # " PRKN",
         # " PINK1",
         # " SNCA",
         # " SYNJ1",
         # " VPS35"
         # ]

path_to_samples = "C:/Users/Vedran/Desktop/all_results"
import gzip

def uncompress_gzip_file(gzip_file_path, output_path):
    with gzip.open(gzip_file_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Define the temporary folder path on the desktop
temp_folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "temp_folder")

# Create the temporary folder if it doesn't exist
if not os.path.exists(temp_folder_path):
    os.makedirs(temp_folder_path)

# Open each subfolder
for sample_folder in os.listdir(path_to_samples):
    print("Opening sample ", sample_folder)
    ID = sample_folder
    subfolder_path = os.path.join(path_to_samples, sample_folder)
    
    for file_name in os.listdir(subfolder_path):
        if ".snp_indel.xls.gz" in file_name:
            
            gzip_file_path = os.path.join(subfolder_path, file_name)  # Path to the compressed .gz file
            print("Path to compressed ", gzip_file_path)
            
            
            output_filename = file_name[:-3] + ".xls"  # Remove the last 3 characters (.gz) and add .xls extension
            output_path = os.path.join(temp_folder_path, output_filename)  # Path where the uncompressed file will be saved
            
            print("Path to uncompressed", output_path)
            uncompress_gzip_file(gzip_file_path, output_path)
                            
        if ".snp_indel.xls" in file_name:
            file_name = os.path.join(subfolder_path, file_name)
            
            try:
                df = pd.read_csv(file_name, sep='\t', encoding='cp1252')
                
                
                # create a new dataframe to store the matching rows
                new_df = pd.DataFrame()
                new_df_2 = pd.DataFrame()
                
                # iterate through each row of the original dataframe
                for index, row in df.iterrows():
                
                    # check if the value in the Gene.refGene column is in the predetermined list
                    if row["Gene.refGene"] in snips:
                        
                        # if it is, copy the entire row (including header) into the new dataframe
                        new_df = new_df.append(row, ignore_index=True)
                        
                #### Second        
                # iterate through each row of the original dataframe
                for index, row in df.iterrows():
                
                    # check if the value in the Gene.refGene column is in the predetermined list
                    if row["InterVar"] == "Pathogenic":
                        new_df_2 = new_df_2.append(row, ignore_index=True)
                    if row["InterVar"] == "Likely pathogenic":
                        new_df_2 = new_df_2.append(row, ignore_index=True)
                # save the new dataframe to a CSV file
                new_df.to_csv(f"{subfolder_path}/panel_{ID}.csv", index=False)
                new_df_2.to_csv(f"{subfolder_path}/path_{ID}.csv", index=False)
            except pd.errors.EmptyDataError:
                print("No columns to parse from file. Skipping:", file_name)



#%% Task 4

snips = [" AQP4"," AQP4-AS1", " PCAT18;AQP4"]

path_to_samples = "C:/Users/Vedran/Desktop/all_results"
path_to_xls = "C:/Users/Vedran/Desktop/temp_folder"
new_folder = "C:/Users/Vedran/Desktop/AQP4_panel"


# Create the main folder "AQP4_panel"
os.makedirs(new_folder, exist_ok=True)

for sample_folder in os.listdir(path_to_samples):
    print("Opening sample ", sample_folder)
    ID = sample_folder
    print("ID", ID)
    subfolder_path = os.path.join(path_to_samples, sample_folder)
    check = ID + ".snp_indel.xls"
    
    xls_filename = None
    for file_name in os.listdir(path_to_xls):
        if check in file_name and file_name.endswith(".xls"):
            xls_filename = file_name
            print("cjeck :",xls_filename)
            break
        
    if xls_filename is not None:
        xls_file_path = os.path.join(path_to_xls, xls_filename)
        
    
    df = pd.read_csv(xls_file_path, sep='\t', encoding='cp1252')
    
    new_df = pd.DataFrame()
    
    for index, row in df.iterrows():
        if row["Gene.refGene"] in snips:
            new_df = new_df.append(row, ignore_index=True)
            
    
    # Create the subfolder within the "AQP4_panel" folder
    subfolder_name = f"{new_folder}/{ID}"
    print("APP4 folder, ", subfolder_name)
    os.makedirs(subfolder_name, exist_ok=True)
    print("Created: ", subfolder_name)
    
    # Save the CSV file within the subfolder
    new_df.to_csv(f"{subfolder_name}/AQP4_panel_{ID}.csv", index=False)       

