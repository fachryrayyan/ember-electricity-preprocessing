import pandas as pd
import csv

clean_lines = []
with open("monthly_full_release_long_format.csv", "r") as f:
    for line in f:
        line = line.strip()
        # Lepas kutip terluar
        if line.startswith('"') and line.endswith('"'):
            line = line[1:-1]
        # Ganti double-quote inner jadi placeholder
        line = line.replace('""', '\x00')
        clean_lines.append(line)

rows = []
for line in clean_lines:
    line = line.replace('\x00', '"')  # restore inner quotes
    rows.append(next(csv.reader([line])))

# Menentukan header dan isi
df = pd.DataFrame(rows[1:], columns=rows[0])

# Mengonversi "Date" menjadi tipe data date
df["Date"] = pd.to_datetime(df["Date"])

# Mengubah nilai kolom flag yang menjadi float
numeric_cols = ["EU", "OECD", "G20", "G7", "ASEAN", "Value", "YoY absolute change", "YoY % change"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Mengubah nilai kolom flag yang NaN menjadi 0
flag_cols = ["EU", "OECD", "G20", "G7", "ASEAN"]
df[flag_cols] = df[flag_cols].fillna(0)

# Menambah kolom turunan dari Date
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Quarter"] = df["Date"].dt.quarter

print(df.shape)
print(df.dtypes)
print(df.isnull().sum())