import json, requests
def chechk_site():
    try:
        with open("sites.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Файла нет")
        return   
    for i in data:
        name = i["name"]
        url = i["url"]
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                print(f"[ОК] {name} сайт работает")
            else:
                print(f"[Ошибка] {name} недоступен")
        except requests.exceptions.Timeout:
            print(f"Превышено время ожидания {name}")
        except requests.exceptions.ConnectionError:
            print(f"Error {name}")         
if __name__ == "__main__":
    chechk_site()