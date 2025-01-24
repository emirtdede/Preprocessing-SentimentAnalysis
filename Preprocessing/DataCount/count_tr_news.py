import json

# JSON dosyasının adı
json_file = "language_tr_data.json"

# Türkçe haber sayısını bulma
try:
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        turkish_news_count = sum(1 for item in data if item.get("Language") == "tr")
    print(f"Türkçe haber sayısı: {turkish_news_count}")
except Exception as e:
    print(f"Hata oluştu: {e}")
