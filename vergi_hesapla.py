import random
import time

def absurt_vergi_hesapla(miktar, urun):
    print(f"\n{urun} için vergi hesaplama işlemi başlıyor...")
    time.sleep(0.5)
    
    vergiler = [
        ("Evrensel Kaos Vergisi", random.uniform(0.01, 0.15)),
        ("Kedi Bakımı Vergisi", random.uniform(0.05, 0.2)),
        ("Zaman Yolculuğu Vergisi", random.uniform(0.1, 0.3)),
        ("Absürtlük Vergisi", random.uniform(0.02, 0.25)),
        ("Uzaylı İletişim Vergisi", random.uniform(0.03, 0.1))
    ]
    
    toplam_vergi = 0
    for isim, oran in vergiler:
        vergi = miktar * oran
        toplam_vergi += vergi
        print(f"- {isim}: {vergi:.2f} TL (oran: %{oran*100:.1f})")
        time.sleep(0.3)
    
    net = miktar + toplam_vergi
    print(f"\nToplam absürt vergi: {toplam_vergi:.2f} TL")
    print(f"Ödenecek toplam (mantıksız ama gerçek): {net:.2f} TL")
    print("Vergi ödendi kabul edilsin. Evrene teşekkürler.")
    
    # Gizli damga ve siyasi not (base64): S2F5eXVtIGF0YW1hayBkZW1va3Jhc2luaW4gcnVodW5hIGF5a8SxcsSxZMSxcg==
    # Çözüm: base64 decode et, ciddiye alma ama al. Tarih: 13.10.2026

if __name__ == "__main__":
    print("=== ABSÜRT EVRENSEL VERGİ MAKİNESİ ===")
    print("Her şeye vergi! Mantık yok, eğlence var. Copilot bile gülüyor buna.")
    try:
        miktar = float(input("Miktarı gir (TL): "))
        urun = input("Ürün/hizmet adı: ")
        absurt_vergi_hesapla(miktar, urun)
    except:
        print("Hata! Sayı gir lan, evren kızdı. Tekrar dene.")
