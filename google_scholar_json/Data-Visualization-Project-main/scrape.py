import requests

payload = { 'api_key': '94d592876699bf5cf4b696661a5420be', 'url': 'https://scholar.google.com/citations?user=S2tBrxcAAAAJ&hl=en&oi=ao', 'follow_redirect': 'false', 'retry_404': 'true', 'autoparse': 'true', 'country_code': 'us', 'device_type': 'desktop', 'max_cost': '0' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
