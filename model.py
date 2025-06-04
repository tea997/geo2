import pandas as pd
import numpy as np

def preprocess_data(file_path_or_df):
    if isinstance(file_path_or_df, str):
        df = pd.read_csv(file_path_or_df)
    else:
        df = file_path_or_df.copy()

    # Function to check if value contains '<' or '>'
    def is_special_val(x):
        if isinstance(x, str):
            return ('<' in x) or ('>' in x)
        return False

    cols_to_drop = []

    for col in df.columns:
        # Count how many values contain '<' or '>'
        special_mask = df[col].apply(is_special_val)
        special_count = special_mask.sum()
        total_count = len(df[col])

        if special_count >= total_count / 2:
            # Drop column if half or more values are special
            cols_to_drop.append(col)
        else:
            # Replace special values with NaN temporarily
            df.loc[special_mask, col] = np.nan
            # Convert to numeric (coerce errors to NaN)
            df[col] = pd.to_numeric(df[col], errors='coerce')

            # Replace NaN with median (or mean)
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)

    # Drop columns with too many special values
    df.drop(columns=cols_to_drop, inplace=True)

    # After cleaning special values, replace other empty strings or '<' as you had before
    df.replace(['', '<'], np.nan, inplace=True)

    # Fill NaN values with your specified defaults (optional, from your original code)
    df.fillna({
        'SiO2': 0.1, 'TiO2': 0.01, 'Al2O3': 0.1, 'Fe2O3': 0.1, 'MnO': 0.03, 'MgO': 0.01,
        'CaO': 0.01, 'Na2O': 0.1, 'K2O': 0.1, 'P2O5': 0.01, 'LOSS': 0.1, 'Ba': 50, 'Sc': 50,
        'Co': 1, 'Cr': 15, 'Ni': 2, 'Cu': 1, 'Zn': 10, 'Ga': 5, 'Rb': 3, 'Sr': 5, 'V': 20,
        'Y.1': 5, 'Zr': 5, 'Nb': 5, 'Pb': 2, 'Th': 4, 'Au': 0.003, 'Li': 5, 'Cs': 10, 'As': 1,
        'Sb': 0.2, 'Bi': 0.1, 'Se': 0.2, 'F': 100, 'Ag': 0.02, 'Cd': 0.1, 'Hg': 0.01, 'Be': 0.3,
        'Ge': 0.05, 'Mo': 5, 'Sn': 5, 'La': 1, 'Ce': 2, 'Pr': 2, 'Nd': 0.3, 'Sm': 0.1, 'Eu': 0.02,
        'Gd': 0.05, 'Tb': 0.01, 'Dy': 0.03, 'Ho': 0.01, 'Er': 0.02, 'Tm': 0.1, 'Yb': 0.2, 'Lu': 0.1,
        'Hf': 0.2, 'Ta': 0.2, 'W': 5, 'U': 0.5
    }, inplace=True)

    return df
