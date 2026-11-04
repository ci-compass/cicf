Getting Started
---------------

To provide a consistent environment for everyone, these tutorials use the
[NDP (National Discovery Platform)](https://www.nationaldiscoveryplatform.org/) JupyterHub
to provide a web-based workspace with a terminal and notebook environment.

1. If you don't have one already, sign up for a (free) GitHub account.
2. Launch an NDP workspace using JupyterHub.

## Signing up for GitHub account

If you don't have a GitHub account create one at [GitHub](https://github.com/).
Accounts are free.

**Please send an email to <cicf@ci-compass.org> telling us your GitHub user name.**

## Sign up / Login to NDP

Use the institutional email address you used when applying for CICF to log in. An account will be automatically created for you. A member of our team will then add you to the CICF classroom.

## Launching an NDP Workspace

1. **Launch JupyterHub.**

   Click Launch at the bottom of the module to open NDP JupyterHub.

2. **Start your JupyterLab server.**

   Use the default resource settings and click Start Server. Wait for JupyterLab to open.

3. **Open your persistent storage.**

   In the JupyterLab File Browser, open `_User-Persistent-Storage_`. Save your work in this
   directory so that it remains available after your server is stopped.

   > **Important:** Storage is limited to 10 GB. Only files saved inside
   > `_User-Persistent-Storage_` are preserved between sessions. Files stored
   > elsewhere on the server are non-persistent and will be lost when your
   > server is stopped.

4. **Select the course workspace.**

   Open the NDP Widget and select the workspace for the current week.

5. **Clone the course repository.**

   In the NDP Widget, use Clone Repository to clone the CICF GitHub repository
   into your current folder.

6. **Install the required Python packages.**

   After cloning the repository, click Install requirements.txt in the NDP
   Widget. Wait for the installation to complete before continuing. This will
   install the Python packages needed for the course materials.

   > **Important:** Required packages are installed for your current JupyterHub
   > session and are not preserved when you stop your server. You will need to
   > click Install requirements.txt again each time you launch a new JupyterHub
   > server.

7. **Open a Terminal.**

   In JupyterLab, click the **+** button to open the Launcher, then select
   Terminal. You can drag the Terminal tab to create a split view alongside a
   tutorial file, allowing you to read instructions and run commands without
   switching between tabs.

## Using the NDP Workspace

The NDP workspace runs on a JupyterHub server. When you stop your server,
only files inside `_User-Persistent-Storage_` are kept. Installed packages
and files outside that directory are lost.

To return to your workspace, launch JupyterHub again and navigate to
`_User-Persistent-Storage_` to find your saved work.

When you are finished working, go to **File > Hub Control Panel > Stop My Server**.

## Running Exercises

In each week there will be exercises named `exercise-1`, `exercise-2`, and so on.
The description of each exercise is in the file.
Do the task of the exercise and then you can see how you did by running the command `make`.
This will run tests and output the results to the terminal.
Successful tests appear as green, and unsuccessful tests appear as red.

## Updating your Repository

You can update your local copy with the current `ci-compass/cicf` repository by using Git:

	git pull

If you get a conflict, it is probably because of some file changing.
The Jupyter notebook files (`*.ipynb`) are notorious for this.
There are two ways of taking care of this.
You can replace these files with the version in the repository:

	git checkout _filename_

Or you can "stash" your changes and try to then re-apply them:

	git stash
	git pull
	git stash pop
