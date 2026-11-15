# The Digital Detective

My Diwali independent learning assignment. The idea is to investigate how my own computer works: what it does with input and output, how the Terminal and the operating system behave, how programs run, how numbers and text are stored, how Git and GitHub work, and how computers talk to each other. I do it as a series of small missions and keep the notes, outputs and code in this repository.

- **Name:** H S Bharath Surya
- **USN:** ends in 8548
- **Repository:** digital-detective-8548

## How this repository is organised

Every mission has its own folder with its own README. I finish a mission, write it up, check the files for anything private, then commit and push it before I start the next one. So each mission has its own commit in the history, and the commits are in mission order.

## My Learning

- A commit is a saved snapshot, and each mission gets its own, so the history shows my work in order. Staging first (`git add`) lets me choose exactly what goes into a commit.
- Paths and redirects matter more than I expected. An absolute path works from anywhere while a relative one depends on where I am, and `>` replaces a file while `>>` adds to the end of it.
- Numbers on a computer are just bits. I converted 13 to binary by dividing by 2 and checked it with Python, and I saw that text also has to be turned into numbers (A is 65) before it can be stored.

## Mission index

| # | Mission | Folder |
|---|---|---|
| 0 | Repository and workspace setup | [mission-00-setup](mission-00-setup/README.md) |
| 1 | Computer fundamentals and IPOS | [mission-01-computer-basics](mission-01-computer-basics/README.md) |
| 2 | Terminal and file management | [mission-02-terminal](mission-02-terminal/README.md) |
| 3 | Operating system, processes and permissions | [mission-03-operating-system](mission-03-operating-system/README.md) |
| 4 | How programs run | [mission-04-programs](mission-04-programs/README.md) |
| 5 | Number systems, Python and text encoding | [mission-05-numbers-data](mission-05-numbers-data/README.md) |
| 6 | Git, GitHub, branches and Pull Requests | [mission-06-git-github](mission-06-git-github/README.md) |
| 7 | Computer networks | [mission-07-networking](mission-07-networking/README.md) |
| 8 | Final review and submission | [mission-08-final-report](mission-08-final-report/README.md) |

Screenshots and selected outputs go in [evidence](evidence/). I redact anything personal before adding it.

## Progress

| Mission | Status |
|---|---|
| 0 | Done |
| 1 | Done |
| 2 | Done |
| 3 | Done |
| 4 | Done |
| 5 | Done |
| 6 | Done (Pull Request open, not merged) |
| 7 | Done |
| 8 | Done |

## Topics explored

- How a computer works: input, processing, output and storage (IPOS), hardware and software types
- Terminal basics: navigating, creating, copying and moving files, flags and pipes, package managers
- The operating system: processes and PIDs, storage, absolute and relative paths, file permissions, what the OS is responsible for
- How programs run: running a Python script, compilers compared with interpreters
- Number systems (decimal, binary, hexadecimal), checking conversions in Python, and how text is stored (ASCII and UTF-8)
- Git and GitHub: staging, commits, history, branches and a Pull Request
- Computer networks: LAN, MAN, WAN, DNS, routers, protocols, packet switching, client-server, and what happens when a website opens

## Running the number converter

The converter is in [mission-05-numbers-data](mission-05-numbers-data/). It needs Python 3 and nothing else.

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

It asks for a decimal number, for example `25`, and prints the binary (`11001`) and hexadecimal (`19`) forms. Anything that isn't a whole number, and negative numbers, get a short message instead of a result.

## What I learned

The biggest thing was seeing that the computer is a chain of simple steps. A key press becomes a signal, the operating system passes it to a program, the program works on it in memory, and the result is shown and saved. The Terminal showed me the same chain in text form, with commands joined by pipes, and with permissions deciding who may touch which file. Converting 13 to binary by hand and checking it in Python made it clear that everything on a computer, text included, is stored as numbers. Git added the habit of saving work in small commits with a clear message, so the history reads like a log of what I did. The details of each mission, including the problems I ran into, are in the mission READMEs.

