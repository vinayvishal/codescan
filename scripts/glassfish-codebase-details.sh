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

echo "<table border=\"1\">"
echo "<tr>"
echo "<th>Type</th>"
echo "<th>Count</th>"
echo "</tr>"
echo "</table>"

}

generate_report(){

cat > ./glassfish-stats.html <<EOF

$(html_header)
$(html_body $1)
$(html_footer)

EOF
}

print_module_stats(){

TOTAL_COUNT=0

## iterate over the repo and find out all pom.xmls

for pom in `find $1 -name "pom.xml"`
do
  COUNT=0
  FILE_TYPES=""
  #echo $pom
  PARENT_DIR="${pom%/*}"
  echo "<tr>"
  echo "<td>${PARENT_DIR##*/}</td>" 
  echo "<td>$PARENT_DIR</td>" 
  COUNT=`find "$PARENT_DIR" -type f | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  echo "<td>$COUNT</td>" 
  echo "<td>$(module_details $PARENT_DIR)</td>"
  echo "</tr>"
#  echo Total number of files in directory `find "$PARENT_DIR" -type f | wc -l`
  for file in `ls $PARENT_DIR`
  do
   if [ -f $file ];then 
   echo "File extension is: ${file##*\.}"
   fi
  done 
  #echo $PARENT_DIR
done
echo "<tr><td>"-"</td><td>"-"</td><td>$TOTAL_COUNT</td><td>"-"</td></tr>"
}

#################
## main #########

GLASSFISH_DIR=$1

generate_report $1
#print_module_stats $1
