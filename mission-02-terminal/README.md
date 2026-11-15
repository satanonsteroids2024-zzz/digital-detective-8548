# Mission 2 — Terminal and File Management

## 1. Task / objective
Use the Terminal to look around folders, make and manage practice files, see what flags and pipes do, and explain what a package manager is. All the file practice stays inside this repository, in `mission-02-terminal/terminal-practice/`.

## 2. Work completed
- Ran the eight basic operations from Task 2.1, one at a time, and wrote down what each did.
- Made the `terminal-practice` folder and created a text file `notes.txt`, then added a second line without erasing the first.
- Made a backup copy and renamed it, and compared copying with moving.
- Ran `ls` with different flags and piped a long listing into `head`.
- Checked Homebrew's version and package list without installing or removing anything.
- Saved the whole session, with my username removed, in [evidence/mission-02/terminal-session.txt](../evidence/mission-02/terminal-session.txt).

## 3. Commands / tools used

### Task 2.1 — Basic operations

| Operation | Command | What it does | What I observed |
|---|---|---|---|
| Current-directory display | `pwd` | Prints the full path of the folder I am in | Showed the full path ending in `digital-detective-8548` (the part before it is my home folder, redacted in the evidence file) |
| Directory listing | `ls` | Lists files and folders in the current location | Listed `README.md`, `evidence` and the nine mission folders |
| Detailed listing | `ls -l` | Lists with permissions, owner, size and date, one item per line | Each folder started with `d`, the README with `-`, and every line had a size and a modified time |
| Change directory | `cd ..` | Moves up to the parent folder | `pwd` before ended in `mission-02-terminal`, after it ended in `digital-detective-8548`, so the location moved one level up |
| Create directory | `mkdir terminal-practice` | Makes a new folder | No output, but `ls` then showed the new folder |
| Create empty file | `touch original.txt` | Makes an empty file (or updates the time of an existing one) | `ls` showed `original.txt` |
| Copy file | `cp original.txt copy.txt` | Makes a second file with the same contents | Both `original.txt` and `copy.txt` were listed |
| Move / rename file | `mv copy.txt renamed-copy.txt` | Changes the name (or location) of a file | `copy.txt` disappeared and `renamed-copy.txt` appeared |
| Display file contents | `cat original.txt` | Prints a file's contents | Printed nothing, because the file is empty. `wc -c original.txt` confirmed 0 bytes |

### Task 2.2 — Changing files safely (inside `terminal-practice`)

| Step | Command |
|---|---|
| Create a file with one line | `echo "Line one: this is my first line." > notes.txt` |
| Add a second line | `echo "Line two: added without removing line one." >> notes.txt` |
| Show the file | `cat notes.txt` (both lines appeared) |
| Make a backup | `cp notes.txt notes-backup.txt` |
| Rename the backup | `mv notes-backup.txt notes.bak` |

### Task 2.3 — Flags and pipes

| Command | Purpose |
|---|---|
| `ls` | Names only |
| `ls -lah` | Long format (`-l`), including hidden files (`-a`), with human-readable sizes (`-h`) |
| `ls -lah \| head -n 4` | Sends the long listing into `head`, which shows only its first 4 lines |

### Task 2.4 — Package manager

| Command | Purpose |
|---|---|
| `brew --version` | Shows the installed Homebrew version (7.0.13) |
| `brew list --formula \| wc -l` | Counts the command-line packages Homebrew manages (28) |
| `brew list --formula \| head -n 5` | Shows the first five of them |

I did not install or uninstall anything.

## 4. My understanding

**Answers for Task 2.2**
- *Replacing vs adding to the end:* `>` replaces the whole file with the new text, so the old content is gone. `>>` adds the new text at the end and keeps what was already there. That is why `notes.txt` ended up with both lines.
- *Copying vs moving:* a copy leaves the original where it is and makes a second file. A move takes the file away from the old name or place, so only one exists afterwards. Renaming is just moving to a new name in the same folder.
- *What `pwd` tells me:* the full path from the top of the disk to where I am, so I know which folder my next command will act on.
- *Why listing is useful:* it shows me what is in a folder before I change anything, and with `-l` I can also check sizes, dates and permissions.

**Flags.** A flag changes how a command behaves. `ls` alone only prints names. Adding `-l` gives the detailed view, `-a` also shows hidden files (names starting with a dot, like `.git`), and `-h` turns byte counts into sizes like `76B`. In the `-lah` output the first two lines were `.` (the current folder) and `..` (its parent), which plain `ls` hides. I also noticed an `@` after the permission letters on macOS, which I understand means the file has extended attributes.

**Pipes.** The `|` symbol takes the output of the command on its left and feeds it in as the input of the command on the right, instead of printing it on the screen. In `ls -lah | head -n 4`, the left side (`ls -lah`) produces the full listing and the right side (`head -n 4`) cuts it down to the first four lines. Each program does one small job and the pipe joins them.

**Package managers.** A package manager installs, updates and removes software from the command line, and it also works out which other packages a program needs and installs those too. That saves me from downloading installers by hand, makes it easy to update everything with one command, and means a tool can be removed cleanly. Homebrew is the one used on macOS, and it was already installed here.

## 5. Difficulties faced
`cat original.txt` printed nothing, so I wanted to be sure it had worked.

## 6. How I resolved them
The file was empty because I had only created it with `touch`. I ran `wc -c original.txt`, which showed 0 bytes, so the blank output was correct.

## 7. Evidence / files
- [evidence/mission-02/terminal-session.txt](../evidence/mission-02/terminal-session.txt): commands and outputs from the whole session (username redacted)
- [terminal-practice/](terminal-practice/): the folder from the practice, containing `notes.txt`, `notes.bak`, `original.txt` and `renamed-copy.txt`

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Pushed to `main` on GitHub and checked there.
