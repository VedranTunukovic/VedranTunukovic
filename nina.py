import os
import pandas as pd

# Change extensions - Run only once


def clean_extensions(samples):
    for i in range(samples):  # Change depending on how many samples you have
        # Change this path to accordingly
        path = f"C:/Users/Vedran/Desktop/Nina/{i}"
        # Iterates through all files in all folders
        for filename in os.listdir(path):
            old_file_name = os.path.join(
                path, filename)  # Takes the old file name
            new_file_name = old_file_name.replace(
                '.xls', '.csv')  # Replaces it with .csv extension
            # Renames file with new name
            os.rename(old_file_name, new_file_name)
            print("Extension changed from .xls to .csv for:",
                  filename)  # Tells you what files were changed


# Load reference sample
def load_reference():
    path = r'C:\Users\Vedran\Desktop\Nina'  # Change this path for use with your PC
    filename = 'reference.xlsx'  # Change this accordig to your reference
    # Creates a full path from previous two variables
    full_path = os.path.join(path, filename)
    # Reads in that reference file as a variable
    reference = pd.read_excel(full_path)
    return reference


reference = load_reference()


def process(samples):
    for i in range(samples):  # Change depending on how many samples you have
        # Change this path accordingly
        path = f"C:/Users/Vedran/Desktop/Nina/{i}"
        for filename in os.listdir(path):  # Again iterates through everything
            full_path = os.path.join(path, filename)  # Full path is read
            # Read the data with dumb encoding
            df = pd.read_csv(full_path, sep='\t', encoding='cp1252')
            # Remove redundant columns
            df2 = df[["avsnp150", "Ref", "Alt", "GT"]]

            # Checking if in reference and removing other crap
            # extract the first column values from reference dataframe into a list
            col1_values = reference.iloc[:, 0].tolist()
            # keep only the rows in df2 where the value in the first column exists in the list of col1_values
            df2 = df2[df2.iloc[:, 0].isin(col1_values)]
            # Remove everything that is not in reference
            df2.reset_index(drop=True, inplace=True)
            # Rename the first column
            df2.rename(columns={"avsnp150": "SNP"}, inplace=True)

            # Checking what is missing from the data and adding it in with 0/0
            # Store existing values from the new data
            existing_values = set(frozenset(row)
                                  for row in df2.iloc[:, 0:1].values)
            for index, row in reference.iterrows():  # Iterate over reference file
                # Check if everything from reference is in new data
                if frozenset(row.iloc[0:1]) not in existing_values:
                    new_row = row.copy()  # If it is not, copy that row
                    new_row["GT"] = '0/0'  # Change last column to 0/0
                    # Add new row to the data
                    df2 = df2.append(new_row, ignore_index=True)
                    # Update existing values
                    existing_values.add(frozenset(row.iloc[0:1]))

            save_path = os.path.join(path, str(i))  # Determine save path
            print("saving here:", save_path)  # Tells you where it will save
            df2.to_excel(save_path + filename + '_clean.xlsx',
                         index=False)  # Save to new excel file
