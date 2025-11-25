import requests


class Brewery:
    def __init__(
        self,
        brewery_id: str,
        name: str,
        brewery_type: str,
        city: str,
        state: str,
        country: str,
        website_url: str,
    ) -> None:
        self.id = brewery_id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.website_url = website_url

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.brewery_type}) - "
            f"{self.city}, {self.state}, {self.country}. "
            f"Strona: {self.website_url}"
        )


response = requests.get(
    "https://api.openbrewerydb.org/v1/breweries?per_page=20"
)
data = response.json()

breweries = [
    Brewery(
        brewery_id=item.get("id"),
        name=item.get("name"),
        brewery_type=item.get("brewery_type"),
        city=item.get("city"),
        state=item.get("state"),
        country=item.get("country"),
        website_url=item.get("website_url"),
    )
    for item in data
]

for brewery in breweries:
    print(brewery)
