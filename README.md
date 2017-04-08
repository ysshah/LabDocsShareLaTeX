# Physics 111B LaTeX Lab Writeups

## Usage instructions

### First-time setup

1. Make a [GitHub](https://github.com/) account
1. Get added as a collaborator to this repository
1. Make a [ShareLaTeX](https://www.sharelatex.com/) account
1. On ShareLaTeX, click "New Project" then "Import from GitHub"
1. Link GitHub account to ShareLaTeX account
1. Click this repository to import its contents
1. Make changes
1. Click "Menu" on top left, then under "Sync" click "GitHub"
1. Click "Push ShareLaTeX changes to GitHub"
1. Website PDF will be automatically updated

### General process

1. Open the ShareLaTeX project corresponding to this GitHub repository
1. Click "Menu" on top left, then under "Sync" click "GitHub"
1. If there are changes in the repository, click "Pull GitHub changes to ShareLaTeX"
1. Make changes
1. Open the GitHub sync box again, and click "Push ShareLaTeX changes to GitHub"
1. Website PDF will be automatically updated

## Steps to Replicate this Repository

Here's what I did to create this repository.

1. Make a [GitHub](https://github.com/) account and create this repository
1. Login to [Travis CI](https://travis-ci.org/) with GitHub account and enable builds on this repository
1. Install the Travis CI command line tool [here](https://github.com/travis-ci/travis.rb#installation)
1. Follow these [instructions](https://oncletom.io/2016/travis-ssh-deploy/). Essentially:
    1. Create an SSH key, replace `<repo>` with name of repository
        ```bash
        ssh-keygen -t rsa -b 4096 -C '<repo>@travis-ci.org' -f ./deploy_rsa
        ```

    1. Add the public SSH key to your Pantheon user's SSH keys
    1. Use `travis encrypt` to add the key to the .travis.yml file
        ```
        travis encrypt-file deploy_rsa --add
        ```

    1. Delete the key since we don't need it anymore
        ```
        rm -f deploy_rsa deploy_rsa.pub
        ```
1. Commented code to installing LaTeX and build the PDFs are in [`.travis.yml`](.travis.yml) and [`create.py`](create.py)
