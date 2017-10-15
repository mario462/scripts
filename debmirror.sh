#!/bin/bash

/usr/bin/debmirror -p -v --nosource -h repos.uh.cu -e http -r ubuntu -d xenial,xenial-updates,xenial-security,xenial-backports -s main,restricted,multiverse,universe -a i386,amd64 --ignore-missing-release --ignore-release-gpg --diff=none --getcontents --i18n --rsync-extra=none $1

echo "Last update: $(date)" > $1/last-update.txt
