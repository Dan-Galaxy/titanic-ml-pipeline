import pandas as pd
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="../configs", config_name="config.yaml",version_base=None)

def load_and_clean_data(cfg: DictConfig) -> pd.DataFrame:
    #Load Data
    df = pd.read_csv(cfg.data.path)
    print(f"Loaded data with {len(df)} rows")
    
    # Basic cleaning
    df = clean_data(df)
    print(f"Data cleaned. Missing values \n(df.isnull().sum())")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the Titanic dataset"""
    # Fill missing age with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    
    # Fill missing embarked with mode (most common value)
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # Drop cabin (too many missing) and other columns we won't use yet
    df = df.drop(['Cabin'], axis = 1)
    return df


if __name__ == "__main__":
    data = load_and_clean_data()
