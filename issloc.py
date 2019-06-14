#!/usr/bin/env python3

import requests
iss =  requests.get("http://api.open-notify.org/iss-now.json").json()
print(iss)
