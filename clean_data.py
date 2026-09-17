import pandas as pd

# 1. Load raw data
df = pd.read_csv(r"C:\Users\adars\OneDrive\Desktop\SWYNEX-Data-Cleaning-Preparation\raw_data\india_aqi_raw_messy (1).csv")

print("Original Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# 2. Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 3. Remove unnecessary S.No column
df = df.drop(columns=["S.No"])

# 4. Clean City names
df["City"] = df["City"].str.strip().str.title()

# 5. Convert Date into one standard format
def clean_date(value):
    value = str(value).strip()

    if value[:4].isdigit() and value[4] == "-":
        return pd.to_datetime(value, format="%Y-%m-%d")

    if "/" in value:
        first, second, year = value.split("/")

        if int(first) > 12:
            return pd.to_datetime(value, format="%d/%m/%Y")
        else:
            return pd.to_datetime(value, format="%m/%d/%Y")

    return pd.to_datetime(value, format="%d-%m-%Y")


df["Date"] = df["Date"].apply(clean_date)

# 6. Clean CO column
df["CO"] = df["CO"].astype(str).str.replace(" ppm", "", regex=False)
df["CO"] = pd.to_numeric(df["CO"], errors="coerce")

# 7. Convert numeric columns
numeric_columns = [
    "PM2.5",
    "PM10",
    "NO2",
    "SO2",
    "CO",
    "O3",
    "AQI"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df["PM10"] = pd.to_numeric(df["PM10"], errors="coerce")

# 8. Replace invalid PM10 values
df["PM10"] = df["PM10"].replace(-999, float("nan"))

# 9. Fill missing numeric values with column mean
numeric_columns = [
    "PM2.5",
    "PM10",
    "NO2",
    "SO2",
    "CO",
    "O3",
    "AQI"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# 10. Clean AQI Bucket values
df["AQI_Bucket"] = df["AQI_Bucket"].str.strip().str.title()

# 11. Fill missing AQI Bucket with most common value
df["AQI_Bucket"] = df["AQI_Bucket"].fillna(
    df["AQI_Bucket"].mode()[0]
)

# 12. Remove duplicate rows
df = df.drop_duplicates()

# 13. Reset index
df = df.reset_index(drop=True)

# 14. Validate cleaned data
print("\nShape after cleaning:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

# 15. Save cleaned dataset
df.to_csv("india_aqi_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")