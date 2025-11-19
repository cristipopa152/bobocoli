from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as gadhsdj:
    gadhsdj.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    gadhsdj.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    url = "https://www.twitch.tv/brutalles"
    gadhsdj.uc_open_with_reconnect(url, 5)
    gadhsdj.sleep(14)
    if gadhsdj.is_element_present("#live-channel-stream-information"):

        if gadhsdj.is_element_present('button:contains("Accept")'):
            gadhsdj.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            gadhsdj.uc_open_with_reconnect(url, 5)
            gadhsdj2 = gadhsdj.get_new_driver(undetectable=True)
            gadhsdj2.uc_open_with_reconnect(url, 5)
            gadhsdj.sleep(10)
            if gadhsdj2.is_element_present('button:contains("Accept")'):
                gadhsdj2.uc_click('button:contains("Accept")', reconnect_time=4)
            while gadhsdj2.is_element_present("#live-channel-stream-information"):
                gadhsdj2.sleep(1)
            gadhsdj.quit_extra_driver()
    gadhsdj.sleep(1)
