import requests
from bs4 import BeautifulSoup

exclude = ["Chinese", "Japanese"]

def scrape_booster_boxes():
    """
    Illustrative function to scrape booster box names and prices from a given URL.
    This is for educational purposes only and not recommended for PriceCharting.com.
    """
    try:
        text = None
        with open("test.html", "r") as f:
            text = f.read()

        soup = BeautifulSoup(text, 'html.parser')

        # This part is highly dependent on the website's HTML structure.
        # You would need to inspect the HTML of PriceCharting.com to find the correct
        # CSS selectors or tags for the booster box names and prices.
        # The following are *placeholders* and will likely NOT work for PriceCharting.com.
        booster_boxes = []
        # Example of what you might look for (these are hypothetical)
        # Assuming each booster box is in a div with class 'product-item'
        # and inside that, a 'h3' for name and 'span' with class 'price' for price.
        product_containers = soup.find_all('tr')
        for product in product_containers:
            name_tag = product.find('div', class_='console-in-title')
            price_tag = product.find('span', class_='js-price')
            title = product.find('td', class_='title').get_text(strip=True)

            if name_tag and price_tag and "Prerelease" not in title and "Build" not in title and "Half" not in title and:
                name = name_tag.get_text(strip=True)
                price = price_tag.get_text(strip=True)
                add = True
                for excluded in exclude:
                    if excluded in name:
                        add = False
                if add:
                    name = name.split("Pokemon ")[1]
                    booster_boxes.append(f"{name}: {price}")

        return booster_boxes

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    simulated_data = scrape_booster_boxes()
    formatted_lines = []
    max_name_length = 0
    for line in simulated_data:
        parts = line.split(':', 1) # Split only on the first colon
        if len(parts) == 2:
            name = parts[0].strip()
            if len(name) > max_name_length:
                max_name_length = len(name)
    for line in simulated_data:
        parts = line.split(':', 1)
        if len(parts) == 2:
            name = parts[0].strip()
            price = parts[1].strip()
            # Use f-string formatting to left-align the name and then add the price
            formatted_line = f"{name:<{max_name_length}}: {price}"
            formatted_lines.append(formatted_line)
        else:
            # If a line doesn't conform to "Name: Price", just keep it as is
            formatted_lines.append(line)
    output_filename = "pokemon_booster_boxes.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        for item in formatted_lines:
            f.write(item + "\n")

    print(f"Simulated data saved to '{output_filename}'.")
