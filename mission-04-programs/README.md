# Mission 4 — How Programs Run

## 1. Task / objective
Write and run a one-line Python program, then compare how a compiler and an interpreter turn source code into something the computer can run.

## 2. Work completed
- Created [hello.py](hello.py) with one line that prints `Hello from Python`.
- Ran it with Python 3 from the Terminal and confirmed the message appeared.
- Filled in the compiler and interpreter comparison table and wrote the short explanation.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `python3 hello.py` | Runs the file with the Python 3 interpreter |
| `python3 --version` | Shows which Python version ran it (3.14.7) |
| `cat hello.py` | Shows the file contents so the evidence is complete |
| VS Code | Where the code is written |

The program is the single line `print("Hello from Python")`. Output:

```
Hello from Python
```

## 4. My understanding

### Task 4.2 — Compiler vs interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | The whole program is translated before it runs. Running is a separate, later step. | The program is read and carried out while it runs, one statement at a time |
| Typical output | A separate executable file or machine code that can run by itself | No separate file needed. The result of running the program is the output |
| One example | C, compiled with a compiler such as `gcc` or `clang` | Python, run with `python3` |
| One advantage | The finished program usually runs faster, and errors in the code are caught before it starts | I can run code straight away and see errors at the exact line, which is good for learning and testing |

**Explanation in my own words.** A compiler translates the whole source code into machine code first, and then I run the result. An interpreter skips that step and executes the code directly, line by line, each time I run it. That is why `python3 hello.py` ran instantly with no extra file made, while a C program would first need compiling. The table shows the trade-off: compiled programs tend to be faster, interpreted ones are quicker to try out. Real languages often mix both. As far as I understand, Python first turns my code into a simpler internal form called bytecode and then its interpreter runs that.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [hello.py](hello.py): the program
- [evidence/mission-04/hello-run.txt](../evidence/mission-04/hello-run.txt): the program, its output and the Python version

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Pushed to `main` on GitHub and checked there.
