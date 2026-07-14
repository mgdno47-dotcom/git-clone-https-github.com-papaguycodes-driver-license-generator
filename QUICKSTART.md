# Driver License Generator - Quick Start Guide

## 🚗 Driver License Generator - အင်စတောလုပ်ခြင်း ရည်ညွှန်းချက်

### Windows မှာ အင်စတောလုပ်ခြင်း (အလွယ်ကျဆုံး)

1. **Repository Clone လုပ်ပါ**
```bash
git clone https://github.com/mgdno47-dotcom/git-clone-https-github.com-papaguycodes-driver-license-generator.git
cd git-clone-https-github.com-papaguycodes-driver-license-generator
```

2. **`setup.bat` ကို Double-Click လုပ်ပါ** ✨
   - အလိုအလျောက် အားလုံးသည် setup လုပ်ပေးပါတယ်
   - Python dependencies install လုပ်ပါတယ်
   - Web server တစ်ခါထဲ run လုပ်သွားပါတယ်

3. **Web Browser မှာ ဖွင့်ပါ**
   - `http://localhost:5000` သို့ သွားပါ
   - Driver License Form ကို fill လုပ်ပါ
   - License ကို generate လုပ်ပါ
   - PNG ဖိုင်ကို download လုပ်ပါ

---

### macOS / Linux မှာ အင်စတောလုပ်ခြင်း

1. **Repository Clone လုပ်ပါ**
```bash
git clone https://github.com/mgdno47-dotcom/git-clone-https-github.com-papaguycodes-driver-license-generator.git
cd git-clone-https-github.com-papaguycodes-driver-license-generator
```

2. **Setup Script Run လုပ်ပါ**
```bash
chmod +x setup.sh
./setup.sh
```

3. **Web Browser မှာ ဖွင့်ပါ**
   - `http://localhost:5000` သို့ သွားပါ

---

## 🛠️ Manual Setup (အကယ်လို Setup Script မ run မဖြစ်ရင်)

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## ✅ အင်္ဂလိပ်စာ လုပ်ဆောင်ချက်များ

1. **Fill in your personal information**
   - First Name
   - Last Name
   - Date of Birth
   - Gender
   - Address
   - State/Province

2. **Upload your photo**
   - Click on file input
   - Select your picture (JPG, PNG, GIF)

3. **Click "Generate License"**
   - System will create your driver license
   - PNG file will be downloaded automatically

4. **Save the file**
   - Your driver license PNG will be saved

---

## 📁 Project Structure

```
driver-license-generator/
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── setup.bat             # Windows setup script
├── setup.sh              # macOS/Linux setup script
├── QUICKSTART.md         # This file
├── README.md             # Full documentation
├── templates/
│   └── index.html        # Web form
├── uploads/              # Photo uploads
└── venv/                 # Virtual environment (created after setup)
```

---

## 🐛 Troubleshooting

### Python not found error?
- Windows မှာ Python install လုပ်ပါ: https://www.python.org/

### Port 5000 already in use?
```bash
# အခြား port သုံးပါ
python app.py --port 5001
```

### Dependencies install မဖြစ်ရင်?
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📞 ကူညီခြင်း

GitHub Issues တွင် သို့မဟုတ် Documentation ကို ကြည့်ပါ။

---

**Happy License Generating!** 🚗✨

Made with ❤️ by Driver License Generator Team
