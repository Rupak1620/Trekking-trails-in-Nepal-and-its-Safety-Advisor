import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from typing import Dict, List, Tuple
from data_processor import TrekkingDataProcessor
from weather_service import WeatherService

class SafetyPredictor:
    def __init__(self, data_processor: TrekkingDataProcessor, weather_service: WeatherService):
        self.data_processor = data_processor
        self.weather_service = weather_service
        self.model = None
        self.feature_columns = None
        
    def prepare_training_data(self) -> Tuple[pd.DataFrame, pd.Series]:
        """Prepare training data with synthetic safety labels based on features."""
        df = self.data_processor.get_processed_data()
        feature_columns = self.data_processor.get_feature_columns()
        
        # Create synthetic safety labels based on features
        # This is a simplified version - in a real scenario, you'd have historical safety data
        df['Safety_Level'] = 'Safe'  # Default
        
        # High risk conditions
        high_risk_mask = (
            (df['Average_Altitude_m'] > 5000) |
            (df['Difficulty_Score'] == 3) |
            (df['Altitude_Sickness'] == 1)
        )
        df.loc[high_risk_mask, 'Safety_Level'] = 'High Risk'
        
        # Moderate risk conditions
        moderate_risk_mask = (
            (df['Average_Altitude_m'] > 4000) |
            (df['Difficulty_Score'] == 2) |
            (df['Landslides'] == 1)
        )
        df.loc[moderate_risk_mask & ~high_risk_mask, 'Safety_Level'] = 'Moderate Risk'
        
        X = df[feature_columns]
        y = df['Safety_Level']
        
        return X, y
        
    def train_model(self) -> None:
        """Train the Random Forest model."""
        X, y = self.prepare_training_data()
        self.feature_columns = X.columns.tolist()
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Print accuracy
        accuracy = self.model.score(X_test, y_test)
        print(f"Model Accuracy: {accuracy:.2f}")
        
    def predict_safety(self, trail_name: str, current_weather: Dict) -> Dict:
        """Predict safety level for a given trail with current weather."""
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        # Get trail data
        df = self.data_processor.get_processed_data()
        trail_data = df[df['Trail_Name'] == trail_name].iloc[0]
        
        # Prepare features
        features = pd.DataFrame(columns=self.feature_columns)
        features.loc[0] = 0  # Initialize with zeros
        
        # Set known features
        for col in self.feature_columns:
            if col in trail_data:
                features[col] = trail_data[col]
                
        # Add weather impact
        weather_impact = self.weather_service.get_safety_impact(current_weather)
        if weather_impact == 'High Risk':
            features['Difficulty_Score'] += 1
        elif weather_impact == 'Moderate Risk':
            features['Difficulty_Score'] += 0.5
            
        # Make prediction
        safety_level = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0]
        
        return {
            'safety_level': safety_level,
            'confidence': max(probability),
            'weather_impact': weather_impact,
            'weather_summary': self.weather_service.get_weather_summary(current_weather)
        }

def main():
    # Example usage
    data_processor = TrekkingDataProcessor('trekking_routes_safety_dataset.csv')
    data_processor.load_data()
    data_processor.clean_data()
    
    weather_service = WeatherService()
    predictor = SafetyPredictor(data_processor, weather_service)
    predictor.train_model()
    
    # Example prediction
    weather_data = weather_service.get_weather_data(27.9881, 86.9250)  # Everest Base Camp
    prediction = predictor.predict_safety('Everest Base Camp Trek', weather_data)
    print("\nSafety Prediction:")
    print(prediction)

if __name__ == "__main__":
    main() 