import os
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Load analysed CSV from local data folder
    input_path = os.path.join("data", "trends_analysed.csv")

    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"{input_path} not found. Run task3_analysis.py first."
        )

    df = pd.read_csv(input_path)

    # Create output folder
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    print("Loaded data:", df.shape)
    print(df.head())

    # Chart 1: Top 10 stories by score
    top_10 = df.nlargest(10, "score").copy()
    top_10["short_title"] = top_10["title"].apply(
        lambda x: x[:50] + "..." if len(x) > 50 else x
    )

    plt.figure(figsize=(12, 6))
    plt.barh(top_10["short_title"], top_10["score"], color="skyblue")
    plt.xlabel("Score")
    plt.ylabel("Title")
    plt.title("Top 10 Stories by Score")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart1_top_stories.png"))
    plt.close()

    # Chart 2: Stories per category
    category_counts = df["category"].value_counts()
    colors = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2"]

    plt.figure(figsize=(8, 5))
    plt.bar(
        category_counts.index,
        category_counts.values,
        color=colors[:len(category_counts)]
    )
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.title("Stories per Category")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart2_categories.png"))
    plt.close()

    # Chart 3: Scatter plot
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    plt.figure(figsize=(8, 6))
    plt.scatter(
        not_popular["score"],
        not_popular["num_comments"],
        color="gray",
        alpha=0.6,
        label="Not Popular"
    )
    plt.scatter(
        popular["score"],
        popular["num_comments"],
        color="red",
        alpha=0.7,
        label="Popular"
    )
    plt.xlabel("Score")
    plt.ylabel("Number of Comments")
    plt.title("Score vs Comments")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "chart3_scatter.png"))
    plt.close()

    print("\nCharts saved successfully in the outputs folder.")


if __name__ == "__main__":
    main()