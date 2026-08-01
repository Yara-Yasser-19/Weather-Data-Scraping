
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://forecast.weather.gov/MapClick.php?textField1=38.9072&textField2=-77.0369"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

cards = soup.find(id="seven-day-forecast").find_all(class_="tombstone-container")

data = []
for c in cards:
    day  = c.find(class_="period-name").get_text(strip=True)
    temp = c.find(class_="temp").get_text(strip=True)
    desc = c.find(class_="short-desc").get_text(strip=True)
    data.append([day, temp, desc])

df = pd.DataFrame(data, columns=["day", "temp", "desc"])
df["temp_num"] = df["temp"].str.extract(r"(-?\d+)").astype(int)

print(df)

plt.plot(df["day"], df["temp_num"], marker="o",color="red")
plt.xticks(rotation=45)
plt.title("NWS Forecast Temperatures")
plt.grid(True)
plt.show()
