#!/bin/bash


#### main ####

REPO_ROOT_DIR=$1

find $1 -iname "*license*" -print0 | while read \
-d $'\0' file; do `cat EPL-2.0.txt > "$file"`; done;
