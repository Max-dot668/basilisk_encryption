SUITE ENCRYPTION SCRIPT
by Max You

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
+------------------+
|   User runs app  |
+------------------+
          |
          v
+------------------+
|   Show menu      |
|  (1, 2, or 3)    |
+------------------+
   |     |      |
   |     |      |
   v     v      v
Create Encrypt Decrypt
 File   File    File
   |     |      |
   |     v      v
   |   Read input file
   |     |
   |     v
   |  Convert text
   |   -> binary
   |   -> suits ♠♥♦♣
   |     |
   |     v
   |  Write encrypted file
   |            |
   |            v
   |      Decrypt reverses
   |        process back
   v
 Done

------------------------------------------------
HOW TO USE
------------------------------------------------
1. Run the program with:
   python main.py

2. You will see a menu with three options:
   (1) Create a new text file
   (2) Encrypt a file
   (3) Decrypt a file

3. Type the number for what you want to do and follow the prompts.

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
