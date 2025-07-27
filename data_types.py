from pydantic import BaseModel

class anksiyete_input(BaseModel):
    Yas: int
    Cinsiyet: str # 'Erkek' - 'Kadın' - 'Diğer'
    Medeni_Hal: str # 'Evli' - 'Bekar' - 'Dul' - 'Boşanmış'
    Is_Durumu: str  # 'Çalışıyor' - 'Öğrenci' - 'Emekli - 'İşsiz'
    Egitim: str # 'İlkokul' - 'Ortaokul' - 'Lise' - 'Üniversite' - 'Yüksek Lisans+'
    Gelir_Duzeyi: str # 'Düşük' - 'Orta' - 'Yüksek'
    Yasam_Yeri: str # 'Küçük Şehir' - 'Büyükşehir' - 'Kırsal'
    Psikolojik_Destek: str # 'Hayır' - 'Evet'
    Calisma_Suresi: int
    sorular : list # contains 20 items ranging from 0 to 3

class borderline_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str
    Is_Durumu: str
    Egitim: str
    Gelir_Duzeyi: str
    Yasam_Yeri: str
    Psikolojik_Destek: str
    Calisma_Suresi: int
    sorular : list # contains 53 items ranging from 0 to 1

class narsizm_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str
    Is_Durumu: str
    Egitim: str
    Gelir_Duzeyi: str
    Yasam_Yeri: str
    Psikolojik_Destek: str
    Calisma_Suresi: int
    SosyalMedya_Saat: float 
    sorular : list # contains 25 items ranging from 0 to 4 

class sosyal_fobi_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str
    Is_Durumu: str
    Egitim: str
    Gelir_Duzeyi: str
    Yasam_Yeri: str
    Psikolojik_Destek: str
    Calisma_Suresi: int
    SosyalMedya_Saat: float
    Internet_Kullanim_Sikliği: str # 'Nadiren' - 'Günde 1-2 kez' - 'Sık sık' - 'Sürekli'
    Evde_Yalniz_Zaman: float
    Arkadas_Sayisi: int
    sorular : list # contains 45 items ranging from 0 to 4

class alkol_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str
    Is_Durumu: str
    Egitim: str
    Gelir_Duzeyi: str
    Yasam_Yeri: str
    Psikolojik_Destek: str
    Depresyon_Skoru: int # 0-10
    Anksiyete_Skoru: int # 0-10
    Yalnizlik_Duzeyi: str # 'Orta' - 'Yüksek' - 'Düşük'
    Travma_Gecmisi: str # 'Evet' - 'Hayır'
    Madde_Kullanimi: str # 'Hayır' - 'Sigara' - 'Diğer maddeler'
    Ailede_Alkol_Sorunu: str # 'Evet' - 'Hayır'
    Stres_Duzeyi: int # 1-5
    Alkol_Farkindaligi: str # 'Düşük' - 'Orta' - 'Yüksek'
    Tedavi_Erisimi: str # 'Yok' - 'Var'
    Egitim_Programi_Katilim: str # 'Evet' - 'Hayır'
    Calisma_Suresi: int
    sorular : list # contains 34 items ranging from 0 to 3

class beck_depresyon_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str
    Is_Durumu: str
    Egitim: str
    Gelir_Duzeyi: str
    Yasam_Yeri: str
    Psikolojik_Destek: str
    Ailede_Ruhsal_Hastalik: str # 'Evet' - 'Hayır'
    Spor_Sıklığı: str # 'Hiç' - 'Haftada 1-2' - 'Haftada 3-4' - 'Her gün'
    Uyku_Suresi: float
    Kahve_Tuketimi: str # 'Yok' - '1-2 fincan' - '3+ fincan'
    Alkol_Tuketimi: str # 'Hiç' - 'Ara sıra' - 'Sık sık'
    Calisma_Suresi: int
    sorular : list # contains 21 items ranging from 0 to 3