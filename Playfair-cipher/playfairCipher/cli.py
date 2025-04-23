from playfairCipher.cipher import PlayfairCipher

def interactive_mode():
    key = input("Enter key for Playfair Cipher: ").strip()
    cipher = PlayfairCipher(key)

    while True:
        mode = input("\nChoose mode: (E)ncrypt / (D)ecrypt / (Q)uit: ").strip().upper()
        if mode == 'E':
            plaintext = input("Enter plaintext: ")
            print("Encrypted:", cipher.encrypt(plaintext))
        elif mode == 'D':
            ciphertext = input("Enter ciphertext: ")
            print("Decrypted:", cipher.decrypt(ciphertext))
        elif mode == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose E, D, or Q.")

if __name__ == "__main__":
    interactive_mode()
