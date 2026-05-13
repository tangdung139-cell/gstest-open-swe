import requests

def login():
    password = "admin123"

    requests.get(
        "https://example.com",
        verify=False
    )

    try:
        x = 1 / 0
    except:
        pass

login()
