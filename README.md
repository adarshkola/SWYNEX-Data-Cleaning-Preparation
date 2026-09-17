# SWYNEX-Data-Cleaning-Preparation
Data cleaning and preparation project completed as part of my Data Analyst Internship at SWYNEX Technologies.

# Task 1 – Data Cleaning & Preparation
## Project Overview

This project was completed as part of my Data Analyst Internship at SWYNEX Technologies.
The objective of this task was to clean and prepare a messy Air Quality Index (AQI) dataset for further analysis.
The dataset contains air quality information for different cities in India, including PM2.5, PM10, NO2, SO2, CO, O3, AQI, and AQI category.

## Dataset

The raw dataset contained **107 rows and 11 columns**.

It included several data quality issues such as:

* Missing values
* Inconsistent city names
* Different date formats
* CO values containing `ppm`
* Invalid `-999` values in PM10
* Inconsistent AQI category names
* Duplicate records

## Tools Used

* Python
* Pandas
* VS Code

## Files

```text
SWYNEX-Data-Cleaning-Preparation
│
├── raw_data
│   └── india_aqi_raw_messy.csv
│
├── cleaned_data
│   └── india_aqi_cleaned.csv
│
├── clean_data.py
└── README.md
```

## Data Cleaning Steps

### 1. Load the Dataset

Loaded the raw CSV file using Pandas.

### 2. Remove Unnecessary Column

Removed the `S.No` column because it was only a serial number and was not required for analysis.

### 3. Clean City Names

Removed extra spaces and standardized city names using `strip()` and `title()`.

For example:

```text
delhi → Delhi
MUMBAI → Mumbai
Chennai  → Chennai
```

### 4. Standardize Date Format

Converted different date formats into a single standard date format.

### 5. Clean CO Values

Removed `ppm` from CO values and converted the column into numeric format.

### 6. Convert Numeric Columns

Converted the pollutant and AQI columns into numeric data types.

### 7. Handle Invalid Values

The value `-999` in the PM10 column was treated as an invalid value and replaced with a missing value.

### 8. Handle Missing Values

Missing values in numeric columns were filled using the mean of their respective columns.

Missing AQI category values were filled using the most frequent category.

### 9. Standardize AQI Categories

Cleaned extra spaces and standardized the AQI category names.

For example:

```text
SEVERE  → Severe
moderate  → Moderate
GOOD → Good
```

### 10. Remove Duplicate Records

Duplicate records were removed after cleaning the inconsistent values.

### 11. Validate the Dataset

Checked:

* Number of rows and columns
* Missing values
* Duplicate rows
* Data types

### 12. Export Cleaned Dataset

The final cleaned dataset was exported as:

```text
india_aqi_cleaned.csv
```

## Before vs After Cleaning

| Metric         | Before Cleaning | After Cleaning |
| -------------- | --------------: | -------------: |
| Rows           |             107 |            100 |
| Columns        |              11 |             10 |
| Missing Values |              80 |              0 |
| Duplicate Rows |               7 |              0 |

## Final Dataset

The cleaned dataset contains:

* **100 rows**
* **10 columns**
* No missing values
* No duplicate rows
* Correct numeric data types
* Standardized city names
* Standardized dates
* Standardized AQI categories

## Learning Outcome

Through this task, I practiced basic data cleaning and preparation using Python and Pandas.

I learned how to handle missing values, incorrect data types, inconsistent categorical values, invalid values, date formats, and duplicate records before using a dataset for analysis.
