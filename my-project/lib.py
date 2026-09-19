import requests


def check_website_status(url):
    """
    Робить GET-запит до вказаного URL та повертає статус-код.
    """
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Помилка: {e}"