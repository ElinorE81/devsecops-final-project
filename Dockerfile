# שימוש בתמונת פייתון רשמית וקלה
FROM python:3.9-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ התלויות והתקנתן
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד האפליקציה
COPY app.py .

# פתיחת הפורט שעליו הפלאסק רץ
EXPOSE 5000

# הפקודה שתרוץ כשהקונטיינר יעלה
CMD ["python", "app.py"]
