#!/bin/bash
#################
## functions ####

TOTAL_COUNT=0
OUTPUT_FILE=""

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
      </head>" > $OUTPUT_FILE.html

}

html_body(){
echo "<body>" >> $OUTPUT_FILE.html
echo "<table border=\"1\">" >> $OUTPUT_FILE.html
echo "<tbody>" >> $OUTPUT_FILE.html
echo "<tr>" >> $OUTPUT_FILE.html
echo "<th>Module</th>" >> $OUTPUT_FILE.html
echo "<th>Path</th>" >> $OUTPUT_FILE.html
echo "<th>File Count</th>" >> $OUTPUT_FILE.html
echo "<th>Details</th>" >> $OUTPUT_FILE.html
echo "</tr>" >> $OUTPUT_FILE.html
}

html_footer(){

echo "</tbody>" >> $OUTPUT_FILE.html
echo "</table>" >> $OUTPUT_FILE.html
echo "</body>" >> $OUTPUT_FILE.html
echo "</html>" >> $OUTPUT_FILE.html
}

module_details(){
echo "<table border=\"1\">" >> $OUTPUT_FILE.html
echo "<tbody>" >> $OUTPUT_FILE.html
echo "<tr>" >> $OUTPUT_FILE.html
echo "<th>Type</th>" >> $OUTPUT_FILE.html
echo "<th>Count</th>" >> $OUTPUT_FILE.html
echo "</tr>" >> $OUTPUT_FILE.html

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

echo "</tbody>" >> $OUTPUT_FILE.html
echo "</table>" >> $OUTPUT_FILE.html

}

dump_module_stats(){
echo "<tr>" >> $OUTPUT_FILE.html
echo "<td>$1</td>" >> $OUTPUT_FILE.html
echo "<td>$2</td>" >> $OUTPUT_FILE.html
echo "</tr>" >> $OUTPUT_FILE.html
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
  
#echo "<tr>" >> $OUTPUT_FILE.html
#echo "<td>${PARENT_DIR##*/}</td> 
#echo "<td>$PARENT_DIR</td> 
#echo "<td>$COUNT</td> 
#  
echo "<tr>" >> $OUTPUT_FILE.html  
echo "<td>${PARENT_DIR##*/}</td>" >> $OUTPUT_FILE.html
echo "<td>$PARENT_DIR</td>" >> $OUTPUT_FILE.html
echo "<td>$COUNT</td>" >> $OUTPUT_FILE.html
echo "<td>" >> $OUTPUT_FILE.html
$(module_details $PARENT_DIR)

echo "</td>" >> $OUTPUT_FILE.html
echo "</tr>" >> $OUTPUT_FILE.html

done
echo "<tr><td>-</td><td>-</td><td>$TOTAL_COUNT</td><td>-</td></tr>" >> $OUTPUT_FILE.html
}

dump_module_data(){
  COUNT=0
  # $pom
  PARENT_DIR="${1%/*}"
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  
echo "<tr>" >> $OUTPUT_FILE.html
echo "<td>${PARENT_DIR##*/}</td>" >> $OUTPUT_FILE.html
echo "<td>$PARENT_DIR</td>" >> $OUTPUT_FILE.html
echo "<td>$COUNT</td>" >> $OUTPUT_FILE.html

}

#################
## main #########

GLASSFISH_DIR=$1

OUTPUT_FILE=${1##*\/}

echo "Output file: $OUTPUT_FILE.html"

generate_report $1
