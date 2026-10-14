import json, urllib.parse
from datetime import datetime, timedelta
import scraper as s

now = datetime.now(s.TZ)
for details in ("false", "true"):
    params = {
        "lang": "de", "arrival": "true", "offset": 0,
        "codeshare": "true", "count": 100,
        "flightStartTime": (now - timedelta(hours=4)).replace(microsecond=0).isoformat(),
        "flightEndTime": (now + timedelta(hours=6)).replace(microsecond=0).isoformat(),
        "showDetails": details,
    }
    data = s.get_json(s.API_URL + "?" + urllib.parse.urlencode(params))
    n = 0
    for fl in data["flights"]:
        if "annull" in json.dumps(fl, ensure_ascii=False).lower() and n < 2:
            n += 1
            print("=== showDetails =", details)
            print(json.dumps(fl, ensure_ascii=False, indent=1))