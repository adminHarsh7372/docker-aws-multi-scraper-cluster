import requests, os, re, json

url = "https://www.wikipedia.org"
print(f"[scraper2] Fetching: {url}")

try:
    r = requests.get(url, timeout=10, headers={"User-Agent": "Scraper2/1.0"})
    title_match = re.search(r"<title>(.*?)</title>", r.text, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "No title found"
except Exception as e:
    title = f"Error: {e}"

os.makedirs("/data/results", exist_ok=True)
with open("/data/results/scraper-2.json", "w") as f:
    json.dump({"url": url, "title": title}, f, indent=2)

print(f"[scraper-2] Done! Title: {title}")
