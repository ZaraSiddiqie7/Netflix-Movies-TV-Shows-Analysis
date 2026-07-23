import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

# Convert date column
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Standardize column names
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

# Save cleaned dataset
df.to_csv("cleaned_netflix_titles.csv", index=False)

print("Cleaned Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nCleaning Completed!")