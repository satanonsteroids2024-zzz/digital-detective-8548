# Mission 5 — Numbers and Data

## 1. Task / objective
Convert numbers between decimal, binary and hexadecimal by hand, check the answers with Python, build a small converter program, and explain how text is stored.

## 2. Work completed
- Did seven conversions by hand and showed the steps for each.
- Checked every one in Python (interactive mode) and compared with my answers. All matched.
- Wrote [number_converter.py](number_converter.py), which asks for a decimal number and prints binary and hexadecimal, and tested it with five valid inputs and three invalid ones.
- Looked up ASCII codes with Python and answered the text-encoding questions.

## 3. Commands / tools used

| Tool / function | Purpose |
|---|---|
| `python3` (interactive mode) | Try expressions and see results immediately |
| `bin(n)` | Turns a whole number into a binary string like `'0b1101'` |
| `hex(n)` | Turns a whole number into a hexadecimal string like `'0xff'` |
| `int(text)` | Turns typed text into a whole number (decimal by default) |
| `int(text, 2)` / `int(text, 16)` | Reads the text as binary / hexadecimal and gives the decimal value |
| `input()` | Asks the user to type something and returns it as text |
| `ord(c)` / `chr(n)` | Character to its code number, and code number back to a character |
| `str.encode('utf-8')` | Shows the actual bytes used to store text |

## 4. My understanding

### Task 5.1 — Conversions by hand

Decimal to binary: divide by 2 again and again, write down the remainders, then read them from the last one to the first.

| Question | Working and answer |
|---|---|
| Decimal 13 to binary | 13 ÷ 2 = 6 remainder **1**<br>6 ÷ 2 = 3 remainder **0**<br>3 ÷ 2 = 1 remainder **1**<br>1 ÷ 2 = 0 remainder **1**<br>Reading the remainders from bottom to top: **1101** |
| Decimal 25 to binary | 25 ÷ 2 = 12 remainder **1**<br>12 ÷ 2 = 6 remainder **0**<br>6 ÷ 2 = 3 remainder **0**<br>3 ÷ 2 = 1 remainder **1**<br>1 ÷ 2 = 0 remainder **1**<br>Bottom to top: **11001** |
| Binary 1010 to decimal | Place values from the right are 1, 2, 4, 8: 1×8 + 0×4 + 1×2 + 0×1 = 8 + 0 + 2 + 0 = **10** |
| Binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 8 + 4 + 0 + 1 = **13** |
| Hexadecimal A to decimal | In hex, A = 10, so the answer is **10** |
| Hexadecimal 1F to decimal | 1×16 + F×1 = 16 + 15 = **31** |
| Binary 1111 to hexadecimal | 1111 is one group of four bits. 8 + 4 + 2 + 1 = 15, and 15 is F in hex, so the answer is **F** |

A check on 25: 16 + 8 + 1 = 25, and in 11001 the 1s sit on the 16, 8 and 1 places. That matches.

### Task 5.2 — Python verification

| Expression tested | Result | Matches my manual answer? |
|---|---|---|
| `bin(13)` | `'0b1101'` | Yes (1101) |
| `bin(25)` | `'0b11001'` | Yes (11001) |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `int("A", 16)` | `10` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(int("1111", 2))` | `'0xf'` | Yes (F) |
| `hex(10)` and `hex(31)` (decimal to hex, going the other way) | `'0xa'` and `'0x1f'` | Yes (A and 1F) |

The `0b` and `0x` at the start only tell Python which number system the text is in. They are not part of the number.

### Task 5.3 — The converter
How `number_converter.py` works:
1. `input()` asks for a decimal number and returns what was typed as text.
2. `int(text)` turns it into a whole number. If it can't, Python raises `ValueError`, which the program catches and prints a friendly message instead of crashing.
3. Negative numbers are rejected, since the task was about positive numbers.
4. `bin(number)` and `hex(number)` produce the binary and hexadecimal text. The program cuts off the first two characters (`0b` or `0x`) with `[2:]` and prints the clean value as well as Python's own form.

How to run it:

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 255 | 11111111 | FF |
| 1024 | 10000000000 | 400 |
| 0 | 0 | 0 |

Invalid input also worked as intended: `abc` and `3.5` printed "That is not a whole number", and `-5` printed the positive-number message.

`bin()` gives the number as a string of 0s and 1s, the base-2 form. `hex()` gives the base-16 form, using the digits 0 to 9 and the letters a to f. Both only change how the same value is written. The value itself is not changed.

### Task 5.4 — How is text stored?
- **ASCII codes:** uppercase `A` is **65** and lowercase `a` is **97** (checked with `ord`). The difference of 32 is the same for every letter pair.
- **Why an encoding standard is needed:** a computer can only store numbers (bits), so every character has to be agreed to match a number. Without one standard, a file written on one computer could show as nonsense on another.
- **A character that is not in basic ASCII:** the rupee sign `₹`. It is Unicode code point 8377 (U+20B9). UTF-8 stores it as 3 bytes, `e2 82 b9`, and trying to encode it as ASCII raised `UnicodeEncodeError`, because basic ASCII only has 128 characters.

## 5. Difficulties faced
- When I first ran Python's interactive mode with the commands piped in, the expressions were not shown next to their results, so the output was hard to read.

## 6. How I resolved them
- I re-ran the checks so that each expression is printed with its result, and saved that in the evidence file.

## 7. Evidence / files
- [number_converter.py](number_converter.py): the converter
- [evidence/mission-05/conversions-and-tests.txt](../evidence/mission-05/conversions-and-tests.txt): Python checks, the converter test runs (valid and invalid) and the encoding experiment

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Pushed to `main` on GitHub and checked there.
