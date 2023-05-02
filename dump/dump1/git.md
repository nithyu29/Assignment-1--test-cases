"
Here's a step-by-step guide to configuring Git for signing commits, adding your GPG key to your GitHub profile, and setting up SSH key access to your GitHub account:

Install Git:

Download and install Git from https://git-scm.com/downloads.
Install GPG:

Download and install GPG from https://gnupg.org/download/.
Generate a GPG key:

Open the command prompt or terminal and run gpg --full-generate-key.
Follow the prompts to create a new key. Use the email address associated with your GitHub account.
List your GPG keys:

Run gpg --list-secret-keys --keyid-format LONG.
Find the key ID for the key you just created (it's the part after the / in the sec line).
Export your GPG public key:

Run gpg --armor --export <your_key_id>, replacing <your_key_id> with the key ID you found in step 4.
Copy the output, including the lines -----BEGIN PGP PUBLIC KEY BLOCK----- and -----END PGP PUBLIC KEY BLOCK-----.
Add your GPG public key to your GitHub profile:

Go to https://github.com/settings/keys.
Click "New GPG key".
Paste your GPG public key and click "Add GPG key".
Configure Git to use your GPG key:

Run git config --global user.signingkey <your_key_id>, replacing <your_key_id> with the key ID from step 4.
Run git config --global commit.gpgsign true to enable commit signing by default.
Generate an SSH key:

Run ssh-keygen -t ed25519 -C "your_email@example.com", replacing your_email@example.com with your GitHub email address.
Follow the prompts to create a new SSH key. Use the default file location and optionally set a passphrase.
Add your SSH public key to your GitHub account:

Run cat ~/.ssh/id_ed25519.pub (or type %USERPROFILE%\.ssh\id_ed25519.pub on Windows) to display your SSH public key.
Copy the output.
Go to https://github.com/settings/keys.
Click "New SSH key".
Paste your SSH public key, give it a title, and click "Add SSH key".
Clone the repository:

Accept the invitation on GitHub Classroom.
Click the green "Code" button on the repository page.
Copy the SSH URL (it should look like git@github.com:NYUAppSec/...).
Run git clone <your_repository_url>, replacing <your_repository_url> with the copied SSH URL.
Now you have Git configured for signing commits, your GPG key added to your GitHub profile, and SSH key access set up for your GitHub account.





User

2 / 2

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git clone git@github.com:nithyu29/Assignment-1--test-cases.git
Cloning into 'Assignment-1--test-cases'...
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
ChatGPT
It seems like you're encountering a permission denied error when trying to clone the repository using SSH. This error usually occurs when your SSH key is not properly set up or recognized by GitHub. To resolve this issue, follow these steps:

Confirm that your SSH key is correctly added to your GitHub account:

Go to https://github.com/settings/keys.
Verify that the SSH key you generated earlier is listed there.
Ensure that the SSH agent is running and has your SSH key added:

For Windows (Git Bash or MINGW64):

Run eval $(ssh-agent -s) to start the SSH agent.
Run ssh-add ~/.ssh/id_ed25519 to add your SSH key to the agent.
If prompted for a passphrase, enter the passphrase you set when generating the SSH key.
For Linux or macOS:

Run eval "$(ssh-agent -s)" to start the SSH agent.
Run ssh-add ~/.ssh/id_ed25519 to add your SSH key to the agent.
If prompted for a passphrase, enter the passphrase you set when generating the SSH key.
Test your SSH connection to GitHub:

Run ssh -T git@github.com.
You should see a message like: "Hi <username>! You've successfully authenticated, but GitHub does not provide shell access."
Retry cloning the repository:

Run git clone git@github.com:nithyu29/Assignment-1--test-cases.git.
If you still encounter the permission denied error after following these steps, double-check that you have copied the correct SSH key to your GitHub account and that you are using the correct SSH URL when cloning the repository.
"

cd
_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ gpg --full-generate-key
gpg (GnuPG) 2.2.29-unknown; Copyright (C) 2021 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal      
   (3) DSA (sign only)      
   (4) RSA (sign only)
  (14) Existing key from card
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072)
Requested keysize is 3072 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 0
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: nithu29
Email address: nithyuraj2929@gmail.com
Comment: nithu
You selected this USER-ID:
    "nithu29 (nithu) <nithyuraj2929@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key 5097E2ACB4423BD0 marked as ultimately trusted
gpg: directory '/c/Users/_SaiNt/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/c/Users/_SaiNt/.gnupg/openpgp-revocs.d/04060FF643CACB6FDAE381405097E2ACB4423BD0.rev'
public and secret key created and signed.

pub   rsa3072 2023-05-01 [SC]
      04060FF643CACB6FDAE381405097E2ACB4423BD0
uid                      nithu29 (nithu) <nithyuraj2929@gmail.com>
sub   rsa3072 2023-05-01 [E]


_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ gpg --list-secret-keys --keyid-format LONG
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
/c/Users/_SaiNt/.gnupg/pubring.kbx
----------------------------------
sec   rsa3072/5097E2ACB4423BD0 2023-05-01 [SC]
      04060FF643CACB6FDAE381405097E2ACB4423BD0
uid                 [ultimate] nithu29 (nithu) <nithyuraj2929@gmail.com>
ssb   rsa3072/0BE86B6FF109CD65 2023-05-01 [E]


_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ gpg --armor --export 04060FF643CACB6FDAE381405097E2ACB4423BD01
gpg: WARNING: nothing exported

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ gpg --armor --export <04060FF643CACB6FDAE381405097E2ACB4423BD01>
bash: syntax error near unexpected token `newline'

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ gpg --armor --export 04060FF643CACB6FDAE381405097E2ACB4423BD01
gpg: WARNING: nothing exported

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ gpg --armor --export 04060FF643CACB6FDAE381405097E2ACB4423BD0
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
1RjrJ/NyBEugDuYChdCWQSIHJWpV
=SusB
-----END PGP PUBLIC KEY BLOCK-----

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git config --global user.signingkey 04060FF643CACB6FDAE381405097E2ACB4423BD0

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git config --global commit.gpgsign true~

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git config --global commit.gpgsign true

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ ssh-keygen -t ed25519 -C nithyuraj2929@gmail.com
Generating public/private ed25519 key pair.
Enter file in which to save the key (/c/Users/_SaiNt/.ssh/id_ed25519): /e/WORKSPACE/Assignment-1--test-cases/ssh.txt
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /e/WORKSPACE/Assignment-1--test-cases/ssh.txt
Your public key has been saved in /e/WORKSPACE/Assignment-1--test-cases/ssh.txt.pub
The key fingerprint is:
SHA256:Iv5Un+J4q2WBlHf2eV5YEfSLkxEgsHEpJsk7MPDRElg nithyuraj2929@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
| .+E+ .o.o.....+.|
| ..+.= ++..   . o|
|   .+ *.o o  .  o|
|     + o o . .+o.|
|    . + S   o+o..|
|   . . o o . o.. |
|    . . + o   .  |
|     o =..       |
|      +oo.       |
+----[SHA256]-----+

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ type %USERPROFILE%\.ssh\id_ed25519.pub
bash: type: %USERPROFILE%.sshid_ed25519.pub: not found

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ type %USERPROFILE%\/e/WORKSPACE/Assignment-1--test-cases/ssh.txt.pub
bash: type: %USERPROFILE%/e/WORKSPACE/Assignment-1--test-cases/ssh.txt.pub: not found

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ type %USERPROFILE%/e/WORKSPACE/Assignment-1--test-cases/ssh.txt.pub
bash: type: %USERPROFILE%/e/WORKSPACE/Assignment-1--test-cases/ssh.txt.pub: not found

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ mkdir ass && cd ass

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git clone git@github.com:nithyu29/Assignment-1--test-cases.git
Cloning into 'Assignment-1--test-cases'...
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ eval $(ssh-agent -s)
Agent pid 711

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ ssh-add ~/.ssh/id_ed25519
/c/Users/_SaiNt/.ssh/id_ed25519: No such file or directory

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ ssh-add /e/WORKSPACE/Assignment-1--test-cases/ssh.txt.pub
Error loading key "/e/WORKSPACE/Assignment-1--test-cases/ssh.txt.pub": invalid format

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ ssh-add /e/WORKSPACE/Assignment-1--test-cases/ssh.txt
Enter passphrase for /e/WORKSPACE/Assignment-1--test-cases/ssh.txt: 
Identity added: /e/WORKSPACE/Assignment-1--test-cases/ssh.txt (nithyuraj2929@gmail.com)

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ ssh -T git@github.com
Hi nithyu29! You've successfully authenticated, but GitHub does not provide shell access.

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git clone git@github.com:nithyu29/Assignment-1--test-cases.git
Cloning into 'Assignment-1--test-cases'...
remote: Enumerating objects: 81, done.
remote: Counting objects: 100% (81/81), done.
remote: Compressing objects: 100% (54/54), done.
remote: Total 81 (delta 21), reused 81 (delta 21), pack-reused 0
Receiving objects: 100% (81/81), 105.55 KiB | 79.00 KiB/s, done.
Resolving deltas: 100% (21/21), done.

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git add .
warning: adding embedded git repository: ass/Assignment-1--test-cases
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint: 
hint:   git submodule add <url> ass/Assignment-1--test-cases
hint: 
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint: 
hint:   git rm --cached ass/Assignment-1--test-cases
hint: 
hint: See "git help submodule" for more information.

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git add .

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git commit -S -m "second commit"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got '_SaiNt@archie-SaiNt.(none)')

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git config user.email "nithyuraj2929@gmail.com"

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git config user.name "nithu29"

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git commit -S -m "second commit"
[main 3604bf9] second commit
 1 file changed, 1 insertion(+)
 create mode 160000 ass/Assignment-1--test-cases

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git push
remote: Permission to nithyu29/Assignment-1--test-cases.git denied to PeterMwendia.
fatal: unable to access 'https://github.com/nithyu29/Assignment-1--test-cases.git/': The requested URL returned error: 403

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git remote set-url origin git@github.com:nithyu29/Assignment-1--test-cases.git

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 838 bytes | 209.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:nithyu29/Assignment-1--test-cases.git
   4761986..3604bf9  main -> main

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases/ass (main)
$ cd /e/WORKSPACE/Assignment-1--test-cases

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git add .
warning: in the working copy of '.vscode/c_cpp_properties.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'ssh.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'ssh.txt.pub', LF will be replaced by CRLF the next time Git touches it

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git commit -S -m "second commit"
[main b297f07] second commit
 9 files changed, 426 insertions(+), 28 deletions(-)
 create mode 100644 .github/workflows/hello.yml
 create mode 100644 .vscode/c_cpp_properties.json
 delete mode 100644 .vscode/tasks.json
 create mode 100644 giftcardreader.exe
 create mode 100644 git.md
 create mode 100644 issues
 create mode 100644 ssh.txt
 create mode 100644 ssh.txt.pub

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git push
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 4 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (13/13), 86.74 KiB | 227.00 KiB/s, done.
Total 13 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:nithyu29/Assignment-1--test-cases.git
   3604bf9..b297f07  main -> main

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$
 *  History restored 


_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git add .

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git push
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ eval $(ssh-agent -s)
Agent pid 861

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ ssh-add /e/WORKSPACE/ssh.txt
/e/WORKSPACE/ssh.txt: No such file or directory

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ ssh-add /e/WORKSPACE/ssh.txt.pub
/e/WORKSPACE/ssh.txt.pub: No such file or directory

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ ssh-add /e/WORKSPACE/ass-2/ssh.txt
Enter passphrase for /e/WORKSPACE/ass-2/ssh.txt: 
Identity added: /e/WORKSPACE/ass-2/ssh.txt (nithyuraj2929@gmail.com)

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ ssh -T git@github.com
Hi nithyu29! You've successfully authenticated, but GitHub does not provide shell access.

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git add .

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git push
Everything up-to-date

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git commit -S -m "second commit"
[main 04e1370] second commit
 3 files changed, 10 deletions(-)
 delete mode 160000 ass/Assignment-1--test-cases
 delete mode 100644 ssh.txt
 delete mode 100644 ssh.txt.pub

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)
$ git push
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 759 bytes | 253.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:nithyu29/Assignment-1--test-cases.git
   b297f07..04e1370  main -> main

_SaiNt@archie-SaiNt MINGW64 /e/WORKSPACE/Assignment-1--test-cases (main)