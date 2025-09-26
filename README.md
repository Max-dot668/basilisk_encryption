SUITE ENCRYPTION SCRIPT
by Maximiliano You

This is my project for CPSC 253. It encrypts and decrypts text files using my own algorithm.

Instead of normal letters or numbers, it changes every character into playing card suit symbols. Each character is converted into binary (8 bits) and then split into 2-bit chunks. Each chunk is matched with a suit symbol:

00 = ♠
01 = ♥
10 = ♦
11 = ♣

The decryption just reverses this process.

------------------------------------------------
PROGRAM FLOW
------------------------------------------------
1. User runs the program
2. Program shows menu:
   1) Create a new text file
   2) Encrypt a file
   3) Decrypt a file
3. User chooses an option
4. Program does the selected task:
   - Create: makes a new .txt file
   - Encrypt: reads text file, converts to suits, writes encrypted file
   - Decrypt: reads encrypted file, converts suits back to text, writes decrypted file
5. Done

------------------------------------------------
HOW TO USE
------------------------------------------------
1. Run the program with:
   python main.py

2. Follow the menu instructions.

------------------------------------------------
EXAMPLE
------------------------------------------------
Input text:
hello

Encrypted text (example):
♥♣♠♦♥♣♣♥♦♥...

Decrypted text:
hello

------------------------------------------------
NOTES
------------------------------------------------
- Only works with .txt files.
- If you enter the wrong file type, it will give an error.
