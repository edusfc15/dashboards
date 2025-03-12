import pandas as pd
from utils.country_mapper import get_iso_alpha_3

def load_data(csv_file="data/comercio_bilateral_2024.csv"):
    """ Load trade data from a CSV file and map country names to ISO Alpha-3 codes. """
    try:
        df = pd.read_csv(csv_file, sep=";", dtype={"CO_ANO": str, "CORRENTE": str, "RANK": str})

        # Print raw data before processing
        print("Raw Data from CSV:\n", df.head())

        df["CORRENTE"] = df["CORRENTE"].str.replace(".", "", regex=False)  # Remove dots
        df["CORRENTE"] = pd.to_numeric(df["CORRENTE"], errors="coerce")
        df["RANK"] = pd.to_numeric(df["RANK"], errors="coerce")

        df["ISO_ALPHA"] = df["NO_PAIS"].apply(get_iso_alpha_3)

        # Print processed data to check if everything is correct
        print("Processed Data:\n", df.head())

        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None