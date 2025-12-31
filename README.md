# 🔐 Quantum Certificate Verification System

A **Final Year Project** designed to detect **fake academic certificates** using a **quantum-inspired cryptographic hashing technique**.  
The system securely issues digital certificates and verifies their authenticity by detecting any data tampering.

---

## 📌 Abstract

Fake certificates are a serious problem in academic and professional environments.  
This project proposes a **Quantum Certificate Verification System** that generates a quantum-resistant hash at the time of certificate issuance. During verification, the hash is regenerated and compared with the stored hash to determine authenticity. Any modification in certificate data results in a mismatch, instantly identifying fake certificates.

---

## ✨ Features

- Secure certificate issuance
- Quantum-inspired hash generation
- Fake certificate detection
- Real-time certificate verification
- Web-based user interface
- REST API based backend
- Simple and scalable architecture

---

## 🏗️ Project Structure

finalyearproject/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── models/
│ │ └── certificate.py
│ ├── utils/
│ │ └── quantum_hash.py
│ └── routes/
│ └── certificate_routes.py
│
├── index.html # Frontend (HTML + CSS + JavaScript combined)
└── README.md


---

## ⚙️ Technologies Used

- **Python**
- **Flask**
- **Flask-CORS**
- **HTML, CSS, JavaScript**
- **Quantum-inspired cryptographic hashing**
- **REST APIs**

---

## 🚀 How to Run the Project

### 1️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
