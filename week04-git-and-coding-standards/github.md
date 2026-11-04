# GitHub

If you are working outside the NDP JupyterHub workspace, you may need to do a little set-up yourself to connect to GitHub.
The other Git hosting services are similar.

First, you need a way for Git to log in to Github.
One way is with a public/private key pair.
Also, the best practice is to have a unique pair for each computer you use.
On the command line run the following, substituting in a good email address for you.
The "cicf" at the end is just to identify this pair, you should change it to a computer name or memorable phrase.
(Since you can have more than one key pair, you will eventually need to distigunish them).

    ssh-keygen -t ed25519 -C "your_email@example.com cicf"

Choose to save the key in the default location (which is `~/.ssh`).
Do not enter a passphrase; when asked just press enter.

There are two files for the pair: one holds the private key and one the public key (this one ends in `.pub`).
Never share the private file.
In fact, good practice is to never remove the private file from this VM image.

    $ cd ~/.ssh
    $ ls 
    id_ed25519  id_ed25519.pub
    $ cat id_ed25519.pub

The file `id_ed25519.pub` is the public key.
Sharing the public key with others lets them verify who you are since this computer is the only place with the corresponding private key.

To add the public key to your GitHub account open Firefox and sign in to GitHub.
Once in, go to the menu in the upper right (your profile picture) and choose "Settings".
Then choose "SSH and GPG keys" from the left-hand side.
Name the key something so you can remember it, e.g. a computer name or "CICF"; keep the key type option as "Authentication Key";
and then paste in the public key we put on the terminal.

