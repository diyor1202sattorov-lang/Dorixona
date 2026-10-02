nomi = "Paratsetamol"
dozasi = "500 mg"
shakli = "Hap (tabletka)"
narxi = 3000
miqdori = 10

print("Dori nomi:", nomi)
print("Dozasi va shakli:", dozasi, "-", shakli)
print("Narxi:", narxi, "so‘m")
print("Miqdori:", miqdori, "qadoq")


def dori_qoshish(nomi, narxi, miqdori, dozasi="500 mg"):
    print("Yangi dori vositasi qo‘shildi:")
    print("Dori nomi:", nomi)
    print("Dozasi:", dozasi)
    print("Narxi:", narxi, "so‘m")
    print("Miqdori:", miqdori, "qadoq")

# Funksiyani chaqirish:
dori_qoshish("Amoksitsillin", 15000, 30, "250 mg")

def dori_qoldigini_tekshir(nomi, miqdori, minimal_qoldiq=10):
    if miqdori < minimal_qoldiq:
        print(f"⚠️ {nomi} kam qoldi ({miqdori} qadoq)! Zudlik bilan yetkazib beruvchiga buyurtma bering.")
    else:
        print(f"✅ {nomi} zaxirada yetarli ({miqdori} qadoq).")

# Funksiyani chaqirish:
dori_qoldigini_tekshir("Paratsetamol", 5)
dori_qoldigini_tekshir("Nurofen", 25)
