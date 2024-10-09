import pandas as pd
import zipfile

def load_and_extract_zip(zip_file, extract_to="mental_health_data"):
    """Extract the dataset from a ZIP file."""
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted data to {extract_to}")

def load_and_concat_csv(file_list):
    """Load multiple CSV files and concatenate them."""
    df = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
    print("Loaded and concatenated CSV files.")
    return df

def clean_data(df):
    """Clean the data by dropping duplicates and null values."""
    df = df.drop_duplicates()
    df = df.drop(['score', 'CAT 1'], axis=1)
    df = df.dropna()
    print("Data cleaned.")
    return df

def save_clean_data(df, output_path):
    """Save the cleaned data to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Clean data saved to {output_path}")

if __name__ == "__main__":
    # Extract, load, and preprocess the data
    zip_file_path = "dataset/archive.zip"
    csv_files = [
        'mental_health_data/Original Reddit Data/Labelled Data/LD DA 1.csv',
        'mental_health_data/Original Reddit Data/Labelled Data/LD EL1.csv',
        'mental_health_data/Original Reddit Data/Labelled Data/LD PF1.csv',
        'mental_health_data/Original Reddit Data/Labelled Data/LD TS 1.csv'
    ]
    output_file = "processed_data.csv"

    load_and_extract_zip(zip_file_path)
    df = load_and_concat_csv(csv_files)
    clean_df = clean_data(df)
    save_clean_data(clean_df, output_file)

