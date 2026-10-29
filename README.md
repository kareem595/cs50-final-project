# Personal Digital Safe & Journal System
#### Video Demo: [https://youtu.be/DrwLU01u2uI?si=XldjY_w91qEh8-iL]
#### Description:
The **Personal Digital Safe & Journal System** is a command-line application built in Python designed to provide secure text journaling and sensitive image encryption using symmetric encryption (Fernet from the `cryptography` library).

### Features:
1. **Secure Journaling:** Save and view timestamped private text notes stored safely.
2. **Image Encryption:** Encrypt sensitive image files into secure `.enc` binaries.
3. **Image Decryption:** Safely restore encrypted images back to their original viewable format.
4. **Key Management:** Automatically generates and manages unique security keys (`secret.key`).

### Files Included:
- `project.py`: The main program containing the core logic and menu.
- `test_project.py`: Unit tests implemented using `pytest` to test core functions.
- `README.md`: Project documentation.
