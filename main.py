import pandas as pd
import matplotlib.pyplot as plt
import os

# Klasör yoksa oluştur
if not os.path.exists("Çıktı"):
    os.makedirs("Çıktı")

# CSV dosyasını oku
df = pd.read_csv("flights.csv")

# Yıla göre toplam uçuş sayısı
if 'year' in df.columns and 'passengers' in df.columns:
    toplam_ucuslar = df.groupby('year')['passengers'].sum()
    print(toplam_ucuslar)

    # En çok uçuş yapılan yıl
    en_yogun_yil = toplam_ucuslar.idxmax()
    max_ucus = toplam_ucuslar.max()
    print(f"En çok uçuş yapılan yıl: {en_yogun_yil} ({max_ucus} uçuş)")

    # Görselleştirme
    toplam_ucuslar.plot(kind='bar', color='skyblue')
    plt.title("Yıllara Göre Toplam Uçuş Sayısı")
    plt.xlabel("Yıl")
    plt.ylabel("Toplam Uçuş")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Kaydet
    plt.savefig("Çıktı/yillik_ucus_sayisi.png")
    plt.show()

else:
    print("Gerekli sütunlar eksik: 'year' ve/veya 'passengers'")
