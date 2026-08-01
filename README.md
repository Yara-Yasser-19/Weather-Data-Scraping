# 🌤️ Weather Data Scraping & Analysis

<p align="center">
  <img src="https://media.giphy.com/media/2Faz2uP9LzF0I53YQ/giphy.gif" alt="weather gif" width="400"/>
</p>

## 📖 Overview
This project is an automated Python script that scrapes the 7-day weather forecast directly from the National Weather Service (NWS) website. It processes the raw HTML into a clean, structured dataset and visualizes the upcoming temperature trends.

## ✨ Features
- **Live Web Scraping:** Extracts real-time weather data using `BeautifulSoup4`.
- **Data Wrangling:** Cleans and structures the data into a tabular format with `Pandas`.
- **Data Visualization:** Generates a line chart of the temperature trend over the week using `Matplotlib`.

## 📊 Extracted Data Structure

| Feature | Description | Example |
| :--- | :--- | :--- |
| **Day** | The day or period of the forecast | *Tonight, Monday, Monday Night* |
| **Temperature** | High or Low temperature | *High: 85 °F, Low: 65 °F* |
| **Description** | Short weather condition summary | *Slight Chance Rain, Sunny* |
| **Temp_Num** | Extracted numerical temperature | *85, 65* |

## 🚀 How to Run
```bash
# 1. Install dependencies
pip install requests beautifulsoup4 pandas matplotlib

# 2. Run the script
python 104.py
```
