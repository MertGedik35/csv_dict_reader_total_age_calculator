# csv_dict_reader_total_age_calculator

`csv.DictReader` kullanarak `people.csv` dosyasından **yaşları okuyup**  
**toplam kişi sayısı** ve **ortalama yaşı** hesaplayan basit bir örnek.

## Dosyalar
- `people.csv` — Örnek veri
- `dict_reader_total_age_calculator.py` — Ortalama yaş hesaplayıcı

## Veri Formatı (people.csv)
```csv
name,age,city
Ali,30,İzmir
Ayşe,27,Ankara
Mehmet,35,Muğla
Çalıştırma
Terminal / PowerShell:

bash
Kodu kopyala
python dict_reader_total_age_calculator.py
Örnek Çıktı
text
Kodu kopyala
Toplam kişi sayısı: 3
Ortalama yaş: 30.67
Kodun Yaptıkları (kısaca)
csv.DictReader ile başlıklara göre okur (name, age, city).

age alanını int'e çevirir; boş/bozuk değerleri atlar (try/except).

total_age ve count tutar, sonunda avg_age = total_age / count.

Windows boş satır sorununa karşı newline="", Türkçe karakterler için encoding="utf-8" kullanır.
Excel’den çıkan dosyalarda BOM varsa utf-8-sig tercih edebilirsin.
