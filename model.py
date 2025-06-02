# model.py (Preprocessing Only)
import pandas as pd
import numpy as np

def preprocess_data(file_path_or_df):
    if isinstance(file_path_or_df, str):
        df = pd.read_csv(file_path_or_df)
    else:
        df = file_path_or_df.copy()
    
    df.replace(['', '<'], np.nan, inplace=True)

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
