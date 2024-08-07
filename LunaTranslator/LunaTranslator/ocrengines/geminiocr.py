import base64
import requests
from ocrengines.baseocrclass import baseocr


class OCR(baseocr):
    def ocr(self, imagebinary):
        self.checkempty(["key"])
        self.checkempty(["url"])
        self.checkempty(["model"])
        api_key = self.config["key"]
        url = self.config["url"]
        model = self.config["model"]
        image_data = base64.b64encode(imagebinary).decode("utf-8")

        # Prepare the request payload
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": "Ocr this picture"},
                        {"inlineData": {"mimeType": "image/png", "data": image_data}},
                    ]
                }
            ]
        }

        # Set up the request headers and URL
        headers = {"Content-Type": "application/json"}
        # by default https://generativelanguage.googleapis.com/v1
        url = f"{url}/models/{model}:generateContent?key={api_key}"

        # Send the request
        response = requests.post(url, headers=headers, json=payload, proxies=self.proxy)
        try:
            # Handle the response
            if response.status_code == 200:
                return response.json()["candidates"][0]["content"]["parts"][0]["text"]
            else:
                raise Exception(response.text)
        except Exception as e:
            raise Exception(response.text) from e
