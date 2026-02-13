# config.py

# Comprehensive SOC Project Configuration

# Region Bounds
REGION_BOUNDS = {
    'latitude_min': 30.0,
    'latitude_max': 50.0,
    'longitude_min': -120.0,
    'longitude_max': -70.0
}

# Temporal Settings
TEMPORAL_SETTINGS = {
    'start_date': '2020-01-01',
    'end_date': '2025-12-31',
    'frequency': 'daily'
}

# Model Configuration
MODEL_CONFIG = {
    'model_type': 'LSTM',  # Options: 'LSTM', 'RandomForest', etc.
    'input_size': 10,
    'hidden_size': 20,
    'num_layers': 2
}

# Training Configuration
TRAINING_CONFIG = {
    'batch_size': 64,
    'learning_rate': 0.001,
    'num_epochs': 100,
    'loss_function': 'MSE'  # Mean Squared Error
}

# Data Paths
DATA_PATHS = {
    'training_data': './data/train.csv',
    'validation_data': './data/val.csv',
    'test_data': './data/test.csv'
}

# Feature Names
FEATURE_NAMES = [
    'temperature',
    'humidity',
    'pressure',
    'wind_speed',
    'solar_radiation'
]

# Normalization Settings
NORMALIZATION_SETTINGS = {
    'normalize_features': True,
    'feature_range': (0, 1)  # For Min-Max normalization
}

# Validation Settings
VALIDATION_SETTINGS = {
    'cross_validation_splits': 5,
    'early_stopping': True,
    'patience': 5
}

if __name__ == "__main__":
    print("SOC Project Configuration Loaded Successfully.")