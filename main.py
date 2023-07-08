import requests

startHorizon, endHorizon = "2023-10-08", "2024-12-31"
URL = f"https://calendar-api.fxstreet.com/en/api/v1/eventDates/{startHorizon}T00:00:00Z/{endHorizon}T23:59:59Z" \
      f"?&volatilities=NONE" \
      f"&volatilities=LOW" \
      f"&volatilities=MEDIUM" \
      f"&volatilities=HIGH" \
      f"&countries=US&countries=UK&countries=EMU&countries=DE&countries=CN&countries=JP&countries=CA&countries=AU" \
      f"&countries=NZ&countries=CH&countries=FR&countries=IT&countries=ES&countries=UA" \
      f"&categories=8896AA26-A50C-4F8B-AA11-8B3FCCDA1DFD" \
      f"&categories=FA6570F6-E494-4563-A363-00D0F2ABEC37" \
      f"&categories=C94405B5-5F85-4397-AB11-002A481C4B92" \
      f"&categories=E229C890-80FC-40F3-B6F4-B658F3A02635" \
      f"&categories=24127F3B-EDCE-4DC4-AFDF-0B3BD8A964BE" \
      f"&categories=DD332FD3-6996-41BE-8C41-33F277074FA7" \
      f"&categories=7DFAEF86-C3FE-4E76-9421-8958CC2F9A0D" \
      f"&categories=1E06A304-FAC6-440C-9CED-9225A6277A55" \
      f"&categories=33303F5E-1E3C-4016-AB2D-AC87E98F57CA" \
      f"&categories=9C4A731A-D993-4D55-89F3-DC707CC1D596" \
      f"&categories=91DA97BD-D94A-4CE8-A02B-B96EE2944E4C" \
      f"&categories=E9E957EC-2927-4A77-AE0C-F5E4B5807C16"

r = requests.get(url=URL)