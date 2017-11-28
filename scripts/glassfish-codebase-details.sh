#!/bin/bash
#################
## functions ####

TOTAL_COUNT=0

html_header(){

cat > ./glassfish-stats.html <<EOF

 <html>
 <title>glassfish-stats</title>
EOF

}

html_body(){
cat >> ./glassfish-stats.html <<EOF
 <body>
 <table border=\"1\">
 <tr>
 <th>Module</th>
 <th>Path</th>
 <th>File Count</th>
 <th>Details</th>
 </tr>
EOF
}

# $(print_module_stats $1)
# </table>
# </body>

html_footer(){

cat >> ./glassfish-stats.html <<EOF
 </table>
 </body>
 </html>
EOF
}

module_details(){
cat >> ./glassfish-stats.html <<EOF
 <table border=\"1\">
 <tr>
 <th>Type</th>
 <th>Count</th>
 </tr>
EOF

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

cat >> ./glassfish-stats.html <<EOF
 </table>
EOF

}

dump_module_stats(){
cat >> ./glassfish-stats.html <<EOF
   <tr>
   <td>$1</td>
   <td>$2</td>
   </tr>
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
  # $pom
  PARENT_DIR="${pom%/*}"
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  
#  cat >> ./glassfish-stats.html <<EOF
#   <tr>
#   <td>${PARENT_DIR##*/}</td> 
#   <td>$PARENT_DIR</td> 
#   <td>$COUNT</td> 
#  
#  EOF
  
cat >> ./glassfish-stats.html <<EOF
    <td>${PARENT_DIR##*/}</td> 
    <td>$PARENT_DIR</td> 
    <td>$COUNT</td> 
    <td>
EOF
$(module_details $PARENT_DIR)

cat >> ./glassfish-stats.html <<EOF
 </td>
 </tr>
EOF

done
cat >> ./glassfish-stats.html <<EOF
 <tr><td>-</td><td>-</td><td>$TOTAL_COUNT</td><td>-</td></tr>
EOF
}

dump_module_data(){
  COUNT=0
  # $pom
  PARENT_DIR="${1%/*}"
  COUNT=`find "$PARENT_DIR" -type f ! -path "*target*" | wc -l`
  TOTAL_COUNT=`expr $TOTAL_COUNT + $COUNT`
  
cat >> ./glassfish-stats.html <<EOF
   <tr>
   <td>${PARENT_DIR##*/}</td> 
   <td>$PARENT_DIR</td> 
   <td>$COUNT</td> 
EOF

}

#################
## main #########

GLASSFISH_DIR=$1

generate_report $1
