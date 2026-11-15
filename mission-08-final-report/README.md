# Mission 8 — Final Report

## 1. Task / objective
Review the whole repository, make the root README useful for someone visiting for the first time, check that every mission has its own commit on GitHub, and get the repository ready to submit.

## 2. Work completed
- Went through every mission folder and README against the structure in the assignment.
- Updated the root README: introduction, mission index, progress table, list of topics, how to run the number converter and a short summary of what I learned.
- Re-ran the number converter from its own folder with three new values (7, 100 and 4095) and got correct results.
- Checked every link in the READMEs, checked that every mission README has all eight headings, and searched all files and the full commit history for my account name, device name and network addresses. Nothing private turned up.
- Made a few small corrections (listed below).

### Status of each mission

| Mission | Status | Commit message | Commit |
|---|---|---|---|
| 0 Setup | Complete | Set up Digital Detective mission structure | `9a05424` |
| 1 Computer basics | Complete | Complete computer basics and IPOS mission | `2b1f417` |
| 2 Terminal | Complete | Complete Terminal and file management mission | `3737986` |
| 3 Operating system | Complete | Document operating system and file management | `2211378` |
| 4 Programs | Complete | Compare compilers and interpreters | `118b88d` |
| 5 Numbers and data | Complete | Build number converter and practise data representation | `dc8984a` |
| 6 Git and GitHub | Complete, Pull Request open and not merged | Complete Git and GitHub collaboration mission | `1d74958` |
| 7 Networking | Complete | Explain networking concepts and website communication | `38616f6` |
| 8 Final report | Complete | Complete final report and verify assignment submission | see the latest commit in the history |

For Mission 6 the branch `update-about` has its own commit (`09d568f`), and the Pull Request is https://github.com/satanonsteroids2024-zzz/digital-detective-8548/pull/1.

### Corrections made
- `c8be28c`: removed one line from the Mission 5 difficulties that was not accurate.
- `fbb28a7`: updated the progress table, which I had not changed after Mission 1.
- This commit: deleted the placeholder file `evidence/.gitkeep` now that the folder has real files, as I planned in Mission 0, and reworded the difficulty line in the Mission 2 README.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `git log --format=...` | List the commit history to match every mission to its commit |
| `git log -p` with `grep` | Search the full history for private details |
| `python3 number_converter.py` | Re-test the converter |
| `wc -c`, `grep` | Check that every README has content and the required headings |
| `git rm` | Remove the placeholder `.gitkeep` |
| `git add`, `git commit`, `git push` | Save and publish the final changes |
| `gh` (GitHub CLI) | Check the repository, its commits and the Pull Request on GitHub |

## 4. My understanding

### Final checklist

- [x] All mission folders are present and each has its own `README.md`.
- [x] Every mission README has the task, commands/tools, understanding and difficulties sections.
- [x] Every mission has its own meaningful commit, and all of them are pushed.
- [x] IPOS, hardware, software and computer-system examples are in Mission 1.
- [x] Terminal operations, file management, flags and pipes are explained in Mission 2.
- [x] The operating system, processes, paths, storage and permissions are covered in Mission 3.
- [x] Compiler and interpreter are compared in Mission 4.
- [x] Number conversions have working and Python verification in Mission 5.
- [x] `number_converter.py` runs with more than three test values.
- [x] The Git commit history, the branch and the Pull Request are visible on GitHub.
- [x] LAN, MAN, WAN, DNS, router, protocols and client-server are explained in Mission 7.
- [x] The root README explains the project and how to run the converter.
- [x] Personal information has been removed from outputs. Evidence files have my account name replaced with `[redacted]`.
- [x] All final changes are committed and pushed.

### What I take from the whole assignment
Each mission was one part of the same picture, from what a computer is made of, to how the operating system runs programs on it, to how data and text are stored, to how computers talk to each other over networks. The repository itself was the practice for the last part, because I had to save each mission with Git, publish it, and check it on GitHub before moving on.

## 5. Difficulties faced
- The Pull Request page on GitHub kept showing two changed files and an "unknown" merge status after I had fixed the branch problem, although the branch comparison showed one changed file.
- Writing about my own computer meant being careful each time not to paste anything that identifies me.

## 6. How I resolved them
- I compared the branches with GitHub's compare view, which showed the correct result. The Pull Request page only updated after I waited and then closed and reopened the Pull Request, and it now shows one changed file and says it can be merged.
- I used commands that print only what I need (for example `dig ... +noall +answer`), replaced my account name with `[redacted]`, and ran searches over the files and history before every commit.

## 7. Evidence / files
- Evidence for each mission is in [evidence/](../evidence/): [mission-01](../evidence/mission-01/system-check.txt), [mission-02](../evidence/mission-02/terminal-session.txt), [mission-03](../evidence/mission-03/os-observations.txt), [mission-04](../evidence/mission-04/hello-run.txt), [mission-05](../evidence/mission-05/conversions-and-tests.txt), [mission-06](../evidence/mission-06/git-workflow.txt) and [mission-07](../evidence/mission-07/network-observations.txt).
- Repository URL to submit: https://github.com/satanonsteroids2024-zzz/digital-detective-8548

## 8. Commit details
- Commit message: `Complete final report and verify assignment submission`
- Pushed to `main` on GitHub and checked there. The repository is public.
