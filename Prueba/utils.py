# 4. Este archivo contendrá cualquier otra función auxiliar que puedas necesitar.

import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)
