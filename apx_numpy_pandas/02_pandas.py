import pandas as pd
import matplotlib.pyplot as plt
# paneled data
# DataFrame
df = pd.read_csv("movies.csv")

# initial data exploration
print(df.head())
print(df.tail())
print(df.sample(5))
print(df.describe())

df["years_since_release"] = 2026 - df["Year"]  # treat a column like a single value
print(df)

print(df[df["Year"] < 2000])

genre_counts = df["Genre"].value_counts()
print(genre_counts)

plt.figure()
genre_counts.plot(kind="pie")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Number of Movies by Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()