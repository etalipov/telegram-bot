import json
import requests
from time import sleep
from base64 import b64decode

import mysecrets


class Text2ImageAPI:
    _url: str = "https://api-key.fusionbrain.ai/"
    _auth_headers: dict

    def __init__(self, api_key: str, secret_key: str):
        self._auth_headers = {
            "X-Key": f"Key {api_key}",
            "X-Secret": f"Secret {secret_key}",
        }

    def get_model(self) -> str:
        response = requests.get(
            f"{self._url}key/api/v1/models", headers=self._auth_headers
        )
        data = response.json()
        return data[0]["id"]

    def generate(
        self,
        prompt: str,
        model: str,
        images: int = 1,
        width: int = 1024,
        height: int = 1024,
    ) -> str:
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {"query": prompt},
        }

        data = {
            "model_id": (None, model),
            "params": (None, json.dumps(params), "application/json"),
        }
        response = requests.post(
            f"{self._url}key/api/v1/text2image/run",
            headers=self._auth_headers,
            files=data,
        )
        data = response.json()

        return data["uuid"]

    def check_generation(
        self, request_id: str, attempts: int = 10, delay: int = 10
    ) -> str | None:
        while attempts > 0:
            response = requests.get(
                f"{self._url}key/api/v1/text2image/status/" + request_id,
                headers=self._auth_headers,
            )
            data = response.json()
            if data["status"] == "DONE":
                return data["images"]

            attempts -= 1
            sleep(delay)


def generate_image(query: str) -> bool:
    api = Text2ImageAPI(mysecrets.KANDINSKIY_API_KEY, mysecrets.KANDINSKIY_SECRET_KEY)
    uuid = api.generate(query, api.get_model())
    images = api.check_generation(uuid)

    if images is None:
        return False

    with open("Picture.png", "wb") as f:
        f.write(b64decode(images[0]))

    return True
