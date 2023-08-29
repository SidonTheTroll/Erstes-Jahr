# Basic Commands:

`git init`: Initialize a new Git repository.  
`git clone <repository_url>`: Clone a remote repository to your local machine.  
`git add <file>`: Start tracking changes in a file.  
`git add .`: Stage all changes for commit.  
`git commit -m "Commit message"`: Commit staged changes with a message.  
`git status`: Check the status of your working directory.  
`git diff`: Show changes between commits, commit and working tree, etc.  
`git log`: View commit history.  
`git log --oneline`: View simplified commit history.  

# Branching and Merging:

`git branch`: List all branches in the repository.  
`git branch <branch_name>`: Create a new branch.  
`git checkout <branch_name>`: Switch to a different branch.  
`git checkout -b <branch_name>`: Create and switch to a new branch.  
`git merge <branch_name>`: Merge changes from one branch into the current branch.  
`git merge --no-ff <branch_name>`: Merge with a new commit, even for fast-forward.  
`git pull`: Fetch and merge changes from a remote repository.  
`git push`: Push local commits to a remote repository.  

# Updating and Undoing:

`git fetch`: Get the latest changes from a remote repository without merging.  
`git reset <file>`: Unstage changes from a file.  
`git reset`: Unstage all changes.  
`git reset --hard <commit_hash>`: Reset to a specific commit, discarding changes.  
`git reset --soft <commit_hash>`: Reset to a specific commit, keeping changes staged.  
`git commit --amend`: Modify the last commit.  
`git revert <commit_hash>`: Create a new commit that undoes changes from a specific commit.  
`git stash`: Temporarily save changes to work on something else.  
`git stash apply`: Apply the most recent stash.  
`git stash pop`: Apply and remove the most recent stash.  

# Remote Repositories:

`git remote -v`: List remote repositories.  
`git remote add <name> <repository_url>`: Add a new remote repository.  
`git remote remove <name>`: Remove a remote repository.  
`git push <remote_name> <branch_name>`: Push local commits to a remote branch.  
`git pull <remote_name> <branch_name>`: Pull changes from a remote branch.  
`git fetch <remote_name>`: Fetch changes from a remote repository.  

# Tagging and Releases:

`git tag`: List all tags in the repository.  
`git tag <tag_name>`: Create a new tag on the current commit.  
`git tag -a <tag_name> -m "Tag message"`: Create an annotated tag with a message.  
`git push --tags`: Push tags to a remote repository.  

# Configuration and Information:

`git config --global user.name "Your Name"`: Set your name for commits.  
`git config --global user.email "youremail@example.com"`: Set your email for commits.  
`git config --list`: List your Git configuration.  
`git remote show <remote_name>`: Show information about a remote repository.  
`git show <commit_hash>`: Show detailed information about a commit.

