from datetime import datetime
import os
from cryptography.fernet import Fernet

# تحديد المسارات المطلقة لضمان عمل البرنامج بسلاسة في أي مجلد
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JOURNAL_FILE = os.path.join(BASE_DIR, "journal.txt")
KEY_FILE = os.path.join(BASE_DIR, "secret.key")


def main():
    print("--- Personal Digital Safe & Journal System ---")
    load_or_create_key()

    while True:
        print("\n[Main Menu]:")
        print("1. Add a new text note")
        print("2. View all saved notes")
        print("3. Encrypt a sensitive image")
        print("4. Decrypt an encrypted image")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            note = input("Write your secret note: ").strip()
            if note:
                save_note(note)
                print("✔ Note saved and secured successfully.")
            else:
                print("⚠ Warning: Cannot save an empty note.")

        elif choice == "2":
            print("\n--- Notes History ---")
            notes = get_notes()
            if notes:
                print(notes)
            else:
                print("No notes recorded yet.")

        elif choice == "3":
            img_path = input("Enter image path to encrypt: ").strip()
            encrypt_image(img_path)

        elif choice == "4":
            enc_path = input("Enter encrypted image path (.enc): ").strip()
            decrypt_image(enc_path)

        elif choice == "5":
            print("Exiting system securely. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please enter a number between 1 and 5.")


def save_note(note, filename=JOURNAL_FILE):
    """Save a note with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n{note}\n" + "-" * 30 + "\n")


def get_notes(filename=JOURNAL_FILE):
    """Retrieve all saved notes."""
    if not os.path.exists(filename):
        return ""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def load_or_create_key(key_filename=KEY_FILE):
    """Ensure the encryption key exists, otherwise generate a new one."""
    if not os.path.exists(key_filename):
        key = Fernet.generate_key()
        with open(key_filename, "wb") as key_file:
            key_file.write(key)
    return key_filename


def encrypt_image(image_path, key_filename=KEY_FILE):
    """Encrypt binary image data and save it with a .enc extension."""
    if not os.path.exists(image_path):
        print("❌ Error: Image file does not exist!")
        return False

    try:
        with open(key_filename, "rb") as key_file:
            key = key_file.read()

        fernet = Fernet(key)

        with open(image_path, "rb") as img_file:
            img_data = img_file.read()

        encrypted_data = fernet.encrypt(img_data)
        output_path = image_path + ".enc"

        with open(output_path, "wb") as enc_file:
            enc_file.write(encrypted_data)

        print(f"✔ Image encrypted successfully: {output_path}")
        return True
    except Exception as e:
        print(f"❌ An error occurred during encryption: {e}")
        return False


def decrypt_image(encrypted_path, key_filename=KEY_FILE):
    """Decrypt an encrypted image and restore its original format."""
    if not os.path.exists(encrypted_path):
        print("❌ Error: Encrypted file does not exist!")
        return False

    try:
        with open(key_filename, "rb") as key_file:
            key = key_file.read()

        fernet = Fernet(key)

        with open(encrypted_path, "rb") as enc_file:
            encrypted_data = enc_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        if encrypted_path.endswith(".enc"):
            output_path = encrypted_path[:-4]
        else:
            output_path = encrypted_path + "_decrypted"

        with open(output_path, "wb") as dec_file:
            dec_file.write(decrypted_data)

        print(f"✔ Image decrypted and restored successfully: {output_path}")
        return True
    except Exception as e:
        print("❌ Security Error: Decryption failed.")
        return False


if __name__ == "__main__":
    main()