from tkinter.filedialog import askopenfile
import pandas as pd
import numpy as np

class SolanaJobs:
    def __init__(self):
        pass

    def solana_dataframe(self) -> pd.DataFrame:
        """Import Dataset"""
        df = pd.read_csv(
            "./datasets/psycon/solana-usdt-to-20220-4-historical-data/sol-usdt.csv"
        )
        return df

    # DataTypes
    # Rename Columns
    # Create Columns
    # Drop Columns
    # Filter by Date
    # Filter by string
    # Filter by Regex
    # Filter by Multilple conditions

    # Descriptive Statistics
    # Counts
    # Describe
    # GroupBy
    # GroupBy Custom Aggregations

    # Rank By
    # Rank By Window

    # Fill Nulls
    # Remove Nulls

    # Joins/Merges
    # Pivots
    # Split and Explodes

    # Writing Data to CSV
    # Writing Data to Excel
    # Wriing Data to JSON
    # Writing Data to Parquet
