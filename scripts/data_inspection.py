from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "online_retail_II.xlsx"


def main() -> None:
    print("Loading data... this is a large file, so it might take a minute.")
    df = pd.read_excel(RAW_PATH)

    print("\n--- Data Information ---")
    df.info()

    print("\n--- Data Summary ---")
    print(df.describe())


if __name__ == "__main__":
    main()
