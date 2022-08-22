from curses import noraw
import pandas as pd
import numpy as np
import pendulum


class SolanaJobs:
    def __init__(self):
        pass

    def solana_dataframe(self) -> None:
        """Import Dataset"""
        self.df = pd.read_csv(
            "./datasets/psycon/solana-usdt-to-20220-4-historical-data/sol-usdt.csv"
        )

    # DataTypes

    def preprocessing_dataframe(self) -> None:
        """Preprocessing Dataframe"""
        self.df.columns = [col.lower().replace(" ", "_") for col in self.df.columns]

    def feature_engineering(self) -> None:
        self.df["hour"] = pd.to_datetime(self.df["open_time"]).dt.hour

    # Rename Columns
    # Create Columns
    def add_columns(self) -> None:
        """Add Last Modified Column"""
        now = pendulum.now("America/Vancouver")
        now = now.to_datetime_string()
        self.df["last_modified"] = pd.to_datetime(now)

    # Drop Columns

    def drop_columns(self) -> None:
        """Dropping Columns"""
        self.df.drop(["ignore"], axis=1, inplace=True)

    # Filter by Date
    def filter_by_date(self) -> None:
        """Filter by Date"""
        self.df = self.df[self.df["open_time"] >= "2020-08-12"]
        self.df = self.df[self.df["open_time"] <= "2020-08-13"]

    # Filter by string
    # Filter by Regex
    # Filter by Multilple conditions
    def filter_by_multilpe_conitions(self) -> None:
        """Filter by Multiple Conditions"""
        self.df = self.df[
            (self.df["open_time"] >= "2020-08-12")
            & (self.df["open_time"] <= "2020-08-13")
            & (self.df["high"] <= 80.00)
            & (self.df["low"] >= 40.00)
        ]

    # Descriptive Statistics
    def descriptive_statistics(self) -> None:
        """Descriptive Statistics"""
        self.df.describe()

    # Counts
    def counts(self) -> None:
        """Counts"""
        self.counts = pd.DataFrame(jobs.df.count(), columns=["count"])

    # GroupBy
    def groupby(self) -> None:
        """GroupBy"""
        self.df.groupby("last_modified").count()

    # GroupBy Custom Aggregations
    def groupby_custom_aggregations(self) -> None:
        """GroupBy Custom Aggregations"""
        self.df.groupby("last_modified").agg({"high": "max", "low": "min"})

    # Sort
    def sort(self) -> None:
        """Sort"""
        self.df.sort_values(by="high", ascending=False)

    # Rank By
    def rank(self) -> None:
        """Rank By"""
        self.df["rank"] = self.df["high"].rank(ascending=False)

    # Rank By Window
    def rank_by_window(self) -> None:
        """Rank By Window"""
        self.df["rank"] = self.df["hour"].rank(ascending=False)

    def dense_rank_by_window(self) -> None:
        """Rank By Window"""
        self.df["dense_rank"] = self.df["hour"].rank(ascending=False, method="dense")

    # Get Dummies
    def get_dummies(self) -> None:
        """Get Dummies per Hour"""
        self.dummies = pd.get_dummies(self.df, columns=["hour"])

    # Create Nulls
    def create_nulls(self) -> None:
        """Create Nulls"""
        self.df["nulls"] = np.where(self.df["high"] == 0, 1, np.nan)

    def fill_nulls(self) -> None:
        """Fill Nulls"""
        self.df["nulls"] = self.df["nulls"].fillna(0)

    def dropna(self) -> None:
        """Drop Nulls"""
        self.df = self.df.dropna()

    # Joins/Merges
    # Pivots
    # def pivot(self) -> None:
    #     """Pivot"""
    #     self.df = self.df.pivot(self.df["open_time"], self.df["high"], self.df["low"])

    # Split and Explodes

    # Writing Data to CSV
    def export_csv(self) -> None:
        """Export to CSV"""
        self.df.to_csv("./output/sol-usdt.csv")

    # Writing Data to Excel
    def export_excel(self) -> None:
        """Export to Excel"""
        self.df.to_excel("./output/sol-usdt.xlsx")

    # Wriing Data to JSON
    def export_json(self) -> None:
        """Export to JSON"""
        self.df.to_json("./output/sol-usdt.json")

    # Writing Data to Parquet
    def export_parquet(self) -> None:
        """Export to Parquet"""
        self.df.to_parquet("./output/sol-usdt.parquet")
