## Hello , Git

# to change the user name 
git config user.name "Bharathesh004"

# To change the global user name 
git config --global user.name "Bharathesh004"


# To chnage the email 
git config user.email "bharathkudupu6360@gmail.com"

# To change the email of global user 
git config --global user.email "bharathkudupu6360@gmail.com"

# to create the repo in git 
git init 


# to set init branch to main
git config --global init.defaultBranch main

# to check the status of the branches on git 
git status 

# to add the file into git repo 
git add filename

# to add all the files into git of current directory 
git add .

# to commit the changes 
git commit -m "First commit"

# to check the logs history in git
git log

# to undo the commits 
git checkout hash-value-of-the-commit

#  to go back the head state 
git checkout main

# to change global author name and email
git config --global author.name "Bharathesh004"

git config --global author.email "bharathkudupu6360@gmail.com"

# to remove local repo 
rm -rf .git
