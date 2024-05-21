import requests

def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        data = response.json()
        return {"setup": data[0]["setup"], "punchline": data[0]["punchline"]}
    else:
        return {"error": "Failed to fetch joke"}

if __name__ == "__main__":
    joke = get_random_joke()
    if "error" in joke:
        print(joke["error"])
    else:
        print(f"Setup: {joke['setup']}")
        print(f"Punchline: {joke['punchline']}")
