# CICF Week 4

The goals for the week 4 lab are to:

1. Create git repositories. Commit changes. Create and merge branches.
1. Create a GitHub account
1. Make a pull request

## Tutorial

This tutorial will focus on one particular tool discussed in the lecture, the Git distributed version control software.
Focusing on this tool makes sense since it is useful for any situation involving sharing text files between people.

To really start using Git we need to configure it with a name and email to use
to tag the changes we make.
This is what I entered, change the name and email to be yours.

    git config --global user.name "Don Brower"
    git config --global user.email "dbrower@nd.edu"

While the default editor is set to be "nano", lets make it explicit:

    git config --global core.editor nano

Every Git repository has a notion of a "default branch".
This is kind of the natural starting point for browsing the code.
Most new git repositories use "main" as this branch name.
We will make sure that is configured for us:

    git config --global init.defaultBranch main

Git tracks changes to the files inside an entire directory.
Lets make a directory to work in.
We will make a new Git repository in this directory for us to practice making commits.

    $ mkdir first-repo
    $ cd first-repo
    $ git init
    Initialized empty Git repository in /home/cicf/first-repo/.git/

The "git init" command tells Git to make a new repository in the current
directory. This new repository is completely empty—none of the files have been added to it yet.
It is good for every project to have a README file to contain the project name and a description for it.

    nano README.md

Type the following:

```
First Repository
================

A repository to test git commands.
```

Exit nano by typing CTRL-S to save and then CTRL-X to exit.

Git classifies the files in our directory as either _tracked_ or _untracked_.
Tracked files are stored in the repository and have their changes being tracked by Git.
Untracked files are not tracked by Git.
We can ask Git to tell us the status of the files in our directory.

    $ git status
    On branch main
    
    No commits yet
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            README.md
    
    nothing added to commit but untracked file present (use "git add" to track)

It says that we are on the branch "main", that the repository has had no commits
yet and that there is an untracked file present.
The untracked file list is a good reminder that a new file has been created and
we should either track it or tell Git to ignore it.
Tell Git to track this file:

    git add README.md

The `git add` command instructs Git to include the changes we've made to this
file in the next commit, but doesn't actually save it to the repository.
The `git commit` will actually save the changes into the repository.

    git commit

A text editor will appear when you run this.
The editor is for you to type a message to describe this change.
Not all of the text will be saved, though.
The lines starting with a hash `#` will be removed by Git before saving.
Git uses them to remind you of the current branch and the files making up
the commit.

A commit message should consist of at least one line giving a brief summary of the changes.
Then if more information is desired, enter a blank line and then write as much as you care to.
Since this is the first commit, nothing has changed yet, so the standard practice is to use "Initial commit".
Exit nano with CTRL-X and save the message.
We've made a commit.

Run `git status`. Has anything changed?

We can see the commit history with `git log`.

    $ git log
    commit c9e8d3ec39248fbb60c94c7555c61e2812f144 (HEAD -> main)
    Author: Don Brower <dbrower@nd.edu>
    Date:   Fri Jan 27 14:18:27 2023 +0000

        Initial Commit

Every commit has a name consisting of a bunch of random-ish numbers and letters, a date, an author, and 0 or more parent commits.
(The name is a SHA1 hash of the contents of the commit, including the current date, committer, etc, so it will necessarily be different from what is shown here).
Most commits will have one parent.
A few may have more than one parent (these are "merge commits").
Since this was the first commit there are no parent commits this time.

Lets make a change to the README file.
Change 'A' to 'The' and add a second line.

    $ nano README.md
    $ git diff
    diff --git a/README.md b/README.md
    index 6bbab16..d7ff0d7 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,4 +1,4 @@
     First Repository
     ================
     
    -A repository to test git commands.
    +The repository to test git commands.

The diff command shows how the files have been changed.
Lines that were added are prefixed with a plus sign `+`,
lines that were removed are prefixed with a minus sign `-`.
Other lines are there to help provide context for the changes.
Now lets make a new commit with these changes.

    $ git add README.md
    $ git commit

This makes a second commit.
Notice that we needed to "add" the README file, even though it was already tracked.
This is because a commit does not automatically contain all the changes in the working copy.
The add means "add the changes in this file to the next commit."
The need to add files to then commit changes is called "staging" the files.
The idea is that you might change many files, but only want to save some of the changes.
For example, you might have needed to change a configuration file or some other
setting so the code works on your computer, but you don't want those changes to
be shared with others.

You can see when each line in a file was changed by using `git blame`

    git blame README.md


### Working with GitHub

Most projects are shared using a Git hosting service.
These services keep a copy of the repository, and may provide a web-based UI and workflow tasks.
One of the biggest is GitHub, and now we will look at how it is used.
There are many open source and open science libraries and applications on GitHub.

First you need to create an account on it if you don't have one already.
Accounts are free. Sign up at [github.com](https://github.com).

We will make a public/private key pair to facilitate pushing commits to GitHub.
This key pair will be unique to you on your VM image.
On the command line run the following, substituting in a good email address for you.

    ssh-keygen -t ed25519 -C "your_email@example.com cicf"

Choose to save the key in the default location (which is `~/.ssh`).
Do not enter a passphrase; when asked just press enter.

There are two files for the pair: one for the private key and one for the public key.
Never share the private file.
In fact, good practice is to never remove the private file from this VM image.

    $ cd ~/.ssh
    $ ls 
    id_ed25519  id_ed25519.pub
    $ cat id_ed25519.pub

The `id_ed25519.pub` file is the public key.
You share the public key with others and then they can use it to verify who you are since this VM is the only place with the corresponding private key.

Lets add the public key to your GitHub account.
Open Firefox in the VM and sign in to GitHub.
Once in, go to the menu in the upper right (your profile picture) and choose "Settings".
Then choose "SSH and GPG keys" from the left-hand side.
Name the key "CICF VM"; keep the key type option as "Authentication Key";
and then paste in the public key we put on the terminal.


### Push to a GitHub Repository

Lets practice pushing a commit to a repository.
First, check out the repository I have prepared, [cicf-2025](https://github.com/dbrower/cicf-2025).

    $ cd
    $ git clone git@github.com:dbrower/cicf-2025.git

This will make a copy of the repository to your VM.
Notice that the local copy of the repository on the VM has a "remote" pointing to the repository we cloned it from.
This is to make it easier to move changes back to the source repository.

    $ cd cicf-2025
    $ git remote –v

Since you don't have write access to the original repository, we will rename it to "upstream" to remind us of this.
(Usually "origin" will point to the place our changes will be shared with, but that requires write access.)

    $ git remote rename origin upstream

Add a copy of your **public** key to this repository.
Name the file with your first initial + last name:

    $ cp ~/.ssh/id_ed25519.pub dbrower.pub
    # change "dbrower" to your name

We will add this file as a commit on a branch:

    $ git checkout -b add-key
    $ git add dbrower.pub
    $ git commit

Now we will share the commit back to the hosting service.

    $ git push upstream add-key

If we had write access this would copy our branch and commit.
But you don't have write access, so the solution is for you to make your own
copy on the hosting service and then put your changes there.
This is called "forking a repository" in the GitHub parlance.
Use the browser to visit [the repo](https://github.com/dbrower/cicf-2025)
on the GitHub service and choose "fork" to make your own copy of it.

Copy the forked repository URL and add it to the checked out repository.

    git remote add origin _your forked repo_

Push your changes to your copy:

    git push origin add-key

View the changes in the browser.
Choose "compare and pull request".
On the next page make sure the base branch is the main branch in the dbrower copy of the repository.
And then select "Create pull request".

On your VM change your branch back to `main`

    $ git checkout main
    $ git pull upstream

## Homework

Everyone should make a pull request to the [cicf-2025] repository with
the public key you generated on your VM.
The process is outlined above in the [Working with GitHub](#working-with-github) section.
In summary you should:

1. Make a GitHub account if you haven't already
2. Fork the [cicf-2025] repository to make your own copy
3. Clone your copy to your VM
4. Copy your **public key** (the file ending with a `.pub`) to the cloned repository and make a commit adding it
5. Push your commit back to your copy of the repository
6. Make a Pull Request to merge your commit into the main repository [cicf-2025]

[cicf-2025]: https://github.com/dbrower/cicf-2025

## Major Facility Repositories

Many Major Facilities have public repositories with code that helps working with their data.
This list is not comprehensive. (And if one is missing, please submit a pull request.)

* [GWOSC (LIGO)](https://git.ligo.org/gwosc)
* [NEON](https://github.com/NEONScience)
* [IceCube](https://github.com/icecube). [Guide to IceCube Repositories](https://github.com/icecube/icecube.github.io/wiki)
* [OOI](https://github.com/oceanobservatories)
* [EarthScope](https://github.com/EarthScope)

## Resources

It is hard to overstate the importance and usefulness of Git in modern software
development. Being comfortable with using Git is absolutely essential for technical workers.

- Software Carpentry's [Version Control with Git](https://swcarpentry.github.io/git-novice/)
- Roger Dudler's [git - the simple guide](https://rogerdudler.github.io/git-guide/)
- [Comprehensive Reference to Git](https://git-scm.com/book/en/v2)
- [Beej's Guide to Git](https://beej.us/guide/bggit/)
- There are many Git hosting sites, these are the big three: [GitHub](https://github.com), [GitLab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/). There are also many smaller ones, such as [SourceHut](https://sourcehut.org/) and [Gitea](https://about.gitea.com/). You can also self-host one, with [Gitea self-hosted](https://github.com/go-gitea/gitea) or [Gitolite](https://gitolite.com/gitolite/index.html).
- [GitHub Skills](https://skills.github.com/) are interactive courses on using GitHub effectively including making [static websites (GitHub Pages)](https://github.com/skills/github-pages).
- Git is by far the most used version control system, but it isn't the only one: [Mercurial](https://www.mercurial-scm.org/), [Fossil](https://www2.fossil-scm.org/home/doc/trunk/www/index.wiki), [Subversion](https://subversion.apache.org/), [CVS]
CVS (ancient, old, please never use)
- [The Biggest and Weirdest Commits in Linux Kernel Git History](https://www.destroyallsoftware.com/blog/2017/the-biggest-and-weirdest-commits-in-linux-kernel-git-history) (2017)

Developers love to design algorithms—including ways that people should organize software development with Git.
- [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- There are too many to name. Organizational needs are important, since open source software is developed differently than closed source, and mobile apps are different than web applications. (e.g. Web applications can deploy a new version continuously unlike mobile apps). Scientific software is likewise different since it is usually for a specific purpose.
- [Example](https://github.com/elastic/elasticsearch-formal-models/pull/29) of a GitHub Pull Request and comments

There are lots of coding standards.
- The Python [PEP 8](https://peps.python.org/pep-0008/) standard for the Python standard library.
- Google [Style Guides](https://google.github.io/styleguide/) for many different languages.
- [JPL Institutional Coding Standard for the C Programming Language](https://andrewbanks.com/wp-content/uploads/2019/07/JPL_Coding_Standard_C.pdf)
- [The Power of 10 Rules](https://en.wikipedia.org/wiki/The_Power_of_10:_Rules_for_Developing_Safety-Critical_Code)
- [NASA F' Flight Software Framework](https://nasa.github.io/fprime/UsersGuide/dev/code-style.html)

Issue tracking is basically a big list but with ability to sort based on metadata.

- [GitHub Issue tracker](https://docs.github.com/en/issues/tracking-your-work-with-issues)
- The big professional grade tracker is Jira, but it is expensive.
- [An epic treatise on scheduling, bug tracking, and triage](https://apenwarr.ca/log/?m=201712)

Testing is a huge area to learn about.

- [PyTest](https://docs.pytest.org/en/stable/contents.html) package
- [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development). Developers love to create methodologies.
- [Checking in on the state of TDD](https://redmonk.com/kholterhoff/2023/07/12/checking-in-on-the-state-of-tdd/) (2023-07-12)
- [Types of tests](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing)
- [Model Checking](https://en.wikipedia.org/wiki/Model_checking) can verify correctness of programs to a specification. In this way it is the other side of the coin from testing. They are based on [temporal logics](https://en.wikipedia.org/wiki/Computation_tree_logic). One example of a model checker is [TLA+](https://lamport.azurewebsites.net/tla/tla.html).


