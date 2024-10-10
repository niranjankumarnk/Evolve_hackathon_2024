import pandas as pd
import kaggle
import os

def download_dataset():
    """Download the dataset from Kaggle."""
    print("Downloading dataset from Kaggle...")
    kaggle.api.dataset_download_files('entenam/reddit-mental-health-dataset', path='dataset/', unzip=True)
    print("Download complete.")
    return 'dataset/'

def load_and_concat_csv(file_list):
    """Load multiple CSV files and concatenate them."""
    df_list = []
    for file in file_list:
        if os.path.exists(file):
            df_list.append(pd.read_csv(file))
            print(f"Loaded {file}")
        else:
            print(f"File not found: {file}")
    df = pd.concat(df_list, ignore_index=True)
    print("Loaded and concatenated CSV files.")
    return df

def clean_data(df):
    """Clean the data by dropping duplicates and null values."""
    df = df.drop_duplicates()
    df = df.drop(['score', 'CAT 1'], axis=1, errors='ignore')
    df = df.dropna()
    print("Data cleaned.")
    return df

def save_clean_data(df, output_path):
    """Save the cleaned data to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Clean data saved to {output_path}")

if __name__ == "__main__":
    # Download and preprocess the data
    dataset_path = download_dataset()
    
    # Define the paths to your CSV files
    csv_files = [
        os.path.join(dataset_path, 'Original Reddit Data/Labelled Data/LD DA 1.csv'),
        os.path.join(dataset_path, 'Original Reddit Data/Labelled Data/LD EL1.csv'),
        os.path.join(dataset_path, 'Original Reddit Data/Labelled Data/LD PF1.csv'),
        os.path.join(dataset_path, 'Original Reddit Data/Labelled Data/LD TS 1.csv')
    ]

    # Load, clean, and save the data
    df = load_and_concat_csv(csv_files)
    clean_df = clean_data(df)
    output_file = "processed_data.csv"
    save_clean_data(clean_df, output_file)

