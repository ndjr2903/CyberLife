# 🛡️ CyberLife - Advanced Encryption & Security Tool

x-special/nautilus-clipboard
copy
file:///tmp/VMwareDnD/LRYpbG/Screenshot 2026-10-21 162627.png

**CyberLife** הוא כלי מתקדם לאבטחת מידע והצפנת קבצים שפותח ב-Python. הכלי נועד לספק מעטפת הצפנה הרמטית, לנהל פרוטוקולים מאובטחים בסביבות מקומיות ומרוחקות, ולהבטיח הגנה מוחלטת על נתונים רגישים.

---

## ✨ תכונות מרכזיות (Features)

הכלי תומך במגוון רחב של אלגוריתמים ושיטות עבודה:
הכלי תומך ב-5 שיטות ומתודולוגיות הצפנה עיקריות:
1. **AES:** הצפנה סימטרית מהירה ומאובטחת.
2. **Hybrid:** שילוב עוצמתי בין AES ו-RSA.
3. **Remote Encryption via SSH:** הצפנה מרחוק מעל תקשורת SSH, הכוללת הורדת הקובץ המקורי, הצפנתו ומחיקתו המאובטחת מהשרת המרוחק.
4. **Encrypt entire drive:** הצפנת כוננים שלמים באמצעות BitLocker או VeraCrypt.
5. **Encrypting mac computers:** תמיכה בהצפנת מחשבי מק.
---

## ⚙️ דרישות המערכת והתקנה (Installation & Setup)

כדי להריץ את הכלי בצורה נקה ומאובטחת בסביבה וירטואלית ייעודית (מומלץ ב-Kali Linux או סביבות לינוקס דומות), עקוב אחר השלבים הבאים:

1. **שכפול המאגר (Clone):**
   ```bash
   git clone https://github.com/ndjr2903/cyber_life.git
   cd cyber_life
   ```bash

1. **יצירת סביבה וירטואלית (כולל הפעלת הסביבה הסביבה הוירטואלית):**
   ```bash
   python3 -m venv ~/recon-env
   source ~/recon-env/bin/activate
   ```bash


1. **התקנת הספריות והתלויות הנדרשות מתוך הקובץ:**
   ```bash
   pip install -r requirements.txt
   ```bash

# 🚀 הפעלת הכלי (Usage)
לאחר שהסביבה פעילה והתלויות מותקנות, הפעל את הסקריפט:
   ```bash
   python3 cyber_life.py
   ```

**בחר את האפשרות הרצויה (1-5) מתוך התפריט הראשי המוצג במסוף.**


# 🛠️ טכנולוגיות (Built With)
Python 3 - השפה המרכזית לפיתוח הלוגיקה והכלים.
SSH Protocols - לניהול תקשורת מאובטחת והצפנת קבצים מרחוק.

# 👤 יוצר הפרויקט (Creator)
מאיר עמוס (ndjr2903)
מייסד GlitchStrike – מומחה לבדיקות חדירה ומודיעין סייבר.
