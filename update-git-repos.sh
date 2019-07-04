#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset
# # set -o xtrace

printf "Syncing Samba share to PRIVATE Gitlab repository ...\n"
rsync -r --exclude '.git'  /Volumes/config/ ~/Code/home-assistant-configuration-gitlab
cd ~/Code/home-assistant-configuration-gitlab/
printf "Pushing ...\n"
git add --quiet .
git commit --quiet -m "Update config"
git push --quiet
printf "\nDone backupping to private repo!\n\n\n"

printf "Syncing to public GitHub repository ...\n"
rsync -r --exclude '.git' --exclude '*.db' --exclude '*.log' --exclude 'esphomeyaml/*/' /Volumes/config/ ~/Code/home-assistant-configuration
printf "Done! Changes are not commited yet - go review them!\n"