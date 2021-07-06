hari = {1: "senin",
2: "selasa",
3: "rabu",
4: "kamis",
5: "jumat",
6: "sabtu",
7: "minggu"}

hari_input = input("Masukkan Nama hari : ")
hari_input_lc = hari_input.lower()
shift_input = input("Masukkan Angka : ")

try:
    shift_input = int(shift_input)
    nomor_hari_input = list(hari.keys())[list(hari.values()).index(hari_input_lc)]
    shift_nomor = (nomor_hari_input + shift_input) % 7
    hari_output = hari[shift_nomor]
    print(f"{shift_input} Hari dari hari {hari_input} adalah {hari_output} ")
except ValueError:
    try:
        shift_input = str(shift_input)
        print("Shift input harus angka")
    except ValueError:
        shift_input = float(shift_input)
        print("Shift input harus angka")