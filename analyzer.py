import requests

def fetch_headers(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    try:
        response = requests.get ( 
            url,
            timeout=10,
            allow_redirects=True,
            headers= {
                "User-Agent": "Wolfheaders/1.0"
                },
        )

        return {
            "url": response.url,
            "status": response.status_code,
            "headers": response.headers,
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Unable to connect: {e}")
                