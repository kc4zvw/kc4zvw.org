#!/bin/ksh
#
# $Id: do-weekly-backup.sh,v 0.2 2017/05/23 18:50:03 kc4zvw Exp kc4zvw $

BACKUP_FILE="$HOME/$USER-hostname.tar.gz"
DOCROOT="/usr/local/www/apache24/data"
#DOCROOT="$HOME/public_html"
EXCLUDE="image09/*"
TARCMD=$(which gtar)
LOGNAME=`logname`

OPTIONS=" --one-file-system --format=gnu "

echo
echo "Running $0"
echo
echo "The path $HOME is the home directory."
echo

rm -f "$BACKUP_FILE"

echo "Launching $TARCMD to create $BACKUP_FILE"
echo "  using $OPTIONS ... "
echo

${TARCMD} ${OPTIONS} --exclude="$EXCLUDE" -czv --file="$BACKUP_FILE" "$DOCROOT"

echo "Finished."

# End of File
