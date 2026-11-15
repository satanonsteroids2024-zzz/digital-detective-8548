# Mission 6 — Git and GitHub

## 1. Task / objective
Learn the everyday Git workflow (status, stage, commit, history), make a branch, change the root README on that branch, open a Pull Request into `main`, and explain what branches and Pull Requests are for.

## 2. Work completed
- Checked the repository status, staged one specific file, committed it and looked at the history (Task 6.1).
- Created the branch `update-about`, added a "My Learning" section to the root `README.md` on it, committed the change and published the branch to GitHub (Task 6.2).
- Opened a Pull Request from `update-about` into `main` with a short description and looked at the changed file in the PR (Task 6.3).
- Wrote my own one-line Git glossary (Task 6.4).

**Pull Request status: open, not merged.** The assignment says to merge only if the instructor asks for it, and I have not been told to, so I left it open. Link: https://github.com/satanonsteroids2024-zzz/digital-detective-8548/pull/1. Because it is not merged, the "My Learning" section is on the `update-about` branch and not yet on `main`.

## 3. Commands / tools used

| Operation | Command | What it does in my own words |
|---|---|---|
| Check repository status | `git status` (`git status --short`) | Shows which files I changed and which of those are staged and ready to be committed |
| Stage selected changes | `git add <file>` | Puts the chosen file's current changes into the staging area, which is the list of what the next commit will contain |
| Create a commit | `git commit -m "message"` | Saves everything that is staged as one snapshot with a message describing it |
| View commit history | `git log --oneline` | Lists the earlier commits, newest first, one line each with a short ID and the message |
| Create a branch | `git switch -c update-about` | Makes a new branch and moves me onto it |
| List branches | `git branch` | Lists the local branches and marks the current one with `*` |
| See what changed | `git diff --stat` | Summarises which files changed and by how many lines |
| Publish a branch | `git push -u origin update-about` | Uploads the branch and its commits to GitHub and links my local branch to it |
| Open a Pull Request | `gh pr create` (also possible on the GitHub website) | Asks for the changes on one branch to be reviewed and merged into another |
| Look at the PR | `gh pr view`, `gh pr diff` | Shows its status and the changed lines |

## 4. My understanding

### Task 6.4 — Git glossary

| Git operation | One-line explanation |
|---|---|
| Initialise a repository | `git init` turns a normal folder into a Git repository by creating the hidden `.git` folder that stores the history |
| Check status | `git status` tells me what has changed and what is staged |
| Stage changes | `git add` picks which changes will go into the next commit |
| Commit changes | `git commit` saves the staged changes as a snapshot with a message |
| View history | `git log` shows the list of commits that led to the current state |
| Create or list branches | `git switch -c name` (or `git branch name`) creates one, and `git branch` lists them |
| Switch branches | `git switch name` moves me to another branch and changes the files to match it |
| Publish changes | `git push` sends my local commits to the remote repository on GitHub |
| Retrieve remote changes | `git pull` downloads new commits from GitHub and merges them into my branch (`git fetch` only downloads them) |

### Staging vs committing
Staging (`git add`) and committing (`git commit`) are two steps. Staging chooses what goes into the next snapshot, so I can change several files but commit only the one I want. Committing then actually records that staged selection in the history. I can see this in the evidence file: after `git add`, the status changed from ` M` to `M ` (changed but unstaged, then staged), and it only became part of history after `git commit`.

### Branch and Pull Request
- **Branch:** a separate line of work inside the same repository. Commits made on `update-about` do not change `main`, so I can try something without touching the finished version.
- **Pull Request:** a request on GitHub to bring the commits from one branch into another, such as `update-about` into `main`. It shows exactly which lines changed and gives a place to discuss, review and approve before anything is merged.
- **Why they are useful with several people:** everyone can work on their own branch at the same time without overwriting each other, and the Pull Request gives the others a chance to check the work first. If there is a mistake, `main` stays safe.

## 5. Difficulties faced
- Right after I opened the Pull Request it listed two changed files, not one. The extra one was `mission-06-git-github/README.md`.
- GitHub's Pull Request page was slow to update its file count even after I fixed it.

## 6. How I resolved them
- I worked out that I had created `update-about` from a local `main` that was one commit ahead of GitHub's `main`, so that commit was being counted as part of the PR. I pushed `main` to GitHub first. After that, the compare view showed only `README.md` as changed.
- I checked the branch comparison through GitHub's compare view, which showed the right result (one commit ahead, one file changed), while the PR page was still refreshing.

## 7. Evidence / files
- [evidence/mission-06/git-workflow.txt](../evidence/mission-06/git-workflow.txt): the Git commands and outputs from the workflow, the branch publish and the Pull Request check
- Pull Request: https://github.com/satanonsteroids2024-zzz/digital-detective-8548/pull/1 (open)

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Pushed to `main` on GitHub and checked there. The branch `update-about` and its Pull Request are also visible on GitHub.
