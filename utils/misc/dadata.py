import datetime as dt
import httpx


# Проверка статуса самозанятого по ИНН
def check_status(inn: str, date: dt.date = None) -> dict:
    date = date or dt.date.today()
    date_str = date.isoformat()
    url = "https://statusnpd.nalog.ru/api/v1/tracker/taxpayer_status"
    data = {
        "inn": inn,
        "requestDate": date_str,
    }
    resp = httpx.post(url=url, json=data)
    return resp.json()


#if __name__ == "__main__":
#    response = check_status("027714145906")
#    print(response)