import json
import os
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "omega_ghost_watches"
# Load NLP model
nlp = None

# Dynamic base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Load JSON safely
def load_json(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

# Load dictionaries
pali_dict = load_json(os.path.join(base_path, "pali.json"))
brahmi_dict = load_json(os.path.join(base_path, "brahmi.json"))

# Reverse dictionaries
pali_to_eng_dict = {v: k for k, v in pali_dict.items()}
brahmi_to_pali_dict = {v: k for k, v in brahmi_dict.items()}

# History file
HISTORY_FILE = os.path.join(base_path, "history.json")

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(data):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

history = load_history()

# NLP processing
def preprocess_text(text):
    return text.lower().split()

# Conversion functions
def english_to_pali(text):
    return " ".join(pali_dict.get(w, w) for w in preprocess_text(text))

def pali_to_brahmi(text):
    return "".join(brahmi_dict.get(c, c) for c in text)

def brahmi_to_pali(text):
    return "".join(brahmi_to_pali_dict.get(c, c) for c in text)

def pali_to_english(text):
    return " ".join(pali_to_eng_dict.get(w, w) for w in text.split())

# Main route
@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []

    result = ""
    file_result = None

    if request.method == "POST":
        action = request.form.get("action", "encrypt")
        
        # Handle file upload
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                original_filename = os.path.basename(file.filename)
                try:
                    text_content = file.read().decode('utf-8', errors='ignore')
                except:
                    text_content = '[Binary file content not processable as text]'
                
                # Save original bytes for binary-ish handling if needed
                file.seek(0)
                original_bytes = file.read()
                if len(original_bytes) > 1000000:  # 1MB limit
                    text_content = '[File too large]'

                
                entry = {"action": action, "filename": original_filename}
                
                if text_content.startswith('['):  # Non-text fallback
                    processed = text_content
                    output_filename = original_filename.rsplit('.', 1)[0] + '_processed.txt'
                elif "encrypt_file" in action:
                    processed = pali_to_brahmi(english_to_pali(text_content))
                    output_filename = original_filename.rsplit('.', 1)[0] + '_encrypted.brahmi'
                else:  # decrypt_file
                    pali_text = brahmi_to_pali(text_content)
                    processed = pali_to_english(pali_text)
                    output_filename = original_filename.rsplit('.', 1)[0] + '_decrypted.txt'
                
                file_result = {'filename': output_filename, 'content': processed}
                entry["output"] = processed[:100] + "..." if len(processed) > 100 else processed  # Truncate for history
                session["history"].append(entry)
                session.modified = True
                return render_template("index.html", file_result=file_result, history=session["history"])
        
        # Handle text input
        text = request.form.get("text", "").strip()
        if text:
            if action == "encrypt":
                result = pali_to_brahmi(english_to_pali(text))
            elif action == "decrypt":
                pali_text = brahmi_to_pali(text)
                result = pali_to_english(pali_text)

            session["history"].append({
                "action": action,
                "input": text,
                "output": result
            })
            session.modified = True

    return render_template("index.html", result=result, file_result=file_result, history=session["history"])

# Clear history
@app.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)
    return redirect(url_for("index"))

# Run app
if __name__ == "__main__":
    app.run(debug=True)
