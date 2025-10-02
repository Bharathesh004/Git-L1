# Git Basic Commands to Know

## to change the user name 
git config user.name "Bharathesh004"

## To change the global user name 
git config --global user.name "Bharathesh004"


## To chnage the email 
git config user.email "bharathkudupu6360@gmail.com"

## To change the email of global user 
git config --global user.email "bharathkudupu6360@gmail.com"

## to create the repo in git 
git init 


## to set init branch to main
git config --global init.defaultBranch main

## to check the status of the branches on git 
git status 

## to add the file into git repo 
git add filename

## to add all the files into git of current directory 
git add .

## to commit the changes 
git commit -m "First commit"

## to check the logs history in git
git log

## to undo the commits 
git checkout hash-value-of-the-commit

##  to go back the head state 
git checkout main

## to change global author name and email
git config --global author.name "Bharathesh004"

git config --global author.email "bharathkudupu6360@gmail.com"

## to remove local repo 
rm -rf .git

## to change branch name to main or other 
git branch -M main

## to add the remote repo to the github URL
git remote add origin https://github.com/Bharathesh004/Git-L1.git 

## to push 
git push -u origin main

# to create a new branch in git repo
git branch branch-name

# to switch to the branch 
git checkout branch-name

# To create a branch and switch to that in one go
git checkout -b branch-name

# To create a branch with source branch 
git branch new-branch-name source-branch-name

# To push all the changes from local branch to github branch
git push --set-upstream origin branch-name

# Alternate to push all the changes from local-branch to github branch
git push -u origin branch-name

# To merge all the changes of sub branches of your branch 
git pull

# To merge two branches 
git checkout branch-to-merge
git merge branch-to-merge-with

# Alternate to merge 
git checkout branch-to-merge
git pull origin branch-to-merge-with
