class PlayfairCipher:
    def __init__(self, key):
        self.table = self._generate_table(key)

    def _generate_table(self, key):
        key = key.upper().replace('J', 'I')
        seen = set()
        table = []

        for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            if char.isalpha() and char not in seen:
                seen.add(char)
                table.append(char)
        return [table[i:i+5] for i in range(0, 25, 5)]

    def _find_position(self, char):
        if char == 'J':
            char = 'I'
        for row_idx, row in enumerate(self.table):
            if char in row:
                return row_idx, row.index(char)
        return None, None

    def _process_text(self, text, pad_char='X'):
        text = text.upper().replace('J', 'I')
        result = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i + 1 < len(text) else pad_char
            if a == b:
                result.append(a + pad_char)
                i += 1
            else:
                result.append(a + b)
                i += 2
        if len(result[-1]) == 1:
            result[-1] += pad_char
        return result

    def encrypt(self, plaintext):
        pairs = self._process_text(''.join(filter(str.isalpha, plaintext)))
        ciphertext = ''
        for a, b in pairs:
            r1, c1 = self._find_position(a)
            r2, c2 = self._find_position(b)

            if r1 == r2:
                ciphertext += self.table[r1][(c1 + 1) % 5]
                ciphertext += self.table[r2][(c2 + 1) % 5]
            elif c1 == c2:
                ciphertext += self.table[(r1 + 1) % 5][c1]
                ciphertext += self.table[(r2 + 1) % 5][c2]
            else:
                ciphertext += self.table[r1][c2]
                ciphertext += self.table[r2][c1]
        return ciphertext

    def decrypt(self, ciphertext):
        pairs = self._process_text(ciphertext)
        plaintext = ''
        for a, b in pairs:
            r1, c1 = self._find_position(a)
            r2, c2 = self._find_position(b)

            if r1 == r2:
                plaintext += self.table[r1][(c1 - 1) % 5]
                plaintext += self.table[r2][(c2 - 1) % 5]
            elif c1 == c2:
                plaintext += self.table[(r1 - 1) % 5][c1]
                plaintext += self.table[(r2 - 1) % 5][c2]
            else:
                plaintext += self.table[r1][c2]
                plaintext += self.table[r2][c1]
        return plaintext
