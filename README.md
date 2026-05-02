Preprocessing — Ember Global Electricity Data
Deskripsi Dataset
Dataset ini berisi data listrik bulanan global dari Ember Climate, mencakup pembangkitan listrik per sumber energi, permintaan listrik, impor neto, dan emisi CO₂ sektor pembangkit. Data tersedia per negara, kawasan, dan blok ekonomi (G7, G20, ASEAN, OECD, EU) dalam long format (satu observasi per baris).

Sumber: Kaggle — Ember Global Electricity Data
Penyedia data asli: Ember Climate
Format file: CSV, long format
Ukuran: 501.483 baris × 18 kolom


Requirements
pandas

Install dengan:
pip install pandas

Cara Menjalankan
GlobalElectricityData.py
Pastikan file monthly_full_release_long_format.csv berada di direktori yang sama dengan GlobalElectricityData.py.

Langkah Preprocessing
1. Membaca CSV
File CSV memiliki format tidak standar — setiap baris dibungkus tanda kutip terluar, dan beberapa nilai field mengandung koma di dalamnya (contoh: "Hydro, Bioenergy and Other Renewables"). Karena itu pd.read_csv() biasa tidak bisa langsung dipakai. File dibaca manual baris per baris, kutip terluar dilepas, lalu di-parse menggunakan csv.reader.

2. Konversi Tipe Data
Seluruh kolom awalnya bertipe str karena proses pembacaan manual. Konversi yang dilakukan:

Date → datetime64
EU, OECD, G20, G7, ASEAN, Value, YoY absolute change, YoY % change → float64

3. Penanganan Missing Values

EU, OECD, G20, G7, ASEAN (55.795) 
Diisi 0 — baris Region/Continent memang tidak punya keanggotaan organisasi

Value (3.292) Dibiarkan
Data emisi CO₂ 2026 memang belum tersedia (provisional)

YoY absolute change (186.705)
Dibiarkan — by design kosong di awal time series

YoY % change (234.044)
Dibiarkan — by design kosong di awal time series

4. Penambahan Kolom Turunan
Dari kolom Date ditambahkan tiga kolom baru untuk keperluan analisis time-series:

Year — tahun
Month — bulan (1–12)
Quarter — kuartal (1–4)


Struktur Output
DataFrame akhir memiliki 21 kolom (18 kolom asli + 3 kolom turunan) dengan tipe data yang sudah sesuai dan siap untuk analisis lebih lanjut.