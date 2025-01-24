import json
import re
import pandas as pd

def clean_text(text):
    """
    Metni temizlemek için Unicode karakterlerini ve gereksiz boşlukları kaldırır.
    """
    if text:
        return re.sub(r'\\u[0-9a-fA-F]{4}', '', text).strip()
    return ""

def clean_entry(entry):
    """
    Tek bir JSON nesnesini temizler.
    """
    entry['Title'] = clean_text(entry.get('Title', ''))
    entry['Summary'] = clean_text(entry.get('Summary', ''))
    entry['Body'] = clean_text(entry.get('Body', ''))
    entry['Date'] = entry.get('Date', '').strip()
    entry['Category'] = entry.get('Category', '').strip()
    entry['Language'] = entry.get('Language', '').strip()
    entry['Link'] = entry.get('Link', '').strip()
    return entry

def process_json(input_file, output_file_csv, output_file_json, output_file_language_tr, output_file_language_en, output_file_language_fr, output_file_language_ru, output_file_language_sq, output_file_language_ba, merged_output_file):
    """
    JSON dosyasını temizler ve CSV/JSON formatında çıktılar oluşturur.
    """
    # JSON dosyasını yükle
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Her bir veriyi temizle
    cleaned_data = [clean_entry(item) for item in data]

    # Veriyi CSV dosyasına yaz
    df = pd.DataFrame(cleaned_data)
    df.to_csv(output_file_csv, index=False, encoding='utf-8')

    # Temizlenmiş JSON dosyasını yaz
    with open(output_file_json, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    # "Language: tr" verilerini filtrele ve ayrı dosyaya yaz
    tr_data = [item for item in cleaned_data if item.get('Language') == 'tr']
    with open(output_file_language_tr, 'w', encoding='utf-8') as f:
        json.dump(tr_data, f, ensure_ascii=False, indent=4)

    # "Language: en" verilerini filtrele ve ayrı dosyaya yaz
    en_data = [item for item in cleaned_data if item.get('Language') == 'en']
    with open(output_file_language_en, 'w', encoding='utf-8') as f:
        json.dump(en_data, f, ensure_ascii=False, indent=4)

    # "Language: fr" verilerini filtrele ve ayrı dosyaya yaz
    fr_data = [item for item in cleaned_data if item.get('Language') == 'fr']
    with open(output_file_language_fr, 'w', encoding='utf-8') as f:
        json.dump(fr_data, f, ensure_ascii=False, indent=4)

    # "Language: ru" verilerini filtrele ve ayrı dosyaya yaz
    ru_data = [item for item in cleaned_data if item.get('Language') == 'ru']
    with open(output_file_language_ru, 'w', encoding='utf-8') as f:
        json.dump(ru_data, f, ensure_ascii=False, indent=4)

    # "Language: sq" verilerini filtrele ve ayrı dosyaya yaz
    sq_data = [item for item in cleaned_data if item.get('Language') == 'sq']
    with open(output_file_language_sq, 'w', encoding='utf-8') as f:
        json.dump(sq_data, f, ensure_ascii=False, indent=4)

    # "Language: ba" verilerini filtrele ve ayrı dosyaya yaz
    ba_data = [item for item in cleaned_data if item.get('Language') == 'ba']
    with open(output_file_language_ba, 'w', encoding='utf-8') as f:
        json.dump(ba_data, f, ensure_ascii=False, indent=4)

    # Filtrelenmiş tüm verileri tek bir dosyada birleştir ve ID'ye göre sırala
    merged_data = tr_data + en_data + fr_data + ru_data + sq_data + ba_data
    merged_data_sorted = sorted(merged_data, key=lambda x: x.get('ID', 0))
    with open(merged_output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data_sorted, f, ensure_ascii=False, indent=4)

# Girdi ve çıktı dosyalarının isimlerini belirtin
input_file = 'data.json'  # Temizlenecek JSON dosyası
output_file_csv = 'cleaned_data.csv'  # Çıktı CSV dosyası
output_file_json = 'cleaned_data.json'  # Çıktı JSON dosyası
output_file_language_tr = 'language_tr_data.json'  # Sadece "Language: tr" verileri
output_file_language_en = 'language_en_data.json'  # Sadece "Language: en" verileri
output_file_language_fr = 'language_fr_data.json'  # Sadece "Language: fr" verileri
output_file_language_ru = 'language_ru_data.json'  # Sadece "Language: ru" verileri
output_file_language_sq = 'language_sq_data.json'  # Sadece "Language: sq" verileri
output_file_language_ba = 'language_ba_data.json'  # Sadece "Language: ba" verileri
merged_output_file = 'merged_filtered_data.json'  # Filtrelenmiş tüm veriler birleştirilmiş ve sıralanmış JSON dosyası

# İşlem başlat
process_json(input_file, output_file_csv, output_file_json, output_file_language_tr, output_file_language_en, output_file_language_fr, output_file_language_ru, output_file_language_sq, output_file_language_ba, merged_output_file)
print("Veriler başarıyla temizlendi, ayrıldı, birleştirildi ve ID'ye göre sıralandı. 'merged_filtered_data.json' dosyasına kaydedildi.")
