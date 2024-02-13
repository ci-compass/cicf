# CICF Week 4

The goals for the week 4 lab are to:

1. Create git repositories. Commit changes. Create and merge branches.
1. Create a GitHub account
1. Make a pull request

## Tutorial

This tutorial will focus on one particular tool discussed in the lecture, the Git distributed version control software.
Focusing on this tool makes sense since it is useful for any situation involving sharing text files between people.

We will first set up some preferences for Git.
It needs to know our name and email to tag the changes we make.
This is what I entered, change the name and email to be yours.

    git config --global user.name "Don Brower"
    git config --global user.email "dbrower@nd.edu"

I think the default editor is set to be "nano", but lets make it explicit:

    git config --global core.editor nano

Every Git repository has a notion of a "default branch".
This is kind of the natural starting point for browsing the code.
Most new git repositories use "main" as this branch name.
We will make sure that is also configured for us:

    git config --global init.defaultBranch main

Git tracks changes to the files inside an entire directory.
Lets make a directory to work in.
We will make a new Git repository in this directory for us to practice making commits.

    mkdir week4-test
    cd week4-test
    git init

The "git init" command tells Git that we want to track changes in the week4 directory (and any subdirectories).
Make a file.
It is good for every project to have a README file to contain the project name and a description for it.

    nano README.md

Type some text. I typed the following:

> Week 4 Test
> ======
>
> A repository to test git commands with.

Exit nano by typing CTRL-S to save and then CTRL-X to exit.

Git classifies the files in our directory as _tracked_ or _untracked_.
Tracked files are stored in the repository and have their changes being tracked by Git.
Untracked files are not tracked by Git.
We can ask Git to tell us the status of the files in our directory compared with the repository (which is currently empty).

    git status

It says that we are on the branch "main", that the repository has no commits and that there is an untracked file present.
The untracked file list is a good reminder that a new file has been created and we should either track it, or tell Git to ignore it.
We will tell Git to track this file:

    git add README.md

The `git add` command just tells Git that we want to include this file in our next commit, but doesn't actually save it to the repository.
The `git commit` actually saves files to the repository.

    git commit

When you run this, a text editor will appear.
Git is asking you to type a message to remind you of what this change is doing.
The lines starting with a hash `#` will be removed by Git before saving.
Git puts them there as a reminder of what files this commit will be updating.

A commit message should consist of at least one line giving a brief summary of the changes.
Then if more information is desired, enter a blank line and then write as much as you care to.
Since this is the first commit, nothing has changed yet, so the standard practice is to use "Initial commit".
Exit nano with CTRL-X and save the message.
You've made a commit.

(Run `git status`. Has anything changed?)

We can now ask Git for the repository history with `git log`.

    $ git log
    commit c9e8d3ec39248fbb60c94c7555c61e2812f144 (HEAD -> main)
    Author: Don Brower <dbrower@nd.edu>
    Date:   Fri Jan 27 14:18:27 2023 +0000

        Initial Commit

Every commit has a name consisting of a bunch of random-ish numbers and letters, a date, an author, and 0 or more parent commits.
(It is a SHA1 hash of the contents of the commit, including the current date, committer, etc).
Since this was the first commit, it doesn't have any parent commits.
Most commits will have one parent.
A few may have more than one parent ("merge commits").

Lets make a change to the README file.
Change 'A' the 'The' and add a second line.

    $ git diff
    $ git add README.md
    $ git commit

This makes a second commit.
Notice that we need to "add" the README file, even though it was already "added" and we just changed it.
The add refers to adding it to the next commit.

The "diff" is in a format called a "unified diff".
Lines that were added are prefixed with a plus sign `+`, lines that were removed are prefixed with a minus sign `-`.
You can see when each line in a file was changed by using `git blame`

    git blame README.md

Let's add a second file.
We will add a batch file that makes a list of numbers.

    $ nano make-numbers.sh

Type in:

    #!/bin/bash
    
    seq 100 > numbers.txt

Make the file executable and then run it:

    $ chmod +x make-numbers.sh
    $ ./make-numbers.sh

It will create a `numbers.txt` file.

    $ ls
    $ git status

We want to track the script file and non track the output file:

    $ git add make-numbers.sh
    $ nano .gitignore

In this new file add a single line

    numbers.txt

This will tell git to not track and to ignore this file.

    $ git status

    $ git status
    On branch main
    Changes to be committed:
      (use "git restore –staged <file>..." to unstage)
             new file:    make-numbers.sh

This shows that the git add does not immediately make the commit happen.
Instead it is keeping the file in a "staging area" until the commit command is issued.

    $ nano README.md

    Use the numbers file for test data

    $ git diff
    $ git add README.md
    $ git commit -m "Add make-numbers script"

### Working with GitHub

Most projects are shared using a Git hosting service.
These services just keep a copy of the repository.
One of the biggest is GitHub, and now we will look at how it is used.
There are many open source and open science libraries and applications on GitHub.

First you need to create an account on it if you don't have one already.
Accounts are free. Sign up at [github.com](https://github.com)

Once you have done this we need to add the key on the VM to your GitHub account.
Open firefox and sign in.
Upper left menu > Settings > SSH and GPG Keys

    cat ~/.ssh/id_ed25519.pub

Now lets reset and get a copy of a repository I have prepared:

    $ cd
    $ git clone git@github.com:dbrower/cicf-2024.git

A clone will make a copy of the repository specified onto the VM.
It will also make a subdirectory called "cicf-2024" and check out the most recent commit.
Notice that the local copy of the repository on the VM has a "remote" to the repository we cloned it from.
This is to make it easier to move changes back to the source repository.

    $ cd cicf-2024
    $ git remote –v
    $ git remote rename origin upstream

Lets see if the python file works.

    $ python3 fib.py

It is common to make a branch for a change so that you can make more than one commit.
Then later you can ask people to review the entire branch at once.
The branch serves as a way to keep the commits that you are making off the main branch for the time being.

    $ git checkout -b add-contact-info
    $ nano README.md
    $ git add README.md
    $ git commit

Notice the change is not on the hosting service yet.
To do that I need to copy the change there

    git push upstream add-contact-info

Usually for a project you will not have access rights to add changes to someone else's repository.
The solution is for you to make your own copy of the repository on the hosting service and then put your changes there.
This is called "forking a repository" (in the Github parlance).
[View the repo](https://github.com/dbrower/cicf-2024) on the github service and choose to fork it.

Add the fork "remote" to the checked out repository.

    git remote add origin _your forked repo_

Now push your changes up to your fork of the repo:

    git push origin add-contact-info

View the changes in the browser.

You can then ask owner of the original repository to merge them into their repo.
On GitHub, at least, this is called a "pull request".
The following command will open the web page for your forced copy of the repository and from there you can choose "Create Pull Request".
Choose the "Compare & pull request" button. On the next page make sure the base branch is the main branch in the dbrower copy of the repository. (It will look slightly different from the screenshot since the screenshot is not working from a fork of the repository.)

And then select "Create pull request".


## Resources

It is hard to overstate the importance and usefulness of Git in modern software development.
However, the user interface leaves a lot to be desired.

- Software Carpentry's [Version Control with Git](https://swcarpentry.github.io/git-novice/)
- Roger Dudler's [git - the simple guide](https://rogerdudler.github.io/git-guide/)
- There are many Git hosting sites, these are the big three: [Github](https://github.com), [Gitlab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/)
- Git is by far the most used version control system, but it isn't the only one: [Mercurial](https://www.mercurial-scm.org/), [Fossil](https://www2.fossil-scm.org/home/doc/trunk/www/index.wiki), [Subversion](https://subversion.apache.org/), [CVS]
CVS (ancient, old, please never use)
- [The Biggest and Weirdest Commits in Linux Kernel Git History](https://www.destroyallsoftware.com/blog/2017/the-biggest-and-weirdest-commits-in-linux-kernel-git-history) (2017)

Developers love to design algorithms—including ways that people should organize software development with Git.
- (https://www.atlassian.com/git/tutorials/comparing-workflows)
- [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Github flow](https://docs.github.com/en/get-started/using-github/github-flow)
- There are too many to name. Organizational needs are important, since open source software is developed differently than closed source, and mobile apps are different than webapps. (e.g. Webapps can deploy a new version continuously unlike mobile apps). Scientific software is likewise different since it is usually for a specific purpose.
- [Example](https://github.com/elastic/elasticsearch-formal-models/pull/29) of a GitHub Pull Request and comments

There are lots of coding standards.
- The Python [PEP 8](https://peps.python.org/pep-0008/) standard for the Python standard library.
- Google [Style Guides](https://google.github.io/styleguide/) for many different languages.
- [JPL Institutional Coding Standard for the C Programming Language](https://andrewbanks.com/wp-content/uploads/2019/07/JPL_Coding_Standard_C.pdf)
- [The Power of 10 Rules](https://en.wikipedia.org/wiki/The_Power_of_10:_Rules_for_Developing_Safety-Critical_Code)
- [NASA F' Flight Software Framework](https://nasa.github.io/fprime/UsersGuide/dev/code-style.html)

Issue tracking is basically a big list but with ability to sort based on metadata.

- [Github Issue tracker](https://docs.github.com/en/issues/tracking-your-work-with-issues)
- The big professional grade tracker is Jira, but it is expensive.
- [An epic treatise on scheduling, bug tracking, and triage](https://apenwarr.ca/log/?m=201712)

Testing is a huge area to learn about.

- [PyTest](https://docs.pytest.org/en/stable/contents.html) package
- [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development). Developers love to create methodologies.
- [Checking in on the state of TDD](https://redmonk.com/kholterhoff/2023/07/12/checking-in-on-the-state-of-tdd/) (2023-07-12)
- [Types of tests](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing)

- [Model Checking](https://en.wikipedia.org/wiki/Model_checking) can verify correctness of programs to a specification. In this way it is the other side of the coin from testing. They are based on [temporal logics](https://en.wikipedia.org/wiki/Computation_tree_logic). One example of a model checker is [TLA+](https://lamport.azurewebsites.net/tla/tla.html).


