import pandas as pd
import glob


def vertical_merge(input_dir):
    files = glob.glob(input_dir)
    df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
    return df