import os
from project import get_notes, load_or_create_key, save_note


def test_load_or_create_key():
    # التأكد من أن دالة المفتاح تعمل وتنشئ الملف بنجاح
    key_file = "test_secret.key"
    if os.path.exists(key_file):
        os.remove(key_file)

    load_or_create_key(key_file)
    assert os.path.exists(key_file)

    # تنظيف الملف بعد الاختبار
    if os.path.exists(key_file):
        os.remove(key_file)


def test_save_and_get_notes():
    # اختبار حفظ واسترجاع المذكرات
    test_journal = "test_journal.txt"
    if os.path.exists(test_journal):
        os.remove(test_journal)

    save_note("This is a test secure note.", test_journal)
    content = get_notes(test_journal)

    assert "This is a test secure note." in content

    # تنظيف الملف بعد الاختبار
    if os.path.exists(test_journal):
        os.remove(test_journal)