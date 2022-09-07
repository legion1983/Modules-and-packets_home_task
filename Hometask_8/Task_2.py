import requests
from pprint import pprint
# from ya_disk import YandexDisk
# -----------------------------------task_1_get_from_yandex--------------------------------------
TOKEN = "AQAAAAAAGUQeAADLW859Tk4gikBEmkURmI0u8H0"
class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }
    def get_files_list(self):
        files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()


if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    pprint(ya.get_files_list())
