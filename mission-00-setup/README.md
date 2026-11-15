# Mission 0 — Setup

## 1. Task / objective
Make a public GitHub repository named after the assignment plus the last four digits of my USN, and set up one folder per mission so all the later work has a place to go.

Repository name: `digital-detective-8548`

## 2. Work completed
- Checked that Python 3 and Git are installed (versions below).
- Made a local folder called `digital-detective-8548`, the same name as the repository, and kept all the work inside it.
- Created the nine mission folders. Each one has an empty `README.md` for now, and `mission-05-numbers-data` also has an empty `number_converter.py`.
- Created an `evidence/` folder for screenshots and outputs. Git does not keep empty folders, so it holds a hidden `.gitkeep` file.
- Wrote the root `README.md`: title, short description, my name and the end of my USN, the mission index with links, and a note that each mission is committed on its own.
- Ran `git init`, made the first commit, created the public repository on GitHub with the same name (without adding a README there, since I already had one) and pushed.
- Opened the repository on GitHub and checked that the folders and the commit show up.

What the folder looks like:

```
digital-detective-8548/
├── README.md
├── evidence/
├── mission-00-setup/README.md
├── mission-01-computer-basics/README.md
├── mission-02-terminal/README.md
├── mission-03-operating-system/README.md
├── mission-04-programs/README.md
├── mission-05-numbers-data/
│   ├── README.md
│   └── number_converter.py
├── mission-06-git-github/README.md
├── mission-07-networking/README.md
└── mission-08-final-report/README.md
```

## 3. Commands / tools used
| Command / tool | What I used it for |
|---|---|
| `python3 --version` | Check that Python 3 is installed |
| `git --version` | Check that Git is installed |
| `mkdir` | Make the project folder and the mission folders |
| `: > filename` | Make an empty file from the Terminal (same result as `touch`) |
| `git init` | Start tracking the folder with Git |
| `git add` | Stage the files for the first commit |
| `git commit` | Save the staged files as a commit with a message |
| `gh repo create` | Create the public repository on GitHub and connect the local folder to it as `origin` |
| `git push` | Upload the commit to GitHub |

Versions found:

| Tool | Version |
|---|---|
| Python | 3.14.7 |
| Git | 2.54.0 (Apple Git-157) |

## 4. My understanding
A repository is a project folder that Git keeps a history of. Every commit is a saved snapshot, so I can look at an older version or undo a mistake. Putting it on GitHub also gives me an online copy that my instructor can open.

The folders are split by mission because each mission is about a different topic and has its own notes, files and commit. It keeps things easy to find, and the commit history reads like a log of the assignment from start to finish.

## 5. Difficulties faced
- My computer is signed in to two GitHub accounts, so I had to be careful that the repository went to the right one.
- Git ignores empty folders, so `evidence/` would not have shown up on GitHub with nothing in it.

## 6. How I resolved them
- I created the repository by naming the account explicitly instead of relying on whichever account was active, then checked the URL after.
- I added an empty `.gitkeep` file inside `evidence/` so Git would track the folder. I deleted it at the end (Mission 8) once the folder had real evidence files in it.

## 7. Evidence / files
- [Root README](../README.md)
- The nine mission folders and the `evidence/` folder, as listed in the tree above

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Pushed to the `main` branch on GitHub, and I confirmed the commit and all the folders are visible in the repository.
