import re

# Binary mapping symbols 
SYMBOLS = { '0': '♔', '1': '♕' }

# Each letter in the alphabet mapped to a number index
letter_to_number = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
                    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
                    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,'X': 23,
                    'Y': 24, 'Z': 25 }


# ================================================================================
# Function implementations
# ================================================================================

def encrypt(text, key):
    ...

def decrypt(ciphertext, key):
    ...

def encrypt_file(input_file, output_file, key):
    ...

def decrypt_file(input_file, output_file, key):
    ...

# ================================================================================
# Helper functions
# ================================================================================

def validate_input(key):
    """
    Raises ValueError if key contains digits.
    Only letters and special characters are allowed 
    """
    pattern = r'\d' # matches digits
    if match := re.search(pattern, key):
        return False
    return True

def binary_conversion(n):
    """
    Returns a string binary represation of a decimal
    number through the eucledian algorithm
    """
    result = ''
    while n != 0:
        result += str(n % 2)
        n = n // 2
    return result[::-1]

# ================================================================================
# Main program 
# ================================================================================
def main():
    print('Suite Encryption Script')
    print('(1) Encrypt a file')
    print('(2) Decrypt a file')

    # user choice with input validation
    while True:
        try:
            choice = int(input('Enter choice here: '))
            if choice in [1, 2]:
                break
            else:
                print('Invalid choice. Please enter 1 or 2')
        except ValueError:
            print('Invalid input. Please enter 1 or 2')



if __name__ == "__main__":
    main()
