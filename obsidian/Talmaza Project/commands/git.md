### SETUP
Configuring user information used across all local repositories
```git
git config --global user.name “[firstname lastname]”
```
set a name that is identifiable for credit when review version history
```git
git config --global user.email “[valid-email]”
```
set an email address that will be associated with each history marker

---
### SETUP & INIT
Configuring user information, initializing and cloning repositories
```git
git init [name-of-project-or-folder-will-create]
```
or
```git
git init
```
The second one initialize an existing directory as a Git repository
```git
git clone [url]
```
retrieve an entire repository from a hosted location via URL

---
### STAGE & SNAPSHOT
Working with snapshots and the Git staging area
```git
git status
```
show modified files in working directory, staged for your next commit
```git
git add [file]
```
add a file as it looks now to your next commit (stage) or using wildcard \* for all not added
```git
git reset [file]
```
unstage a file while retaining the changes in working directory
```git
git commit -m “[descriptive message]”
```
commit your staged content as a new commit snapshot

---
### BRANCH & MERGE
Isolating work in branches, changing context, and integrating changes
```git
git branch
```
list your branches. a * will appear next to the currently active branch
```git
git branch [branch-name]
```
create a new branch at the current commit
```git
git checkout
```
switch to another branch and check it out into your working directory
```git
git merge [branch]
```
merge the specified branch’s history into the current one
```git
git log
```
show all commits in the current branch’s history

---
### SHARE & UPDATE
Retrieving updates from another repository and updating local repos
```git
git remote add [alias] [url]
```
add a git URL as an alias
```git
git fetch [alias]
```
fetch down all the branches from that Git remote
```git
git merge [alias]/[branch]
```
merge a remote branch into your current branch to bring it up to date
```git
git push [alias] [branch]
```
Transmit local branch commits to the remote repository branch
```git
git pull
```
fetch and merge any commits from the tracking remote branch

---
### TEMPORARY COMMITS
Temporarily store modified, tracked files in order to change branches
```git
git stash
```
Save modified and staged changes
or
```git
git stash save "description for the stash"
```
```git
git stash list
```
list stack-order of stashed file changes
```git
git stash pop
```
write working from top of stash stack (the last one)
or
```git
git stash pop stash@{[id]}
```
choose the stash you want by id
```git
git stash apply
```
write working from top of stash stack (the last one), wthout removing it from stash list
or
```git
git stash apply stash@{[id]}
```
choose the stash you want by id, wthout removing it from stash list
```git
git stash drop
```
discard the changes from top of stash stack
or
```git
git stash drop stash@{[id]}
```
choose the stash you want by id
```git
git stash clear
```
clear all the stash

---
### Restore And Clean
```git
git restore --staged [file]
```
to remove files from stage to be untracked
```git
git clean -n
```
to see the files that will be clean from unstage/untracked
```git
git clean -f
```
to force to clean them (delete them)

---
### reset
```git
git reset --hard [25e22eb39a6589b2439eb2ad6cbea8918ef5e658]
```
to return back and delete all old commits

---
### ignore
make file named ".gitignore", and write in it the files that you want to ignore it
```gitignore
koko.txt
```
this will ignore file koko.txt only
```gitignore
koko.txt
*.koko
```
so all files has this extention will be ignored
```gitignore
koko.txt
*.koko
!vip.koko
```
this means all files has this extention will be ignored except vip.koko
```gitignore
koko.txt
*.koko
!vip.koko
env/
```
this means it will ignore folder "env" and it's contents

```gitignore
git add -f koko.txt
```
this will force to add it