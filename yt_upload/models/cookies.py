import json

from pydantic import BaseModel, ConfigDict, ValidationInfo
from pydantic import field_validator, model_serializer

from ..typing import YT_COOKIES


class Cookies(BaseModel):
    cookies: YT_COOKIES
    
    model_config = ConfigDict(validate_assignment=True)

    @field_validator("cookies")
    @classmethod
    def validate_cookies(cls, cookies: YT_COOKIES, info: ValidationInfo)\
            -> YT_COOKIES:
        if cookies is None:
            with open(info.data['cookies_path'], encoding="utf-8") as f:
                cookies = json.loads(f.read())

        for cookie in cookies:
            if cookie["sameSite"] in ["unspecified", "no_restriction"]:
                cookie["sameSite"] = "None"
            elif cookie["sameSite"] == "lax":
                cookie["sameSite"] = "Lax"
            elif cookie["sameSite"] == "strict":
                cookie["sameSite"] = "Strict"
        
        return cookies

    @model_serializer()
    def serialize_model(self):
        return self.cookies

    def update_cookies(self, cookies: YT_COOKIES) -> None:
        for old_cookie in self.cookies:
            for new_cookie in cookies:
                if new_cookie['name'] == old_cookie['name']:
                    if 'hostOnly' in old_cookie:
                        new_cookie['hostOnly'] = old_cookie['hostOnly']
                    if 'storeId' in old_cookie:
                        new_cookie['storeId'] = old_cookie['storeId']
                    if 'session' in old_cookie:
                        new_cookie['session'] = old_cookie['session']
    
                    break
        
        self.cookies = cookies
    
    def save_cookies(self, path: str) -> None:
        with open(path, "w+", encoding="utf-8") as f:
            f.write(self.model_dump_json(indent=4))
