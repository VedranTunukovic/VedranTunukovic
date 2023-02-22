import os
import glob
import pandas as pd

def clean_extensions(samples):
    """
    This function reads in .xls files and changes the extension to .csv
    
    Parameters
    ----------
    samples : int
        Set the number of samples to process

    Returns
    -------
    None.

    """
    for i in range(1, samples+1):
        path = f"C:/Users/Vedran/Desktop/Nina/{i}"
        for old_file_name in glob.glob(os.path.join(path, '*.xls')):
            file_name, extension = os.path.splitext(old_file_name)
            new_file_name = file_name + '.csv'
            os.rename(old_file_name, new_file_name)
            print("Extension changed from .xls to .csv for:", old_file_name)


def process(samples):
    """
    This function processes the given samples and compares them to the reference

    Parameters
    ----------
    samples : int
        Set the number of samples to process

    Returns
    -------
    None.

    """
    path = r'C:\Users\Vedran\Desktop\Nina'
    filename = 'reference.xlsx'
    full_path = os.path.join(path, filename)
    reference = pd.read_excel(full_path)

    for i in range(1, samples+1):
        path = f"C:/Users/Vedran/Desktop/Nina/{i}"
        for file_name in glob.glob(os.path.join(path, '*.csv')):
            df = pd.read_csv(file_name, sep='\t', encoding='cp1252')
            df = df[["avsnp150", "Ref", "Alt", "GT"]]
            df.rename(columns={"avsnp150": "SNP"}, inplace=True)
            df = df[df['SNP'].isin(reference.iloc[:, 0].to_list())]

            existing_values = set(frozenset(row) for row in df[["SNP", "Ref", "Alt"]].values)
            for _, row in reference.iterrows():
                if frozenset(row[0:3]) not in existing_values:
                    new_row = pd.DataFrame([row[0], row[1], row[2], '0/0'], index=df.columns).T
                    df = pd.concat([df, new_row], ignore_index=True)
                    existing_values.add(frozenset(row[0:3]))

            save_filename = os.path.splitext(os.path.basename(file_name))[0] + '_clean.xlsx'
            df.to_excel(os.path.join(path, save_filename), index=False)