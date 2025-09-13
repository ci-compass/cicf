Getting Started
---------------

The CICF technical program aims to give you an overview of cyberinfrastructure
concepts, tools, and skills.
This repository provides a way for you to try out commands and tools yourself.
Two of the skills we most want you to develop is a familiarity with using the command line
and comfort with using Git, a ubiquitous tool for contributing to technical projects.

**There is an expectation that you complete the exercises for each week.**

## Preparing for the course

To provide a consistent environment for everyone, we will use GitHub Codespaces.
This provides a free, web-based virtual machine that has a command line.

1. If you don't have one already, sign up for a (free) GitHub account.
2. Fork this repository (ci-compass/cicf). This will make your personal copy of it.
3. Start a codespace for this repository.

### Signing up for GitHub account

If you don't have a GitHub account already, go to [GitHub](https://github.com/) to sign up.
Accounts are free.

When you have an account, please let tell us your user name by sending an email to `cicf@ci-compass.org`.

<!-- maybe we save forking for week 4
### Fork this repository

Sign in to your account on GitHub and then visit this repository's page, [ci-compass/cicf](https://github.com/ci-compass/cicf).
Choose the "Fork" drop down on the upper right of the page, and then make a fork of the repository
into your own space, so the owner will be your account and keep the repository name `cicf`.
After some time you will have your own copy of the CICF repository.
-->

### Start a Codespace for this repository

Once you made your own fork of the repository choose the big plus sign `+` at the top left of the screen and then "create a new Codespace".
Base the codespace this repository (so `ci-compass/cicf`),
on the main branch,
and use the default region and machine type.
This will then open a window that looks like a VS code interface.
(If you are not familiar with VSCode, don't worry!).
The window has a few regions which are marked in the following screenshot.
![Picture of codespace window](./codespace-marked.png)
There is a file pane, which lists the files in the repository,
an editor pane which is where files being edited will appear (right now there is none),
and at the bottom of the window you should see a prompt that is similar to `@dbrower ➜ /workspaces/cicf (main) $`,
this is the terminal window.

You can make the terminal window larger by choosing the "full screen" button on the termal pane.
You can also hide the file pane using the panel controls.

## Structure of this repository

This repository has a directory for each week.
Inside each directory there will be a `README` file describing the exercises for the week.
The exercises are in files starting with the word `exercise-`.
They may be shell scripts, or python scripts.

Each directory also has a test suite that will evaluate the exercises.
Run the test with the command `make` while you are in the current week's directory.
If each test passes, congratulations!
If a test fails you can troubleshoot, and try again.

