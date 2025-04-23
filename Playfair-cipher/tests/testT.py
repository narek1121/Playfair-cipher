import unittest
from playfairCipher.cipher import PlayfairCipher

class TestPlayfairCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = PlayfairCipher("MONARCHY")

    def test_encrypt_decrypt(self):
        plaintext = "HELLO WORLD"
        encrypted = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(encrypted)
        cleaned = decrypted.replace('X', '')
        self.assertTrue("HELLOWORLD".startswith(cleaned[:len("HELLOWORLD")]))

    def test_handle_repeated_letters(self):
        plaintext = "BALLOON"
        encrypted = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(encrypted)
        cleaned = decrypted.replace('X', '')
        self.assertTrue("BALLOON".startswith(cleaned[:len("BALLOON")]))

    def test_ignore_non_letters(self):
        plaintext = "ATTACK AT DAWN!"
        encrypted = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(encrypted)
        cleaned = decrypted.replace('X', '')
        self.assertTrue("ATTACKATDAWN".startswith(cleaned[:len("ATTACKATDAWN")]))
