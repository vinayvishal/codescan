#!/bin/bash
#################
## functions ####

html_header(){

echo "<html>"
echo "<title>glassfish-stats</title>"


}

html_body(){
echo "<body>"
echo "<table border=\"1\">"
echo "<tr>"
echo "<th>Module</th>"
echo "<th>Path</th>"
echo "<th>File Count</th>"
echo "<th>Details</th>"
echo "</tr>"
echo $(print_module_stats $1)
echo "</table>"
echo "</body>"
}

html_footer(){

echo "</html>"
}

module_details(){
EXTENSIONS=()
FILE_TYPES=""
FILE_EXTENSION=""


echo "<table border=\"1\">"
echo "<tr>"
echo "<th>Type</th>"
echo "<th>Count</th>"
echo "</tr>"
INDEX=0
COUNTER=0
for file in `find $1 ! -path "*target*"`
do
 if [ -f $file ];then 
#  echo "$file"
  FILE_EXTENSION=`echo ${file##*\.}`
  if [ ! -z ${FILE_EXTENSION} ];then
#    echo $FILE_EXTENSION
    EXTENSIONS[$INDEX]=$FILE_EXTENSION    
    INDEX=`expr $INDEX + 1`
  fi
 fi
done

#for i in "${EXTENSIONS[@]}"
#do
#  echo "<tr>"
#  echo "<td>$i</td>"
#  echo "<td>-</td>"
#  echo "</tr>"
#done 

IFS=$'\n' EXTENSION_SET=($(sort -u <<<"${EXTENSIONS[*]}"))
unset IFS
for ext in “${EXTENSION_SET[@]}”
#COUNTER=`expr 0`
do
  for exts in "${EXTENSIONS[@]}"
  do
    if [ $exts = $ext ];then
    COUNTER=`expr $COUNTER + 1`
    fi
  done 
  echo "<tr>"
  echo "<td>$ext</td>"
  echo "<td>$COUNTER</td>"
  echo "</tr>"
COUNTER=0
done 
echo "</table>"

}

generate_report(){

cat > ./glassfish-stats.html <<EOF

$(html_header)
$(html_body $1)
i$(html_footer)

EOF
}

print_module_stats(){

TOTAL_COUNT=0

## iterate over the repo and find out all pom.xmls

for pom in `find $1 -name "pom.xml"`
do
  COUNT=0
  #echo $pom
  PARENT_DIR="${pom%/*}"
  echo "<tr>"
  echo "<td>${PARENT_DIR##*/}</td>" 
  echo "<td>$PARENT_DIR</td>" 
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  echo "<td>$COUNT</td>" 
  echo "<td>$(module_details $PARENT_DIR)</td>"
  echo "</tr>"
done
echo "<tr><td>"-"</td><td>"-"</td><td>$TOTAL_COUNT</td><td>"-"</td></tr>"
}

#################
## main #########

GLASSFISH_DIR=$1

generate_report $1
#print_module_stats $1
