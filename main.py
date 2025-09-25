# -------------------------
# Suite-symbol recursive encryption
# -------------------------

# 2-bit suit tokens
SUITS = {
    "00": "♠",
    "01": "♥",
    "10": "♦",
    "11": "♣"
}

# Reverse mapping for decryption
REVERSE_SUITS = {v: k for k, v in SUITS.items()}


# -------------------------
# Helper functions
# -------------------------

def to_binary_8bit(n):
    """Manual decimal -> 8-bit binary string."""
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n = n // 2
    while len(bits) < 8:
        bits = "0" + bits
    return bits


def encrypt_recursive(text):
    if text == "":
        return ""  # base case

    first_char = text[0]
    ascii_code = ord(first_char)
    binary = to_binary_8bit(ascii_code)

    if len(binary) % 2 != 0:
        binary += "0"

    suits = ""
    i = 0
    while i < len(binary):
        chunk = binary[i:i+2]
        suits += SUITS[chunk]
        i += 2

    return suits + encrypt_recursive(text[1:])


def decrypt_recursive(symbols):
    if symbols == "":
        return ""  # base case

    first_four = symbols[:4]  # 4 suits = 8 bits
    binary = ""
    for s in first_four:
        binary += REVERSE_SUITS[s]

    char = chr(int(binary, 2))
    return char + decrypt_recursive(symbols[4:])


def validate_txt_file(filename):
    """Ensure the file has a .txt extension."""
    if not filename.lower().endswith(".txt"):
        print(f"Error: '{filename}' is not a .txt file.")
        return False
    return True


# -------------------------
# File handling
# -------------------------

def create_text_file():
    filename = input("Enter the name of the new text file (with .txt): ")
    if not validate_txt_file(filename):
        return
    content = input("Enter the text you want to put in the file:\n")
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"File '{filename}' created successfully!")
    except Exception as e:
        print(f"Error creating file: {e}")


def encrypt_file(input_file, output_file):
    if not validate_txt_file(input_file) or not validate_txt_file(output_file):
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
        return

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(encrypt_recursive(line))
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")
        return

    print(f"File encrypted successfully -> {output_file}")


def decrypt_file(input_file, output_file):
    if not validate_txt_file(input_file) or not validate_txt_file(output_file):
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
        return

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(decrypt_recursive(line))
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")
        return

    print(f"File decrypted successfully -> {output_file}")


# -------------------------
# Main menu
# -------------------------

def main():
    print("Suite Encryption Script")
    print("(1) Create a new text file")
    print("(2) Encrypt a file")
    print("(3) Decrypt a file")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_text_file()
    elif choice == "2":
        input_file = input("Enter the input file name: ")
        output_file = input("Enter the output file name: ")
        encrypt_file(input_file, output_file)
    elif choice == "3":
        input_file = input("Enter the input file name: ")
        output_file = input("Enter the output file name: ")
        decrypt_file(input_file, output_file)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
