import os
import pandas as pd
from pathlib import Path
from typing import Tuple
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, data_path: str):
        self.data_path = data_path
    
    def read_csv(self, filename: str) -> pd.DataFrame:
        """Read CSV file and return DataFrame"""
        file_path = os.path.join(self.data_path, filename)
        df = pd.read_csv(file_path)
        return df
    
    def read_excel(self, filename: str) -> pd.DataFrame:
        """Read Excel file and return DataFrame"""
        file_path = os.path.join(self.data_path, filename)
        df = pd.read_excel(file_path)
        return df
    
    def get_data_info(self, df: pd.DataFrame) -> dict:
        """Get basic information about the dataset"""
        info = {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.to_dict(),
            'missing_values': df.isnull().sum().to_dict()
        }
        return info
    
    def train_test_split(self, df: pd.DataFrame, test_size: float = 0.2) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Split data into train and test sets"""
        train_df, test_df = train_test_split(df, test_size=test_size, random_state=42)
        return train_df, test_df