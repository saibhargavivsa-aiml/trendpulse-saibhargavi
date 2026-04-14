import os
import pandas as pd
import numpy as np


def main():
    # Load trends_clean.csv from local data folder
    input_path = os.path.join("data", "trends_clean.csv")

    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"{input_path} not found. Run task2_data_processing.py first."
        )

    df = pd.read_csv(input_path)
    print("Loaded data shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())

    # Numpy analysis
    scores = df["score"].to_numpy()
    comments = df["num_comments"].to_numpy()

    mean_score = np.mean(scores)
    median_score = np.median(scores)
    std_score = np.std(scores)

    highest_score = np.max(scores)
    lowest_score = np.min(scores)

    top_category = df["category"].value_counts().idxmax()

    most_comments_index = np.argmax(comments)
    most_commented_title = df.iloc[most_comments_index]["title"]
    most_commented_count = df.iloc[most_comments_index]["num_comments"]

    print("\nNumpy analysis:")
    print("Mean score:", mean_score)
    print("Median score:", median_score)
    print("Standard deviation of score:", std_score)
    print("Highest score:", highest_score)
    print("Lowest score:", lowest_score)
    print("Category with most stories:", top_category)
    print("Story with most comments:", most_commented_title)
    print("Comment count:", most_commented_count)

    # Add two columns
    df["engagement"] = df["num_comments"] / (df["score"] + 1)
    average_score = mean_score
    df["is_popular"] = df["score"] > average_score

    print("\nSample of new columns:")
    print(df[["score", "num_comments", "engagement", "is_popular"]].head())

    # Save analysed CSV locally
    output_path = os.path.join("data", "trends_analysed.csv")
    df.to_csv(output_path, index=False)

    print(
        f"\nSaved analysed data with {df.shape[0]} rows and {df.shape[1]} "
        f"columns to {output_path}"
    )


if __name__ == "__main__":
    main()