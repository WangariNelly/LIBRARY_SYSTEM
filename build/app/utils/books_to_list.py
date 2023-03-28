#!/usr/bin/env pyrhon3

import pandas as pd
import numpy as np


def csv_to_list(path):
    """
    Args:
        path (path) - Path of the csv
    Return:
        Dataframe
    """
    df = pd.read_csv(path)
    return df.to_numpy().tolist()
