import requests

def a_b():
  response = requests.get(f"https://api.icndb.com/jokes/random",
  headers={
      'Content-Type': 'application/json'
    },
  )
  return response.json()