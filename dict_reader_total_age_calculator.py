import csv

total_age = 0 
count = 0

with open("people.csv","r",encoding="utf-8",newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        try:
            age = int(row["age"])

        except (ValueError,TypeError):
            continue

        total_age += age
        count += 1

avg_age = total_age / count if count else 0

print(f"Toplam kişi sayısı: {count}\nOrtalama yaş: {round(avg_age,2)}")