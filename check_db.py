import sqlite3

# الاتصال بقاعدة البيانات - تأكد أن الملف في نفس المجلد أو عدل المسار
try:
    conn = sqlite3.connect('chinook.db')

    # تنفيذ الاستعلام لجلب أسماء الجداول
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = conn.execute(query).fetchall()

    print("الجداول الموجودة:")
    print([t[0] for t in tables])

    conn.close()
except Exception as e:
    print(f"حدث خطأ: {e}")