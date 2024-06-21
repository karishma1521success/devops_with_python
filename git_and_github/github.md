git - It is a software that is installed locally on your machine and manages the project in your local system

github - It is a hosted service git repository

STAGES 
U - untracked
A - added or staged  {staging area known as Index}
C - commited 

git consists git directory, staging and working tree

Git directory - database to store all the changes/commits and history of the file.

Staging - it takes files to the staging area from the working tree and staging area goes to git directory so by committing changes can store in git repository

working tree - It acts as a sandbox where we can edit the current version of the file. means vs code where we can edit our file.

.gitignore -->> it is a file in which you write file name that you don't want git to track but still want in your directory.

Good commit - 
1. A short description upto 50 characters
2. give a blank line
3. 1 or more paragraphs of the details of change. 
4. each line of paragraph should be less than of 72 characters.

Git Commands

1. git init  -->> to initialize git in your project or to make git available in your project

2. git add . / git add filepath  -->> to adding files and staging them 

3. git commit -m "message"  -->> commit them and make a saved point or check point

4. git log --oneline -->> used to get the current status of saved points and also to get all the saved point
    a.  HEAD --> main  - represents current saved point 
        HEAD is a pointer to the current commit branch
    b. Each saved / checked points has unique ID 
    Note - press q to get out of the command
  
    Note : git log --> used to get all the information about all the saved points like who commit it on which date and time what is the message.

5. git reset --hard HEAD~1 -->   reverting back to previous saved pointf

   git reset --hard/soft/mixed HEAD~no.of steps you want to move back.

6. git status -s -->>  To know the current status of unstaged and staged files.
        a.  ?? - untracked file    A - added     
            AM - added but modified   M - modified
    Tell the status or stages of files before commit and after commit. If you made the commit then run command git status -s that will not show any status.

7. git branch branchName  ->> create new branch

8. git switch branchName -->> to switch to the other branch

9. git merge branchName -->> to merge main with branchName
    a. to merge the branch you have to be on main branch

    b. conflict may occur while merging means main branch and other branch have different code at some line the git get confused which code he has to take.

10. git merge -->> to get all the branches. * - represent the current branch you are in right now.

11. git branch -d branchName -->> to delete the branch
 
12. git switch -C branchName -->> branch will get created and it also get switch to that branch 

Branching - branch is a new and seperate copy of the main branch.

conflit - It is that suitation when main and branch code of some line is different and when try to merge them.
Suppose main 4th line of code and other branch 4th line of code is different then we try to merge both branches git get confused which 4th line of code to be considered. so conflict occurs

Merging techniques --> ff merge, three way merge, squash merge, recursive merge, rebase and merge.

ff merge -- (fast forward merge) new copy don't create just main get updated in memory allocation.

three way merge -- This merging is when main branch and side branch both move one step forward and then we merge both the branches

Stashing :--> Git stash is used to save the files that are made modifications and are not ready to commit. 
            1. Jb bhi aap kisi branch mai ho aor aapne usme kuch code likhaa hao aor aapne usko commit nhai kiyaa hai,, aur aap doosri branch mai jaane ki kohshis krte ho toh git aapko bolta hai ki bhai save nhi changes delete ho aayenge yaah toh hum un changes ko delete hone de yaah draft kr skte hai
            2. draft/stash kiye hue changes na toh delete hote hai naa hi add hote hai woh git ki memory mai jaake store ho jaate hai.
            3. and jb bhi aap us branch mai wapas aao toh un draft messages ko apply kr skte ho.
            4. issi ko stashing bolte hai


13. git stash --> to draft/ stash the modified changes 
    a. after stashing you can switch to the different branch

14. git stash apply--> to apply the draft code in your code

15. git stash clear --> to delete the stash/ draft


