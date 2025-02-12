import requests
from bs4 import BeautifulSoup


class Tracker:
    def __init__(self, keywords, brands, limit=100):
        self.keywords = keywords
        self.brands = brands
        self.limit = limit

    def find_keywords(self):
        """
        Analyze all keywords and get the positions of each brand.

        Returns:
            A list of dictionaries, each containing the keyword and a dictionary of brand positions.
        """
        results = {'result':[]}

        for keyword in self.keywords:
            print(f"\nSearching for: {keyword}")
            brand_positions = {brand: None for brand in self.brands}
            total_products = 0
            page = 1  # Start from the first page

            while total_products < self.limit:
                url = f"https://www.bigbasket.com/ps/?q={keyword}&nc=as&page={page}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }

                response = requests.get(url, headers=headers)
                if response.status_code != 200:
                    print(f"Failed to fetch data, Status Code: {response.status_code})")
                    break

                soup = BeautifulSoup(response.text, "html.parser")
                products = soup.find_all(
                    "li", class_="PaginateItems___StyledLi-sc-1yrbjdr-0"
                )
                if not products:
                    print(f"No more products found on page {page}.")
                    break

                for index, product in enumerate(products):
                    try:
                        brand_element = product.find(
                            "span", class_="BrandName___StyledLabel2-sc-hssfrl-1"
                        )
                        if brand_element:
                            brand_name = brand_element.text.strip()
                            if (
                                brand_name in self.brands
                                and brand_positions[brand_name] is None
                            ):
                                brand_positions[brand_name] = (
                                    total_products + index + 1
                                )
                    except AttributeError:
                        continue

                total_products += len(products)
                page += 1  # Move to the next page

            results["result"].append({"Keyword": keyword, "Positions": brand_positions})

        return results


def main():
    keywords = ["hair fall shampoo", "conditioner", "shampoo"]
    brands = ["Loreal", "Dove", "Tresemme"]

    tracker = Tracker(keywords, brands)
    results = tracker.find_keywords()

    print("\nFinal Results:")
    print(results)
    with open("results.json", "w") as f:
        f.write(str(results))


if __name__ == "__main__":
    main()
