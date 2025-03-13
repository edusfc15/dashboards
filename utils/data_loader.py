import pandas as pd
from utils.country_mapper import get_iso_alpha_3

def load_data(csv_file="data/comercio_bilateral_2024.csv"):
    """ Load trade data from a CSV file and map country names to ISO Alpha-3 codes. """
    try:
        df = pd.read_csv(csv_file, sep=";", dtype={"CO_ANO": str, "CORRENTE": str, "RANK": str})

        # Remove dots from numbers and convert to float
        df["CORRENTE"] = df["CORRENTE"].str.replace(".", "", regex=False)
        df["CORRENTE"] = pd.to_numeric(df["CORRENTE"], errors="coerce")  # Convert invalid values to NaN

        df["RANK"] = pd.to_numeric(df["RANK"], errors="coerce")  # Convert to int (NaN if empty)

        # Map country names to ISO Alpha-3 codes
        df["ISO_ALPHA"] = df["NO_PAIS"].apply(get_iso_alpha_3)

        # ✅ Fix: Remove rows where CORRENTE or ISO_ALPHA is NaN
        df = df.dropna(subset=["CORRENTE", "ISO_ALPHA"])

        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
