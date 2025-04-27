import pandas as pd
import numpy as np
from typing import Tuple

class TrekkingDataProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        
    def load_data(self) -> None:
        """Load the dataset from CSV file."""
        self.df = pd.read_csv(self.file_path)
        
    def clean_data(self) -> None:
        """Clean and preprocess the dataset."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Convert altitude to numeric, handling any non-numeric values
        self.df['Average_Altitude_m'] = pd.to_numeric(self.df['Average_Altitude_m'], errors='coerce')
        
        # Create binary features for known risks
        risk_columns = ['Altitude_Sickness', 'Landslides', 'Cold_Weather', 'Remote_Access', 'High_Winds']
        for risk in risk_columns:
            self.df[risk] = self.df['Known_Risks'].str.contains(risk.replace('_', ' '), case=False).astype(int)
            
        # Convert difficulty to ordinal values
        difficulty_map = {'Easy': 1, 'Moderate': 2, 'Hard': 3}
        self.df['Difficulty_Score'] = self.df['Trail_Difficulty'].map(difficulty_map)
        
        # Create season binary features
        seasons = ['Pre-Monsoon', 'Post-Monsoon', 'Monsoon', 'Winter']
        for season in seasons:
            self.df[f'Season_{season}'] = self.df['Typical_Season'].str.contains(season, case=False).astype(int)
            
    def get_processed_data(self) -> pd.DataFrame:
        """Return the processed dataset."""
        if self.df is None:
            raise ValueError("Data not processed. Call clean_data() first.")
        return self.df
        
    def get_feature_columns(self) -> list:
        """Return list of feature columns for model training."""
        return [
            'Difficulty_Score',
            'Average_Altitude_m',
            'Altitude_Sickness',
            'Landslides',
            'Cold_Weather',
            'Remote_Access',
            'High_Winds',
            'Season_Pre-Monsoon',
            'Season_Post-Monsoon',
            'Season_Monsoon',
            'Season_Winter'
        ]

def main():
    # Example usage
    processor = TrekkingDataProcessor('trekking_routes_safety_dataset.csv')
    processor.load_data()
    processor.clean_data()
    processed_df = processor.get_processed_data()
    print("\nProcessed Dataset Preview:")
    print(processed_df.head())
    print("\nFeature Columns:")
    print(processor.get_feature_columns())

if __name__ == "__main__":
    main() 