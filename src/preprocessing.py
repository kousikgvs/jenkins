import numpy as np
import pandas as pd


def preprocess_customer_data(data_frame: pd.DataFrame) -> pd.DataFrame:
    processed = data_frame.copy()
    processed['age'] = processed['age'].fillna(processed['age'].median())
    processed['city'] = processed['city'].astype(str).str.strip().str.title()
    processed['monthly_spend'] = pd.to_numeric(processed['monthly_spend'], errors='coerce').fillna(0.0)
    processed['spend_segment'] = np.where(processed['monthly_spend'] >= 1000, 'high', 'standard')
    return processed