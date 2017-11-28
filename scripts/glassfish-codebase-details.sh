#!/bin/bash
#################
## functions ####

TOTAL_COUNT=0

html_header(){


echo "<html>
      <head>

      <title>glassfish-stats</title>
      <style>
       table, th, td {
          border: 1px solid black;
        }
       table {
         border-collapse: collapse;
         width: 100%;
         table-layout: fixed;
         }
      </style>
      </head>" > ./glassfish-stats.html

}

html_body(){
echo "<body>" >> ./glassfish-stats.html
echo "<table border=\"1\">" >> ./glassfish-stats.html
echo "<tr>" >> ./glassfish-stats.html
echo "<th>Module</th>" >> ./glassfish-stats.html
echo "<th>Path</th>" >> ./glassfish-stats.html
echo "<th>File Count</th>" >> ./glassfish-stats.html
echo "<th>Details</th>" >> ./glassfish-stats.html
echo "</tr>" >> ./glassfish-stats.html
}

html_footer(){

echo "</table>" >> ./glassfish-stats.html
echo "</body>" >> ./glassfish-stats.html
echo "</html>" >> ./glassfish-stats.html
}

module_details(){
echo "<table border=\"1\">" >> ./glassfish-stats.html
echo "<tr>" >> ./glassfish-stats.html
echo "<th>Type</th>" >> ./glassfish-stats.html
echo "<th>Count</th>" >> ./glassfish-stats.html
echo "</tr>" >> ./glassfish-stats.html

EXTENSIONS=()
FILE_TYPES=""
FILE_EXTENSION=""


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
  dump_module_stats $ext $COUNTER
  COUNTER=0
done

echo "</table>" >> ./glassfish-stats.html

}

dump_module_stats(){
echo "<tr>" >> ./glassfish-stats.html
echo "<td>$1</td>" >> ./glassfish-stats.html
echo "<td>$2</td>" >> ./glassfish-stats.html
echo "</tr>" >> ./glassfish-stats.html
}

generate_report(){


$(html_header)
$(html_body)
$(print_module_stats $1)
$(html_footer)

}

print_module_stats(){


## iterate over the repo and find out all pom.xmls

for pom in `find $1 -name "pom.xml"`
do

  COUNT=0
  # $pom
  PARENT_DIR="${pom%/*}"
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  
#echo "<tr>" >> ./glassfish-stats.html
#echo "<td>${PARENT_DIR##*/}</td> 
#echo "<td>$PARENT_DIR</td> 
#echo "<td>$COUNT</td> 
#  
  
echo "<td>${PARENT_DIR##*/}</td>" >> ./glassfish-stats.html
echo "<td>$PARENT_DIR</td>" >> ./glassfish-stats.html
echo "<td>$COUNT</td>" >> ./glassfish-stats.html
echo "<td>" >> ./glassfish-stats.html
$(module_details $PARENT_DIR)

echo "</td>" >> ./glassfish-stats.html
echo "</tr>" >> ./glassfish-stats.html

done
echo "<tr><td>-</td><td>-</td><td>$TOTAL_COUNT</td><td>-</td></tr>" >> ./glassfish-stats.html
}

dump_module_data(){
  COUNT=0
  # $pom
  PARENT_DIR="${1%/*}"
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  
echo "<tr>" >> ./glassfish-stats.html
echo "<td>${PARENT_DIR##*/}</td>" >> ./glassfish-stats.html
echo "<td>$PARENT_DIR</td>" >> ./glassfish-stats.html
echo "<td>$COUNT</td>" >> ./glassfish-stats.html

}

#################
## main #########

GLASSFISH_DIR=$1

generate_report $1
