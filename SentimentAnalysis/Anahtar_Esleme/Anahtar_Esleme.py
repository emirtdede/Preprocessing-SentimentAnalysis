import json
import re

# Durum kategorileri
categories = {
    "0": "Nötr",
    "1": "Çevre Sorunları",
    "2": "Eğitim ve Kültür Sorunları",
    "3": "Siyasi Çatışmalar",
    "4": "Toplumsal Sorunlar",
    "5": "Ekonomik Kriz",
    "6": "Halk Sağlığı Krizleri",
    "7": "Kaza Haberleri",
    "8": "Suç Olayları",
    "9": "Doğal Afetler",
    "10": "Savaş ve Şiddet"
}

# Örnek haberlerin kategorize edilmesi için anahtar kelimeler
category_keywords = {
    "Çevre Sorunları": ["hava kirliliği", "doğa tahribatı", "pislik", "kirlilik", "kir"],
    "Eğitim ve Kültür Sorunları": ["eğitim", "okul", "kültür", "öğrenciler", "müfredat"],
    "Siyasi Çatışmalar": ["siyasi", "hükümet", "protesto", "çatışma", "seçim", "parti", "darbe", "amerika", "rusya", "çin"],
    "Toplumsal Sorunlar": ["toplum", "yoksulluk", "işsizlik", "eşitsizlik", "kadın hakları"],
    "Ekonomik Kriz": ["ekonomi", "kriz", "işsizlik", "pahalılık", "enflasyon", "borç"],
    "Halk Sağlığı Krizleri": ["sağlık", "pandemi", "hastalık", "aşı", "kriz", "virüs", "sağlık sistemi"],
    "Kaza Haberleri": ["kaza", "trafik kazası", "kaza", "araba çarpması", "trafik kazası"],
    "Suç Olayları": ["suç", "hırsızlık", "cinayet", "soygun", "kaçakçılık", "mafya", "cinsel", "istismar", "suikast"],
    "Doğal Afetler": ["deprem", "sel", "tsunami", "yangın", "doğal afet", "fırtına"],
    "Savaş ve Şiddet": ["savaş", "çatışma", "bombalama", "terör", "şiddet", "askeri operasyon"]
}

# 'data.json' dosyasını okuma
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Haber metnini analiz etme ve durum kategorisini atama
for news_item in data:
    body = news_item.get("Body", "").lower()  # 'Body' metnini al, küçük harfe çevir
    
    # Durum başlangıçta nötr (0) olarak atanır
    news_item["Durum"] = "0"
    
    # Her kategori için anahtar kelimeleri kontrol et
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', body):  # Anahtar kelimenin tam eşleşmesi
                news_item["Durum"] = [key for key, value in categories.items() if value == category][0]
                break
    
# Güncellenmiş veriyi kaydetme
with open("updated_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Durum kategorileri başarıyla güncellendi.")
