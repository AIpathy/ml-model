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

class kayip_yas_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str
    Is_Durumu: str
    Egitim: str
    Gelir_Duzeyi: str
    Yasam_Yeri: str
    Psikolojik_Destek: str
    Calisma_Suresi_Ay: int
    Kayıp_Turu: str # 'Olum' - 'Bosanma' - 'Ayrilik' - 'Olum disi Ayrilik'
    Kayip_Surei_Ay: int
    Aile_Destegi: str # 'Yetersiz' - 'Orta' - 'Yuksek'
    Arkadas_Destegi: str # 'Yetersiz' - 'Orta' - 'Yuksek'
    Fiziksel_Saglik_Sorunu: str # 'Evet' - 'Hayır'
    Uyku_Kalitesi: float # 0-10
    Yasam_Doyumu: float # 0-10
    Gunluk_Stres: float # 0-10
    Disadonukluk: int # 1-5
    Nevrotiklik: int # 1-5
    sorular : list # contains 35 items ranging from 0 to 5

class travma_input(BaseModel):
    Yaş: int
    Cinsiyet: str
    Medeni_Hal: str
    İş_Durumu: str
    Eğitim: str
    Gelir_Düzeyi: str
    Yaşam_Yeri: str
    Psikolojik_Destek: str
    Çalışma_Süresi_Ay: int
    Kayıp_Türü: str # 'Ölum' - 'Boşanma' - 'Ayrılık' - 'Ölüm dışı Ayrılık'
    Kayıp_Sürei_Ay: int
    Travma_Şiddeti: float # 0-10
    Travma_Yıl_Önce: float
    Tedavi_Türü: str # 'Bireysel Terapi' - 'Grup Terapisi' - 'İlaç Tedavisi' - 'Diğer'
    Aile_Desteği: str # 'Yetersiz' - 'Orta' - 'Yüksek'
    Arkadaş_Desteği: str # 'Yetersiz' - 'Orta' - 'Yüksek'
    Fiziksel_Sağlık_Sorunu: str # 'Evet' - 'Hayır'
    Kronik_Hastalık: str # 'Evet' - 'Hayır'
    Uyku_Kalitesi: float # 0-10
    Yaşam_Doyumu: float # 0-10
    Günlük_Stres: float # 0-10
    Stres_Yönetimi: float # 0-10
    Anksiyete: float # 0-10 [kullanıcı anksiyete testini doldurmuşsa risk grubuna göre puanlanır]
    Depresyon: float # 0-10 [aynı şeklilde]
    Sosyal_Aktivite_Sıklığı: str # 'Nadiren' - 'Ara sıra' - 'Sık sık'
    Disadönüklük: int # 1-5
    Nevrotiklik: int # 1-5
    Mükemmeliyetçilik: int # 1-5
    Dayanıklılık: float # 0-10
    sorular : list # contains 36 items ranging from 1 to 5

class cocuk_terkedilme_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Aile_Tipi: str # 'Çekirdek' - 'Geniş' - 'Tek Ebeveyn'
    Anne_Çalışıyor: str # 'Evet' - 'Hayır'
    Baba_Çalışıyor: str # 'Evet' - 'Hayır'
    Anne_Eğitim: str # 'İlkokul' - 'Ortaokul' - 'Lise' - 'Üniversite' - 'Yüksek Lisans'
    Baba_Eğitim: str # same as above
    Ebeveyn_Ayrı: str # 'Evet' - 'Hayır'
    Bölge: str # 'Akdeniz' - 'Ege' - 'Marmara' - 'İç Anadolu' - 'Karadeniz' - 'Güneydoğu Anadolu' - 'Doğu Anadolu'
    Kardeş_Sayısı: int
    Okul_Türü: str # 'Devlet' - 'Özel' - 'Kolej'
    Yaşadığı_Kişi: str # 'Anne ve Baba' - 'Sadece Anne' - 'Sadece Baba' - 'Büyükanne/Büyükbaba' - 'Koruyucu Aile'
    Psikiyatrik_Tanı: str # 'Var' - 'Yok'
    Mahalle_Tipi: str # 'Tehlikeli' - 'Orta' - 'Güvenli'
    Gelişimsel_Sorun: str # 'Var' - 'Yok'
    Ekran_Süresi_Saat: float 
    Ebeveynle_Zaman: str # 'Yetersiz' - 'Orta' - 'Yeterli'
    Duygusal_İhmal: str # 'Var' - 'Yok'
    Psikolojik_Danışman: str # 'Var' - 'Yok'
    Kaygı: float # 0-10
    Uyku_Kalitesi: float # 0-10
    Sosyal_Destek: str # 'Düşük' - 'Orta' - 'Yüksek'
    Travma: float # 'Var' - 'Yok'
    sorular: list # contains 14 items ranging from 1 to 4

class coklu_zeka_input(BaseModel):
    Yaş: int
    Cinsiyet: str
    Eğitim: str # 'İlköğretim' - 'Lise' - 'Üniversite' - 'Yüksek Lisans'
    Meslek: str # 'Öğretmen', 'Diğer', 'Öğrenci', 'Akademisyen', 'Serbest Meslek', 'Mühendis', 'Sanatçı'
    Öğrenci_mi: str # 'Evet' - 'Hayır'
    Sanatsal_Etkinlik_Katılımı: str # 'Evet' - 'Hayır'
    Ailede_Müzikal_Biri_Var_Mı: str # 'Evet' - 'Hayır'
    Günlük_Fiziksel_Aktivite_Süresi: float 
    Yabancı_Dil_Seviyesi: str # 'Temel' - 'Orta' - 'İleri'
    Yaşam_Yeri: str # 'Küçük Şehir' - 'Büyükşehir' - 'Kırsal'
    Müzik_Dinleme_Süresi: float
    Ailede_Eğitim_Düzeyi: str # 'İlk' - 'Orta' - 'Lise' - 'Üniversite' - 'Yüksek Lisans+'
    Kardeş_Sayısı: int
    Psikolojik_Destek_Geçmişi: str # 'Evet' - 'Hayır'
    Günlük_Ekran_Süresi: float
    sorular: list # contains 80 items ranging from 1 to 5
    Sözel_Dilsel_Skoru: int
    Mantıksal_Matematik_Skoru: int
    Görsel_Mekansal_Skoru: int
    Bedensel_Kinestetik_Skoru: int
    Müziksel_Ritmik_Skoru: int
    Kişilerarası_Skoru: int
    İçsel_Skoru: int
    Doğasal_Skoru: int
    Puan_ortalaması: int

class dehb_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Egitim: str # 'Ilkokul' - 'Lise' - 'Universite' - 'Yuksek Lisans' - 'Doktora'
    Is_Durumu: str # 'Çalışıyor' - 'Öğrenci' - 'İşsiz'
    Medeni_Hal: str # 'Evli' - 'Bekar' - 'Boşanmış'
    Ekran_Suresi_Gun: float 
    Fiziksel_Aktivite: str # 'Hiç' - '1-2 gün' '3+ gün'
    Sigara_Alkol_Kullanimi: str # 'Yok' - 'Var'
    Cocukluk_Tanisi: str # 'Evet' - 'Hayır'
    Ailede_DEHB: str # 'Evet' - 'Hayır'
    Ailede_Ruhsal_Hastalik: str # 'Evet' - 'Hayır'
    Anksiyete_Tanisi: str # 'Evet' - 'Hayır'
    Depresyon_Tanisi: str # 'Evet' - 'Hayır'
    Tedavi_Gecmisi: str # 'Evet' - 'Hayır'
    Kardes_Sayisi: int
    Dogum_Sirasi: int
    Unutkanlik_Düzeyi: int # 1-5
    Görev_Bitirme_Zorluğu: int # 1-5
    Kafein_Tuketimi: str # 'Az' - 'Orta' - 'Fazla'
    sorular : list # contains 36 items ranging from 0 to 5

class ofke_sim_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Eğitim: str # 'Ilkokul' - 'Lise' - 'Universite' - 'Yuksek Lisans' - 'Doktora'
    Gelir: str # 'Düşük' - 'Orta' - 'Yüksek'
    Medeni_Durum: str # 'Evli' - 'Bekar' - 'Boşanmış'
    Yaşam_Yeri: str # 'Küçük Şehir' - 'Metropol' - 'Kırsal'
    İş_Durumu: str # 'Çalışıyor' - 'Öğrenci' - 'İşsiz' - 'Emekli'
    Psikolojik_Destek: str # 'Var' - 'Yok'
    Ailede_Psik_Hastalik: str # 'Var' - 'Yok'
    Nevrotiklik: float # 1-5
    Mükemmeliyetçilik: float # 1-5
    Günlük_Stres: float # 0-10
    Fiziksel_Sağlık_Sorunu: str # 'Var' - 'Yok'
    Uyku_Kalitesi: float # 0-10
    Anksiyete: float # 0-10
    Depresyon: float # 0-10
    Sosyal_Destek: str # 'Düşük' - 'Orta' - 'Yüksek'
    Alkol_Madde_Kullanımı: str # 'Var' - 'Yok'
    Fiziksel_Aktivite: str # 'Hiç' - 'Ara sıra' - 'Düzenli'
    Teknoloji_Süresi_Saat: float 
    Hobi_Sosyal_Aktivite: str # 'Düşük' - 'Orta' - 'Yüksek'
    Dini_İnanç: str # 'Zayıf' - 'Orta' - 'Güçlü'
    Kayıp_Travma: str # 'Yok' - 'Var'
    sorular: list # contains 34 items ranging from 0 to 5

class golombok_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str # 'Evli' - 'Bekar' - 'Birlikte' - 'Boşanmış'
    İlişki_Süresi_Yıl: int
    Cinsel_Yönelim: str # 'Heteroseksüel', 'Biseksüel', 'Homoseksüel', 'Diğer'
    Cinsel_Frekans: str # 'Haftada ≥5', 'Haftada 2–4', 'Haftada ≤1'
    Cinsel_Eğitim: str # 'Var', 'Yok'
    Psikolojik_Destek: str # 'Var', 'Yok'
    Psikolojik_Tanı: str # 'Var', 'Yok'
    Cinsel_Travma: str # 'Var', 'Yok'
    Alkol_Kullanımı: str # 'Yok', 'Ara sıra', 'Sık'
    Porno_İzleme_Sıklığı: str # 'Haftada birkaç kez', 'Ayda birkaç kez', 'Her gün', 'Hiç'
    Partner_Yaş_Farkı: int 
    Partnerle_Cinsel_Uyum: float # 0-10
    Cinsel_İletişim_Düzeyi: float # 0-10
    Sadakat_Sorunu: str # 'Evet', 'Hayır'
    İlişkiden_Memnuniyet: float # 0-10
    Günlük_Stres: float # 0-10
    Uyku_Kalitesi: float # 0-10
    Fiziksel_Sağlık_Sorunu: str # 'Evet', 'Hayır'
    sorular: list # contains 28 items ranging from 0 to 5

class okb_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Eğitim: str # 'Yüksek Lisans', 'Lise', 'Üniversite', 'İlkokul', 'Doktora'
    Gelir: str # 'Düşük', 'Orta', 'Yüksek'
    Medeni_Durum: str # 'Evli', 'Bekar', 'Boşanmış'
    Yaşam_Yeri: str # 'Küçük Şehir', 'Metropol', 'Kırsal'
    İş_Durumu: str # 'Çalışıyor', 'Öğrenci', 'İşsiz', 'Emekli'
    Psikolojik_Destek: str # 'Var', 'Yok'
    Ailede_Psik_Hastalik: str # 'Var', 'Yok'
    Nevrotiklik: float # 1-5
    Mükemmeliyetçilik: float # 1-5
    Günlük_Stres: float # 0-10
    Fiziksel_Sağlık_Sorunu: str # 'Var', 'Yok'
    Uyku_Kalitesi: float # 0-10
    Anksiyete: float # 0-10
    Depresyon: float # 0-10
    Sosyal_Destek: str # 'Düşük', 'Orta', 'Yüksek'
    Alkol_Madde_Kullanımı: str # 'Var', 'Yok'
    Fiziksel_Aktivite: str # 'Hiç', 'Ara sıra', 'Düzenli'
    Teknoloji_Süresi_Saat: float
    Hobi_Sosyal_Aktivite: str # 'Düşük', 'Orta', 'Yüksek'
    Dini_İnanç: str # 'Zayıf', 'Orta', 'Güçlü'
    Kayıp_Travma: str # 'Yok', 'Var'
    sorular: list # contains 36 items ranging from 0 to 1