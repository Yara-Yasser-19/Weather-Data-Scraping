# 📺 Televisions Data Scraping & Analysis

<p align="center">
  <img src="https://media.giphy.com/media/xT9IgFbwEwEqA5jSxi/giphy.gif" alt="television gif" width="400"/>
</p>

## 📖 Overview
This project is an automated Python script that scrapes television listings from e-commerce websites. It extracts detailed product specifications and prices, and processes the raw HTML into a clean, structured dataset for market analysis.

## ✨ Features
- **Live Web Scraping:** Extracts real-time television prices and features using `BeautifulSoup4`.
- **Data Wrangling:** Cleans and structures the data into a tabular format with `Pandas`.
- **Data Visualization:** Generates charts comparing TV brands, prices, and sizes using `Matplotlib`.

## 📊 Extracted Data Structure

| Feature | Description | Example |
| :--- | :--- | :--- |
| **Brand** | Television Manufacturer | *Samsung, LG, Sony* |
| **Price** | Current listed price | *$499.99, $1200.00* |
| **Size** | Screen size in inches | *55", 65"* |
| **Resolution** | Display resolution | *4K, 1080p* |

## 🚀 How to Run
```bash
# 1. Install dependencies
pip install requests beautifulsoup4 pandas matplotlib

# 2. Run the script
python 104.py
```
