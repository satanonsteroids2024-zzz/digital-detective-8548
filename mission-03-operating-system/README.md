# Mission 3 — Operating System

## 1. Task / objective
Find out which operating system I am running, which account is active, how much storage is free and what the machine is doing right now. Then look at processes, paths and file permissions, and explain what an operating system is responsible for.

## 2. Work completed
- Collected system information from the Terminal: OS version, current account, disk space and a snapshot of activity. I replaced personal details with `[redacted]` before saving them.
- Listed running processes and found their PIDs.
- Moved between the project folder and a subfolder and watched the path change.
- Looked at the permission letters of a practice file and a practice folder.
- Filled in the table of operating-system responsibilities.

## 3. Commands / tools used

| Command | Purpose |
|---|---|
| `sw_vers` | Shows the macOS name and version |
| `uname -srm` | Shows the kernel name, release and CPU architecture |
| `whoami` | Shows which user account I am logged in as |
| `df -h /` and `df -h /System/Volumes/Data` | Shows disk size, used and available space in readable units |
| `top -l 1 -n 0` | Prints one snapshot of system activity and then exits |
| `ps -axo pid,comm` | Lists every running process with its PID and command name |
| `pwd`, `cd` | Show and change the current location |
| `ls -l`, `ls -ld` | Show permissions, owner and size of a file or folder |

## 4. My understanding

### Task 3.1 — System information

| Information explored | What it tells me | My observation (privacy-safe) |
|---|---|---|
| Operating system / system details | Which OS and version is running, and on what kind of processor | macOS 27.2 (build 26B123), Darwin kernel 27.2.0, `arm64` (Apple silicon) |
| Current account identity | Which user account is running my commands, which decides what I am allowed to touch | `[redacted]` |
| Available and used storage | How much disk space is taken and how much is left | The disk is about 926 GiB. `df -h /` showed 13 GiB used and 456 GiB available. That "used" figure is only for the system volume, so I also checked the Data volume (where my own files are) to get the fuller picture, in the evidence file. |
| System activity snapshot | How busy the computer is right now | 831 processes (3 running, 828 sleeping), load average about 2.2, CPU about 74% idle, and 14 GB of the 16 GB memory in use |

### Task 3.2 — Processes
I used the Terminal (`ps`) for the process list instead of Activity Monitor.

- **What is a process?** A program that is currently running. The program on disk is just a file, and it becomes a process when the operating system loads it into memory and starts running it. One program can have several processes.
- **What does the PID column represent?** The process identifier, a unique number the OS gives each process so it can be told apart, watched and stopped. PIDs are different each time the computer starts.
- **Two processes on my computer:** `launchd` with PID 1, which is the first process macOS starts and which then starts many others, and `Finder` with PID 680 at the time, which is the program that shows my files and folders. Others in the list were background ones like `logd` (system logging) and `configd` (network and system configuration).

### Task 3.3 — Paths and permissions
- **Absolute path:** a path that starts from the very top of the file system (`/`) and works down, so it means the same thing wherever I am. Example from my project: `/Users/[redacted]/Desktop/digital-detective-8548/mission-03-operating-system`
- **Relative path:** a path that starts from the folder I am currently in. Example from my project: from the project folder, `mission-03-operating-system` or `mission-02-terminal/terminal-practice/notes.txt`. From inside a mission folder, `..` means the project folder above it.
- **What I observed:** `cd mission-03-operating-system` then `pwd` ended with `/mission-03-operating-system`, and `cd ..` took me back to `/digital-detective-8548`.

Permissions for `mission-02-terminal/terminal-practice/notes.txt`:

```
-rw-r--r--  1 [redacted]  staff  76  notes.txt
```

| Part | Meaning |
|---|---|
| `-` | It is a regular file (a folder would start with `d`) |
| `rw-` | Owner can read and write, but cannot execute |
| `r--` | The group can only read |
| `r--` | Everyone else can only read |

So as the owner I can read and edit `notes.txt` but cannot run it as a program. For the folder `terminal-practice` the owner part is `rwx`. The `x` on a folder means I can go into it. I did not change any permissions.

| Permission | Meaning | Example |
|---|---|---|
| r (read) | The contents can be read | Opening a text file |
| w (write) | The file can be changed | Editing a text file |
| x (execute) | The file can be run, or a folder can be entered | Running a script |

### Task 3.4 — Operating-system responsibilities

| OS responsibility | My explanation | Example |
|---|---|---|
| Process management | Decides which running programs get the processor and for how long, and starts and stops them | With Chrome, the editor and the Terminal all open, macOS switches the processor between them so they all seem to run at once |
| Memory management | Gives each program its own part of RAM, keeps them from overwriting each other and frees memory when a program closes | The 14 GB in use in my snapshot is shared out between all the processes |
| Device management | Talks to hardware through drivers so programs don't need to know how each device works | When I press a key or play a sound, the OS handles the keyboard and speakers for the app |
| File management | Keeps track of where files live on the disk, their names, folders and permissions | `mkdir`, `cp` and `mv` in Mission 2 all went through the OS file system |
| User interface / shell | Gives me a way to talk to the computer, either by windows and clicks or by typing commands | The desktop and Finder are the graphical interface, and Terminal with zsh is the command-line shell |
| Security and permissions | Decides who can read, change or run what, and keeps accounts and programs apart | `rw-r--r--` on `notes.txt` lets only the owner change it |

## 5. Difficulties faced
- The first process search I wrote only matched names without spaces, so it missed apps like Google Chrome.
- `df -h /` showed only 13 GiB used on a 926 GiB disk, which didn't match how I thought my disk was being used.

## 6. How I resolved them
- I used the exact process names `launchd` and `Finder`, which were found, and listed other background processes from the top of the process list instead.
- I checked `df -h /System/Volumes/Data` as well. As far as I understand, macOS keeps the system and my own data on separate volumes of one disk. The root `/` line only reports the system volume, so I read both lines together.

## 7. Evidence / files
- [evidence/mission-03/os-observations.txt](../evidence/mission-03/os-observations.txt): the command outputs from this mission, with the account name, home folder path and any addresses redacted

## 8. Commit details
- Commit message: `Document operating system and file management`
- Pushed to `main` on GitHub and checked there.
