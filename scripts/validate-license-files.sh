#!/bin/bash


check_header(){

diff EPL-header.txt <(head -n 15 $1)

}

#### main ####

REPO_ROOT_DIR=$1

find $1 -name "*.java" ! -path "*samples*" -print0 | while read -d $'\0' file; do echo -e "##### $file ######\n\n"; check_header $file ;echo -e "\n\n#################\n\n"; done;
