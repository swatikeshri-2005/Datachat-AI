import pandas as pd
import os

UPLOADED_DIR = "uploads"

def save_csv(file):
    os.makedirs(UPLOADED_DIR, exist_ok=True)
    filepath = os.path.join(
        UPLOADED_DIR,
        file.filename
    )
    with open(filepath, "wb") as f:
        f.write(file.file.read())

    return filepath


def load_csv(path):
    return pd.read_csv(path)