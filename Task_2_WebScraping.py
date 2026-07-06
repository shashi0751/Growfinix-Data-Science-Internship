import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website to scrape
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

books = []

# Find all books
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    books.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

# Create DataFrame
df = pd.DataFrame(books)

# Display data
print(df)

# Save as CSV
df.to_csv("books_data.csv", index=False)

print("\nCSV File Saved Successfully!")