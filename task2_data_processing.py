import os
from datetime import datetime
import pandas as pd

print("script started")
def main():
    # Input file from local data folder
    today_date = datetime.now().strftime("%Y%m%d")
    input_path = os.path.join("data", f"trends_{today_date}.json")

    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"{input_path} not found. Run task1_fetch.py first."
        )

    # Load JSON
    df = pd.read_json(input_path)
    print("Loaded rows:", len(df))

    # Remove duplicates
    df = df.drop_duplicates(subset="post_id")
    print("After removing duplicates:", len(df))

    # Handle missing values
    df = df.dropna(subset=["post_id", "title", "score"])
    print("After dropping missing post_id/title/score:", len(df))

    # Fix data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].fillna(0).astype(int)
    print("Data types fixed:")
    print(df[["score", "num_comments"]].dtypes)

    # Remove low-quality rows
    df = df[df["score"] >= 5]
    print("After removing low-score stories:", len(df))

    # Strip extra spaces
    df["title"] = df["title"].str.strip()
    print("Title whitespace cleaned.")

    # Save cleaned CSV locally
    output_path = os.path.join("data", "trends_clean.csv")
    df.to_csv(output_path, index=False)

    print(f"Saved {len(df)} rows to {output_path}")
    print("\nStories per category:")
    print(df["category"].value_counts())


if __name__ == "__main__":
    main()