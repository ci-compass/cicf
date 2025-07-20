Getting Started
---------------

The CICF technical program aims to give you an overview of cyberinfrastructure
concepts, tools, and skills.
And since the best way to learn is by doing, you are expected to try completing the exercises each week.
Many previous fellows have commented that more familiarity with the command line would be helpful.

One of the most important skills we want to develop is familarity and comfort with
using the command line.

## Preparing for the course

To provide a consistent envrionment for everyone, we will use GitHub Codespaces as the
preferred envrionment.
This provides a web-based virtual machine that has a command line.

1. If you don't have one already, sign up for a (free) GitHub account.
2. Fork this repo (ci-compass/cicf). This will make your personal copy of it.
3. Start a Codespace for this repository.

### Signing up for GitHub account

If you don't have a GitHub account already, go to [GitHub](https://github.com/) to sign up.
Accounts are free.

When you have an account, please let us know your user name by sending an email to cicf@ci-compass.org stating it.

### Fork this repository

Sign in to your account on GitHub and then visit this repository's page, [ci-compass/cicf](https://github.com/ci-compass/cicf).
Choose the "Fork" drop down on the upper right of the page, and then make a fork of the repository
into your own space, so the owner will be your account and keep the repository name `cicf`.
After some time you will have your own copy of the CICF repository.

### Start a Codespace for this repository

Once you made your own fork of the repository choose the big plus sign `+` at the top left of the screen and then create a new Codespace.
Have the codespace be based on your copy of the cicf repository (so `<your username>/cicf`),
on the main branch, and use the default region and machine type.
This will then open a window that looks like a VS code interface.
(If you are not familar with VSCode, don't worry!).
At the bottom of the window you should see a prompt that is similar to `@dbrower ➜ /workspaces/cicf (main) $`.
This is a command line prompt, and if you see this, you're ready for week 1!

## Structure of this repository

This repository has a directory for each week.
Inside each directory there will be a `README` file describing the exercises for the week.
The exercieses are in files starting with the word `exercise-`.
They may be shell scripts, or python scripts.
Either way, they are intended to be executed and that is how they will be evaluated.

Each directory also has a test suite that will evaluate the exercises.
Run the test with the command `make` while you are in the current week's directory.
If each test passes, congratulations!
If a test fails you can troubleshoot, and try again.

