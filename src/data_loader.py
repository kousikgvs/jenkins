import pandas as pd

from src.static_data import get_static_customer_data


def load_customer_data() -> pd.DataFrame:
    return pd.DataFrame(get_static_customer_data())