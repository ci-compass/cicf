# CICF Week 4

The goals for the week 4 tutorial are to:

1. Be able to use Git at the command line
2. Be able to make Git commits, create and merge branches.
3. Make a pull request.

## Tutorial

> **Tip:** You can read this tutorial and type commands side by side.
> In JupyterLab, open this `README.md` file (right-click it and choose
> **Open With > Markdown Preview** for a rendered view). Then click the
> **+** button to open a new Launcher and select **Terminal**. Drag the
> Terminal tab to the right side of the editor area to create a split
> view — instructions on the left, terminal on the right.

Git has become ubiquitous in all of computing, not just scientific computing.
Git is useful in any situation that involves sharing text files between people.
Git tracks changes at the directory level.
This means you make changes not just to a single file, but to _groups_ of files at a time.

Git is already installed and configured in your NDP JupyterHub workspace:

    user@server:~/cicf$ git config list | grep user
    user.name=Don Brower
    user.email=dbrower@nd.edu

You should see your name and email.
These are what Git uses to identify you when you make changes to the repository.

> [!NOTE]
> If you are using Git and these are not configured, you can do it from
> the command line:
>
>     git config --global user.name "Don Brower"
>     git config --global user.email "dbrower@nd.edu"
>
> And while you are at it, set the default editor as well. If you don't
> have an editor yet, use `nano`.
> 
>     git config --global core.editor nano


We have been using Git this whole time.
A basic Git command is "status" which gives information on the changes
in the current directory.

    $ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            .vscode/
            week01/
            week03-more-python/iris.csv
            zzz

    nothing added to commit but untracked files present (use "git add" to track)

This tells us what branch we are on, whether our current version matches
the version in our remote repository named `origin/main`.
It lists any files with changes and also the _untracked_ files, that is
files that exist in the directory but which have not been added to the repository.
The exact files you see in these lists depends on the exact changes in your workspace.

You can also see the history of the changes in the repository.

    $ git log --graph

This displays the commits in the `ci-compass/cicf` repository starting from the
current version and going backward in time to the first commit.

## Using a test repository

The best way to experiment with Git is to make a new repository to work on.
For this section we will make another Git repository in your workspace.

    $ mkdir ~/test
    $ cd ~/test
    $ git init
    Initialized empty Git repository in /home/user/test/.git/

The `git init` command makes a new repository in the current directory.
This new repository is completely empty—no files have been added to it yet.
It is good for every project to have a README file that contains the project name and a description for it.

Using a text editor, create a file called `README.md` with the following content:

```
Test Repository
===============

A repository to test git commands.
```

Now if we look at the status.

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

    $ git add README.md

The `git add` command instructs Git to include the changes we've made to this
file in the next commit, but doesn't actually save it to the repository.
The `git commit` will actually save the changes into the repository.

    $ git commit

A text editor will appear when you run this.
The editor is for you to type a message to describe this change.
Not all of the text will be saved, though.
The lines starting with a hash `#` will be removed by Git before saving.
Git uses them to remind you of the current branch and the files that are part of this commit.

A commit message should consist of at least one line giving a brief summary of the changes.
Then, if more information is desired, enter a blank line and then write as much as you care to.
Since this is the first commit, nothing has changed yet, so the standard practice is to use "Initial commit".
Save and close the editor.
We've made a commit.

Run `git status`.

    $ git status
    On branch main
    nothing to commit, working tree clean

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
Since this was the first commit there are no parents.

Let's make a change to the README file.
Change 'A' to 'The' and add a second line. Open the file in a text editor, make the change, and save it.

    $ git diff
    diff --git a/README.md b/README.md
    index 6bbab16..d7ff0d7 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,4 +1,4 @@
     Test Repository
     ===============
     
    -A repository to test git commands.
    +The repository to test git commands.

The diff command shows how the files have been changed.
Lines that were added are prefixed with a plus sign `+`,
lines that were removed are prefixed with a minus sign `-`.
Other lines are there to help provide context for the changes.
Now let's make a new commit with these changes.

    $ git add README.md
    $ git commit

This makes a second commit.
Notice that we needed to "add" the README file, even though it was already tracked.
This is because a commit does not automatically contain all the changes in the working copy.
The add means "add the changes in this file to the next commit."
The need to add files before committing changes is called _staging_ the files.
The idea is that you might change many files, but only want to save some of the changes.
For example, you might have needed to change a configuration file or some other
setting so the code works on your computer, but you don't want those changes to
be shared with others.

You can see when each line in a file was changed by using `git blame`

    $ git blame README.md

If you started making a change and changed your mind, you can revert a file back to its version in the previous commit:

    $ echo "whoops" > README.md
    # we want to recover the previous version of README:
    $ git checkout README.md

### Branches

The repository has a complete history of changes.
The "checkout" command lets us view the repository at a previous point in time.
You can checkout an exact change, or you can check out a _branch_.
A branch lets us make changes in a way that won't disrupt other people.
And then, if we feel like it we can merge branches together to share the changes.

The easiest way to make a branch is to just tell Git we want to start a branch from our current location:

    # in ~/test
    $ git checkout -b new-branch
    Switched to a new branch 'new-branch'

We will usually name the branch in clearer way.
The status message will now show that we are on the new branch:

    # in ~/test
    $ git status
    On branch new-branch
    nothing to commit, working tree clean

Lets add some numbers to the README (the two carets will _append_ the output to the specified file)

    # in ~/test
    $ seq 10 >> README.md
    $ git add README.md
    $ git commit
    [new-branch a5714fb] more changes
     1 file changed, 10 insertions(+)

Now we can see the changes between our branch and the main branch

    # in ~/test
    $ git diff main

This is showing us that the branch has lines added.
One nice thing about branches is that you can switch between them if you have a few projects going on.

    # in ~/test
    $ git checkout main

This will change all the files to be as they are on the "main" branch.
You can then make commits or switch to other branches.

    # in ~/test
    $ git checkout new-branch

You will eventually want to combine the changes in the branch with other branches or the main branch.
Usually this is through a review step so others are award of what you did and can approve it.
But for small repositories you will merge branches yourself.
You can do this via a Pull Request on GitHub, or you can do it on the command line.
We'll first do it on the command line.

    # in ~/test
    $ git checkout main
    $ git merge new-branch

Mostly, this should just work. You will be asked to edit a commit message for the _merge commit_, which is the junction combining the two branches.
If there were changes to a file on both branches that overlapped you will have a _merge conflict_, and at this point you Git will tell you and ask you to edit the conflict.
Git will have edited the files to include both sets of changes inside tags that start with `<<<<`, `=====`, and `>>>>>`.
Edit the files to be as you want them to be, `git add` them and then `git merge --continue`.

Alternately, to use a pull request, upload the branch to the shared repository and then use the repository service to make the request.

### first rule of Git

Git can overwrite changes that you have not committed yet.
It will try not to, but sometimes it will.
The best places for changes is actually _committed in the repository_ since then there are ways to find and get them again, no matter
what state your local files have ended up in.
Now, figuring our the commands to get the changes back may be non-trivial, but it is possible.

### Detached HEAD

You might get an warning message about "detached HEAD state".
The current state that is checked out is call the HEAD commit.
When you check out a branch Git knows that if you make a commit it will be on the current branch, and it will update the branch to
point to this new commit.
If you are in detached HEAD state, Git doesn't know what branch you are on and it is complaining.
Nothing is wrong, it is just a side effect of how Git tracks branches.


## Working with GitHub

Most projects are shared using a Git hosting service.
These services keep a copy of the repository, and may provide a web-based UI and workflow tasks.
The most important service these Git hosting services provide is a copy of you Git repositories in the cloud.
This lets you have a copy not on your computer, and if you are on a team, it can be a central point where everyone on the team can share changes and updates.
The cloud service is also nice since it provides a web page that you can use to share code with others.

The Git repository on your computer is called your _local repository_.
Copies of the repository not on your computer are _remote repositories_.
There can be more than one remote repository, but usually there is just one.
In your local repository you can give nicknames the remotes.
The default nickname for the first remote repository is "origin".
This is usually the place where you will get all the new changes from and push your changes to.

We need to make an access token so we can push to our repositories from the JupyterHub workspace.
Follow [this link](https://github.com/settings/personal-access-tokens/new?name=CICF+token&description=Write%20code%20and%20push%20it%20to%20main%21&contents=write&pull_requests=write&workflows=write&expires_in=90) to open a browser window that lets you create the access token.
An access token is just a sequence of characters.
Once you make the token, copy it and paste it into the following command line in your Terminal:

    export GH_TOKEN="paste token here inside the quotes"

> [!NOTE]
> If you start a new JupyterHub server you will need to set the token again.
> You can manage your tokens on your GitHub profile in Settings > Developer Settings > Personal Access Tokens > [Fine-grained Tokens](https://github.com/settings/personal-access-tokens).
> There is also [more info on creating a fine-grained personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token).

OK, now lets make a copy of the test repository on GitHub.
On the Github website, create a new repository.
Name it "cicf-test".
It will be empty.

At the command line add it to the "test" repository:

    # in ~/test
    $ git remote add origin "https://$GITHUB_USER:$GH_TOKEN@github.com/$GITHUB_USER/cicf-test"

Now push your changes to GitHub:

    # in ~/test
    git push origin main

You can see the remotes configured for this repository with:

    $ git remote –v


### Push to a GitHub Repository

The most basic operation is getting changes from the remote repository.
We have already done "pulls": this does a two step operation of first getting changes from the remote
and then updating your current branch to contain all the new changes on it.
There is also a "fetch" that just gets the changes from the remote but doesn't do the update step.

    # in ~/test
    $ git fetch
    $ git pull

The other basic step is moving your updates to the remote repository.
This is called a "push".
Git doesn't match branch names up automatically, so we need to tell Git that our "main" branch is the same as the remote's "main" branch.
That is why we type "origin main" on the command line.

    # in ~/test
    $ git push origin main

Now you will see these changes on GitHub.


### Making changes to other GitHub repositories

Sometimes you want to suggest a change to a repository you do not have write access to.
You can handle that by making a copy (_fork_) of the repository to your shared hosting provider, pushing your changes there and then making a pull request back into the original repository.

Lets try this by making a fork of the CICF repository.
Do this on the GitHub webpage for [ci-compass/cicf](https://github.com/ci-compass/cicf).
There is a drop down menu on the top that says "Fork".
When GitHub is done making your forked copy of the repository,
find the new repository location by choosing the green `<> Code` button and then
choosing the SSH tab.
You should see a path similar to `git@github.com:dbrower/cicf`.
Copy the path by clicking the clipboard icon next to it.
At the command line add it to the checked out repository:

    # in ~/cicf
    git remote add personal <our-forked-repo-path> # <-- paste in the path here

Now lets make a branch.

    # in ~/cicf
    git checkout -b my-patch

You can now make the changes you want and then when the branch looks good:

    git push personal my-patch

Notice that this time we pushed the new branch to our forked copy of the repository.
For GitHub, you can now view the new branch in the browser on your forked copy.
Choose "compare and pull request".
This is how you submit a pull request.
Exercise 1 will ask you to make a pull request on another repository.
If the person reviewing the pull request has changes, you can make them in local checkout.
Then add them with a commit to the same branch and then 

    git push my-patch

will update your personal branch with the new changes.



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
- Git is by far the most used version control system, but it isn't the only one: [Mercurial](https://www.mercurial-scm.org/), [Fossil](https://www2.fossil-scm.org/home/doc/trunk/www/index.wiki), [Subversion](https://subversion.apache.oHTTPS), [CVS]
CVS (ancient, old, please never use)
- [The Biggest and Weirdest Commits in Linux Kernel Git History](https://www.destroyallsoftware.com/blog/2017/the-biggest-and-weirdest-commits-in-linux-kernel-git-history) (2017)

Developers love to design algorithms—including ways that people should organize software development with Git.
- [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- There are too many to name. Organizational needs are important, since open source software is developed differently than closed source, and mobile apps are different than web applications. (e.g. Web applications can deploy a new version continuously unlike mobile apps). Scientific software is likewise different since it is usually for a specific purpose.
- [Example](https://github.com/elastic/elasticsearch-formal-models/pull/29) of a GitHub Pull Request and comments

There are lots of coding standards.
- The Python [PEP 8](httpHTTPS/peps.python.org/pep-0008/) standard for the Python standard library.
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

- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) an MIT course that covers the same ideas as Software Carpentry: many useful computing skills are not taught in university CS classes.
