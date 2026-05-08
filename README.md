# Shlokey:Ancient-Lang-Cryptography-Tool

🎉 Overview
Shlokey is a professional cryptography tool that converts text/files between English ↔ Pali ↔ Brahmi script using dictionary-based mappings. Perfect for secure text transformation, ancient script encoding, or linguistic experiments.

Features
🔓 Text Encryption/Decryption (English → Brahmi / Brahmi → English)
📁 File Processing (Any file type - 1MB limit)
🎨 Modern Dark UI - Responsive & Professional
📜 Session History with previews
⚡ Fast Processing - Real-time results
🚀 Quick Start
# Clone & setup
git clone https://github.com/atheistog/shlokeyweb.git
cd shlokeyweb

# Install dependencies
pip install -r requirements.txt

# Run web app
python app.py
Open http://127.0.0.1:5000

📋 Usage
Web Interface (Recommended)
Text Mode: Enter text → Encrypt/Decrypt Text
File Mode: Upload any file → Encrypt/Decrypt File → Download result
History: View recent operations (session-based)
Output Formats:

Encrypted: {filename}_encrypted.brahmi
Decrypted: {filename}_decrypted.txt
Binary files: Placeholder message preserved
CLI Mode (Optional)
python shlokey.py
# Follow interactive menu
🛠 Installation & Setup
Prerequisites
Python 3.8+
Flask (pip install flask)
Full Setup
1. git clone https://github.com/atheistog/shlokeyweb.git
2. cd shlokey
3. pip install -r requirements.txt
4. python app.py
5. Visit http://127.0.0.1:5000
File Structure
shlokeyweb/
├── app.py                 # Flask web app
├── shlokey.py            # CLI version  
├── pali.json             # English ↔ Pali dictionary (1000+ words)
├── brahmi.json           # Pali ↔ Brahmi script mapping
├── templates/
│   └── index.html        # Modern UI
├── history.json          # Persistent history (optional)
├── requirements.txt      # Dependencies
└── README.md            # You're reading it!
🔧 Customization
Add New Words
Edit pali.json:

"new_word": "pali_translation"
Extend Scripts
Add to brahmi.json:

"new_char": "𑀓𑀩"  // Brahmi glyph
🎨 UI Features
Dark Theme - Glassmorphism design
Responsive - Mobile/Desktop
Icons - FontAwesome throughout
Animations - Smooth hovers/transitions
Real-time Preview - History & results
📱 Demo
Shlokey Demo

🤝 Contributing
Fork repository
Create feature branch (git checkout -b feature/amazing)
Commit changes (git commit -m 'Add amazing feature')
Push (git push origin feature/amazing)
Open Pull Request
📄 License
MIT License - See LICENSE file.

🙏 Acknowledgments
Built with Flask
Icons by FontAwesome
Inspired by ancient Brahmi script preservation
⭐ Star this project if useful!
🐛 Found a bug? Open an issue!
