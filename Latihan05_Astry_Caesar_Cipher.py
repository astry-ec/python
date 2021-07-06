#menggunakan konversi ASCII Unicode; y = ord('A') = 65; y = ord('a') = 97

text = input("Masukan Kata : ")
shift = int(input("Masukan Angka : "))

encryption = ""

for current in text:
    if current.islower():
        current_unicode = ord(current)
        current_index = ord(current) - ord("a")
        caesar_index = (current_index + shift) % 26
        caesar_unicode = caesar_index + ord("a")
        caesar_character = chr(caesar_unicode)
        encryption = encryption + caesar_character

    elif current.isupper():
        current_unicode = ord(current)
        current_index = ord(current) - ord("A")
        caesar_index = (current_index + shift) % 26
        caesar_unicode = caesar_index + ord("A")
        caesar_character = chr(caesar_unicode)
        encryption = encryption + caesar_character

    else:
        encryption += current

print("Hasil Caesar Cipher : ",encryption)