import requests, os, re, json

url = "https://www.python.org"
print(f"[scraper3] Fetching: {url}")

try:
    r = requests.get(url, timeout=10, headers={"User-Agent": "Scraper3/1.0"})
    title_match = re.search(r"<title>(.*?)</title>", r.text, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "No title found"
except Exception as e:
    title = f"Error: {e}"

os.makedirs("/data/results", exist_ok=True)
with open("/data/results/scraper3.json", "w") as f:
    json.dump({"url": url, "title": title}, f, indent=2)

print(f"[scraper3] Done! Title: {title}")
