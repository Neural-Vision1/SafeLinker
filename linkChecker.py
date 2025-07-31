import re
import requests
import json

print("Paste your text (it can have multiple links):")
text = input()

pattern = r'(https?://[^\s]+|www\.[^\s]+)'
links = re.findall(pattern, text)


API_KEY = 'YOUR_API_KEY_HERE'
url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

if links:
    print("\nLinks found and their safety status:\n")
    for link in links:
    
        body = {
            "client": {
                "clientId": "yourcompanyname",
                "clientVersion": "1.0"
            },
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [
                    {"url": link}
                ]
            }
        }

        try:
            response = requests.post(url, json=body)
            result = response.json()

            if "matches" in result:
                print(f"⚠️  {link} → UNSAFE (Malware or Phishing detected)")
            else:
                print(f"✅ {link} → Safe")
        except Exception as e:
            print(f"❌ Error checking {link}: {str(e)}")
else:
    print("No links found.")