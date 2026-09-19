from lib import check_website_status


def main():
    """
    Головна функція, яка викликає методи з lib.py та виводить результат.
    """
    url = "https://example.com"
    print(f"Перевіряємо статус сайту {url}...")

    status = check_website_status(url)
    print(f"Результат (статус-код): {status}")


if __name__ == "__main__":
    main()