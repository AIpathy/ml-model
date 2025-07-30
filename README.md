<div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 20px; border-radius: 8px;">
  <h1># AIpathy ML-Model</h1>
  <p>AIpathy projesinin Machine Learning ve AI servislerini sağlayan Python tabanlı microservice'idir.</p>
  <p>Bu servis, psikolojik test analizleri, ses analizi ve AI destekli yorumlar sunar.</p>
</div>

---

<div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 20px; border-radius: 8px;">
  <h2>🛠️ Kullanılan Teknolojiler ve Araçlar</h2>

  <h3><strong>Diller:</strong></h3>
  <ul>
    <li><strong>Python</strong> - Ana programlama dili</li>
  </ul>

  <h3><strong>Web Framework:</strong></h3>
  <ul>
    <li><strong>FastAPI</strong></li>
    <li><strong>Uvicorn</strong> - ASGI server</li>
  </ul>

  <h3><strong>Machine Learning ve Data Science:</strong></h3>
  <ul>
    <li><strong>scikit-learn</strong> - Machine learning library</li>
    <li><strong>pandas</strong> - Data manipulation ve analiz</li>
    <li><strong>Pydantic</strong> - Data validation ve serialization</li>
  </ul>

  <h3><strong>AI ve NLP:</strong></h3>
  <ul>
    <li><strong>google-genai</strong> - Google Gemini AI integration & "gemini-2.5-flash"</li>
    <li><strong>ElevenLabs</strong> - Speech-to-text & "scribe_v1"</li>
  </ul>

  <h3><strong>HTTP ve API:</strong></h3>
  <ul>
    <li><strong>requests</strong> - HTTP</li>
    <li><strong>python-multipart</strong> - File upload handling</li>
  </ul>

  <h3><strong>Database:</strong></h3>
  <ul>
    <li><strong>MySQL</strong></li>
  </ul>

  <h3><strong>Development ve Environment:</strong></h3>
  <ul>
    <li><strong>python-dotenv</strong> - Environment variables</li>
  </ul>

  <h3><strong>Deployment/Containerization:</strong></h3>
  <ul>
    <li><strong>Docker</strong> - Containerization</li>
    <li><strong>Docker Compose</strong> - Multi-container orchestration</li>
  </ul>

  <h3><strong>CI/CD:</strong></h3>
  <ul>
    <li><strong>Github Actions</strong></li>
    <li><strong>Deploy to Server</strong></li>
  </ul>

  <h3><strong>Domain/Hosting/Server</strong></h3>
  <ul>
    <li><strong>ML Service Domain: https://ml.aipathy.xyz</strong></li>
    <li><strong>Main Domain: aipathy.xyz</strong></li>
    <li><strong>Provider: Sercan Arga (Teşekkürler)</strong></li>
  </ul>

  <h3><strong>Control Panel:</strong></h3>
  <ul>
    <li><strong>Plesk</strong> - Web hosting kontrol paneli</li>
  </ul>
</div>

---

<div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 20px; border-radius: 8px;">
  <h2>Proje Mimarisi ve Kod Yapısı</h2>

  <h3><strong>Microservice Architecture:</strong></h3>
  <ul>
    <li><strong>FastAPI</strong></li>
    <li><strong>RESTful API</strong> - Standart HTTP endpoint'leri</li>
    <li><strong>Async/Await</strong> - Asynchronous request handling</li>
    <li><strong>Pydantic Models</strong> - Request/response validation</li>
  </ul>

  <h3><strong>API Endpoints:</strong></h3>
  <ul>
    <li><strong>GET /</strong> - Health check</li>
    <li><strong>GET /health</strong> - Service status</li>
    <li><strong>POST /predict_anksiyete/</strong> - Anksiyete testi analizi</li>
    <li><strong>POST /predict_borderline/</strong> - Borderline testi analizi</li>
    <li><strong>POST /predict_narsizm/</strong> - Narsizm testi analizi</li>
    <li><strong>POST /predict_sosyal_fobi/</strong> - Sosyal fobi testi analizi</li>
    <li><strong>POST /predict_beck_depresyon/</strong> - Beck depresyon testi analizi</li>
    <li><strong>POST /predict_alkol/</strong> - Alkol testi analizi</li>
    <li><strong>POST /stt_emotion/</strong> - Ses analizi ve duygu tespiti</li>
    <li><strong>POST /chat</strong> - AI destekli sohbet</li>
  </ul>

  <h3><strong>ML Model Yapısı:</strong></h3>
  <ul>
    <li><strong>Random Forest Classifiers</strong> - Ana ML algoritması</li>
    <li><strong>Label Encoders</strong> - Kategorik veri encoding</li>
    <li><strong>Feature Engineering</strong> - Veri ön işleme</li>
    <li><strong>Model Serialization</strong> - Pickle formatında model saklama</li>
  </ul>

  <h3><strong>AI Entegrasyonu:</strong></h3>
  <ul>
    <li><strong>Google Gemini AI</strong> - Metin analizi ve yorumlar</li>
    <li><strong>ElevenLabs</strong> - Speech-to-text</li>
    <li><strong>Emotion Analysis</strong> - Ses dosyalarından duygu analizi</li>
    <li><strong>Natural Language Processing</strong> - Metin işleme</li>
  </ul>

  <h3><strong>Data Validation:</strong></h3>
  <ul>
    <li><strong>Pydantic Models</strong> - Request/response validation</li>
    <li><strong>Type Hints</strong> - Python type checking</li>
    <li><strong>Input Validation</strong> - Veri doğrulama</li>
    <li><strong>Error Handling</strong> - Hata yönetimi</li>
  </ul>

  <h3><strong>Performance Optimizations:</strong></h3>
  <ul>
    <li><strong>Async/Await</strong> - Asynchronous request handling</li>
    <li><strong>Model Caching</strong> - Pre-loaded ML models</li>
    <li><strong>Memory Management</strong> - Efficient resource usage</li>
    <li><strong>Docker Optimization</strong> - Container performance</li>
  </ul>

  <h3><strong>Security Features:</strong></h3>
  <ul>
    <li><strong>Input Validation</strong> - Request data validation</li>
    <li><strong>File Upload Security</strong> - Secure file handling</li>
    <li><strong>Error Handling</strong> - Secure error responses</li>
    <li><strong>Environment Variables</strong> - Secure configuration</li>
  </ul>
</div>

---

<div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 20px; border-radius: 8px;">
  <h2>ML Model Detayları</h2>

  <h3><strong>Desteklenen Testler:</strong></h3>
  <ol>
    <li><strong>Beck Anksiyete Testi</strong> - 20 soru, 0-3 puanlama</li>
    <li><strong>Borderline Kişilik Testi</strong> - 53 soru, 0-1 puanlama</li>
    <li><strong>Narsizm Testi</strong> - 25 soru, 0-4 puanlama</li>
    <li><strong>Sosyal Fobi Testi</strong> - 45 soru, 0-4 puanlama</li>
    <li><strong>Beck Depresyon Testi</strong> - 21 soru, 0-3 puanlama</li>
    <li><strong>Alkol Testi</strong> - 34 soru, 0-3 puanlama</li>
  </ol>

  <h3><strong>Risk Grupları:</strong></h3>
  <ul>
    <li><strong>Düşük Risk</strong> - Normal seviye</li>
    <li><strong>Orta Risk</strong> - Dikkat edilmeli</li>
    <li><strong>Yüksek Risk</strong> - Profesyonel destek gerekli</li>
  </ul>

  <h3><strong>AI Özellikleri:</strong></h3>
  <ul>
    <li><strong>Ses Analizi</strong> - Konuşma tonundan duygu tespiti</li>
    <li><strong>Chatbot</strong> - AI destekli sohbet sistemi</li>
    <li><strong>Personalized Responses</strong> - Kişiselleştirilmiş yanıtlar</li>
  </ul>
</div>

---

<div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 20px; border-radius: 8px;">
  <h2>Gelecek Geliştirmeler</h2>

  <h3><strong>Planlanan Özellikler:</strong></h3>
  <ul>
    <li><strong>Text-to-Speech for AI</strong> - AI ile realtime sesli sohbet</li>
    <li><strong>Test Sonuçlarına Göre AI Sohbeti</strong> - Kullanıcıların çözdüğü testlere göre bağlam ve analiz</li>
    <li><strong>Multi-language Support</strong> - Çoklu dil desteği</li>
    <li><strong>Model Retraining</strong> - Otomatik model güncelleme</li>
    <li><strong>Advanced Analytics</strong> - Gelişmiş analitik raporlar</li>
  </ul>
</div>

---

<div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 20px; border-radius: 8px;">
  <p><strong>Not</strong>: Bu servis, AIpathy projesinin AI/ML ihtiyaçlarını karşılamak üzere tasarlanmıştır.</p>
</div>
