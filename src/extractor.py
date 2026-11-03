import httpx

class DataExtractor:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def fetch_posts(self) -> list[dict]:
        """
        Make a synchronous HTTP request to fetch the posts from the API.
        """
        endpoint = f"{self.base_url}/posts"
        
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(endpoint)
                response.raise_for_status()  # Raise an exception if there is an HTTP error (4xx or 5xx)
                return response.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error connecting to the API: {e.response.status_code}")
            raise
        except httpx.RequestError as e:
            print(f"Network or connection error: {e}")
            raise