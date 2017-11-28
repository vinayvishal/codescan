#!/bin/bash
#################
## functions ####

TOTAL_COUNT=0

html_header(){

cat > ./glassfish-stats.html <<EOF

echo "<html>"
echo "<title>glassfish-stats</title>"
EOF

}

html_body(){
cat >> ./glassfish-stats.html <<EOF
echo "<body>"
echo "<table border=\"1\">"
echo "<tr>"
echo "<th>Module</th>"
echo "<th>Path</th>"
echo "<th>File Count</th>"
echo "<th>Details</th>"
echo "</tr>"
EOF
}

#echo $(print_module_stats $1)
#echo "</table>"
#echo "</body>"

html_footer(){

cat >> ./glassfish-stats.html <<EOF
echo "</table>"
echo "</body>"
echo "</html>"
EOF
}

module_details(){
EXTENSIONS=()
FILE_TYPES=""
FILE_EXTENSION=""


cat >> ./glassfish-stats.html <<EOF
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
  FILE_EXTENSION=`echo ${file##*\.}`
  if [ ! -z ${FILE_EXTENSION} ];then
    EXTENSIONS[$INDEX]=$FILE_EXTENSION    
    INDEX=`expr $INDEX + 1`
  fi
 fi
done

IFS=$'\n' EXTENSION_SET=($(sort -u <<<"${EXTENSIONS[*]}"))
unset IFS
for ext in “${EXTENSION_SET[@]}”
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
EOF
}

generate_report(){

#cat >> ./glassfish-stats.html <<EOF

$(html_header)
$(html_body)
$(print_module_stats $1)
$(html_footer)

#EOF
}

print_module_stats(){


## iterate over the repo and find out all pom.xmls

for pom in `find $1 -name "pom.xml"`
do

  COUNT=0
  #echo $pom
  PARENT_DIR="${pom%/*}"
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  
#  cat >> ./glassfish-stats.html <<EOF
#  echo "<tr>"
#  echo "<td>${PARENT_DIR##*/}</td>" 
#  echo "<td>$PARENT_DIR</td>" 
#  echo "<td>$COUNT</td>" 
#  
#  EOF
  
cat >> ./glassfish-stats.html <<EOF
   echo "<td>${PARENT_DIR##*/}</td>" 
   echo "<td>$PARENT_DIR</td>" 
   echo "<td>$COUNT</td>" 
   echo "<td>
EOF
$(module_details $PARENT_DIR)

cat >> ./glassfish-stats.html <<EOF
echo "</td>"
echo "</tr>"
EOF

done
cat >> ./glassfish-stats.html <<EOF
echo "<tr><td>"-"</td><td>"-"</td><td>$TOTAL_COUNT</td><td>"-"</td></tr>"
EOF
}

dump_module_data(){
  COUNT=0
  #echo $pom
  PARENT_DIR="${1%/*}"
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  
cat >> ./glassfish-stats.html <<EOF
  echo "<tr>"
  echo "<td>${PARENT_DIR##*/}</td>" 
  echo "<td>$PARENT_DIR</td>" 
  echo "<td>$COUNT</td>" 
EOF

}

#################
## main #########

GLASSFISH_DIR=$1

generate_report $1
