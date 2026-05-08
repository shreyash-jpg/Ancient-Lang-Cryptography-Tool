# 🕉️ Shlokey: Ancient-Lang-Cryptography-Tool

### 🎉 Overview
**Shlokey** is a professional cryptography tool that converts text/files between **English ↔ Pali ↔ Brahmi** script using dictionary-based mappings. Perfect for secure text transformation, ancient script encoding, or linguistic experiments.

---

### ✨ Features
- 🔓 **Text Encryption/Decryption:** (English → Brahmi / Brahmi → English)
- 📁 **File Processing:** Any file type (up to 1MB limit)
- 🎨 **Modern Dark UI:** Responsive & Professional glassmorphism design
- 📜 **Session History:** View recent operations with previews
- ⚡ **Fast Processing:** Real-time results

---

### 🚀 Quick Start

#### Prerequisites
- Python 3.8+
- Flask

#### Installation & Setup
1. **Clone the repository**
   
   git clone [https://github.com/shreyash-jpg/Ancient-Lang-Cryptography-Tool.git]
   cd shlokeyweb
2. **Install dependencies
    pip install -r requirements.txt

3. **Run the application
     python app.py
4. **Visit: http://127.0.0.1:5000 in your browser.

### 📋 Usage
**Web Interface (Recommended)
     Text Mode: Enter text → Click Encrypt/Decrypt.
     File Mode: Upload file → Process → Download result.
     History: View your session-based activity.

**Output Formats:
     Encrypted: {filename}_encrypted.brahmi
     Decrypted: {filename}_decrypted.txt

**CLI Mode (Optional)
     python shlokey.py

### 📂 File Structure

 shlokeyweb/
  ├── app.py              # Flask web app
  ├── shlokey.py          # CLI version  
  ├── pali.json           # English ↔ Pali dictionary (1000+ words)
  ├── brahmi.json         # Pali ↔ Brahmi script mapping
  ├── templates/
  │   └── index.html      # Modern UI
  ├── requirements.txt    # Dependencies
└── README.md           # Documentation
###🔧 Customization
       Add New Words:  pali.json -> "word": "translation"
       Extend Scripts:  brahmi.json -> "char": "glyph"

### 🎨 UI Features
     Dark Theme - Glassmorphism design
     Responsive - Mobile/Desktop
     Icons - FontAwesome throughout
     Animations - Smooth hovers/transitions
     Real-time Preview - History & results
