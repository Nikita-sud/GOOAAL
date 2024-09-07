import requests
import time

def get_ngrok_url():
    time.sleep(2)  # Даем время ngrok для старта
    url = "http://127.0.0.1:4040/api/tunnels"
    try:
        response = requests.get(url)
        data = response.json()
        return data['tunnels'][0]['public_url']
    except Exception as e:
        print(f"Ошибка при получении ngrok URL: {e}")
        return None