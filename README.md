# AIpathy ML-Model

AIpathy projesinin Machine Learning ve AI servislerini sağlayan Python tabanlı microservice'idir.

Bu servis, psikolojik test analizleri, ses analizi ve AI destekli yorumlar sunar.

---

## 🛠️ Kullanılan Teknolojiler ve Araçlar

### **Diller:**
- **Python** - Ana programlama dili

### **Web Framework:**
- **FastAPI**
- **Uvicorn** - ASGI server

### **Machine Learning ve Data Science:**
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation ve analiz
- **Pydantic** - Data validation ve serialization

### **AI ve NLP:**
- **google-genai** - Google Gemini AI integration & "gemini-2.5-flash"
- **ElevenLabs** - Speech-to-text & "scribe_v1"

### **HTTP ve API:**
- **requests** - HTTP
- **python-multipart** - File upload handling

### **Database:**
- **MySQL**

### **Development ve Environment:**
- **python-dotenv** - Environment variables

### **Deployment/Containerization:**
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

### **CI/CD:**
- **Github Actions**
- **Deploy to Server**

### **Domain/Hosting/Server**
- **ML Service Domain: https://ml.aipathy.xyz**
- **Main Domain: aipathy.xyz**
- **Provider: Sercan Arga (Teşekkürler)**

### **Control Panel:**
- **Plesk** - Web hosting kontrol paneli

---

## Proje Mimarisi ve Kod Yapısı

### **Microservice Architecture:**
- **FastAPI**
- **RESTful API** - Standart HTTP endpoint'leri
- **Async/Await** - Asynchronous request handling
- **Pydantic Models** - Request/response validation

### **API Endpoints:**
- **GET /** - Health check
- **GET /health** - Service status
- **POST /predict_anksiyete/** - Anksiyete testi analizi
- **POST /predict_borderline/** - Borderline testi analizi
- **POST /predict_narsizm/** - Narsizm testi analizi
- **POST /predict_sosyal_fobi/** - Sosyal fobi testi analizi
- **POST /predict_beck_depresyon/** - Beck depresyon testi analizi
- **POST /predict_alkol/** - Alkol testi analizi
- **POST /stt_emotion/** - Ses analizi ve duygu tespiti
- **POST /chat** - AI destekli sohbet

### **ML Model Yapısı:**
- **Random Forest Classifiers** - Ana ML algoritması
- **Label Encoders** - Kategorik veri encoding
- **Feature Engineering** - Veri ön işleme
- **Model Serialization** - Pickle formatında model saklama

### **AI Entegrasyonu:**
- **Google Gemini AI** - Metin analizi ve yorumlar
- **ElevenLabs** - Speech-to-text
- **Emotion Analysis** - Ses dosyalarından duygu analizi
- **Natural Language Processing** - Metin işleme

### **Data Validation:**
- **Pydantic Models** - Request/response validation
- **Type Hints** - Python type checking
- **Input Validation** - Veri doğrulama
- **Error Handling** - Hata yönetimi

### **Performance Optimizations:**
- **Async/Await** - Asynchronous request handling
- **Model Caching** - Pre-loaded ML models
- **Memory Management** - Efficient resource usage
- **Docker Optimization** - Container performance

### **Security Features:**
- **Input Validation** - Request data validation
- **File Upload Security** - Secure file handling
- **Error Handling** - Secure error responses
- **Environment Variables** - Secure configuration

---

## ML Model Detayları

### **Desteklenen Testler:**
1. **Beck Anksiyete Testi** - 20 soru, 0-3 puanlama
2. **Borderline Kişilik Testi** - 53 soru, 0-1 puanlama
3. **Narsizm Testi** - 25 soru, 0-4 puanlama
4. **Sosyal Fobi Testi** - 45 soru, 0-4 puanlama
5. **Beck Depresyon Testi** - 21 soru, 0-3 puanlama
6. **Alkol Testi** - 34 soru, 0-3 puanlama

### **Risk Grupları:**
- **Düşük Risk** - Normal seviye
- **Orta Risk** - Dikkat edilmeli
- **Yüksek Risk** - Profesyonel destek gerekli

### **AI Özellikleri:**
- **Ses Analizi** - Konuşma tonundan duygu tespiti
- **Chatbot** - AI destekli sohbet sistemi
- **Personalized Responses** - Kişiselleştirilmiş yanıtlar

---

## Gelecek Geliştirmeler

### **Planlanan Özellikler:**
- **Text-to-Speech for AI** - AI ile realtime sesli sohbet
- **Test Sonuçlarına Göre AI Sohbeti** - Kullanıcıların çözdüğü testlere göre bağlam ve analiz
- **Multi-language Support** - Çoklu dil desteği
- **Model Retraining** - Otomatik model güncelleme
- **Advanced Analytics** - Gelişmiş analitik raporlar

---

> **Not**: Bu servis, AIpathy projesinin AI/ML ihtiyaçlarını karşılamak üzere tasarlanmıştır.
