#!/bin/bash

################ constants #############

dependency_list_str="\[INFO\] The following files have been resolved:"

# needs anchoring for an exact match, carat at the beginning and $
# at the end ensures the same.

flag_switch_string="^\[INFO\]$"
#dependency_substring=".*following.*"
#http_expression="http://([^/]+)/"

find_dependency_resolution_string="true"
process_dependencies="false"

################ functions #############

format_dependency(){

   dependency_str="$( cut -d ' ' -f 2- <<< "$line" )" 
   dependency_string=${dependency_str// }
   groupid="$( cut -d ':' -f 1 <<< "$dependency_string" )"
   artifactid="$( cut -d ':' -f 2 <<< "$dependency_string" )"
   scope="$( cut -d ':' -f 5 <<< "$dependency_string" )"
   version="$( cut -d ':' -f 4 <<< "$dependency_string" )"
#   echo "Group Id: $groupid ArtifactId: $artifactid Scope: $scope Version: $version"
   echo "    <tr>"
   echo "      <td colspan=\"1\">$scope</td>"
   echo "      <td colspan=\"1\"> </td>"
   echo "      <td colspan=\"1\"> </td>"
   echo "      <td colspan=\"1\">$groupid:$artifactid</td>"
   echo "      <td colspan=\"1\">$version</td>"
   echo "      <td colspan=\"1\"> </td>"
   echo "      <td colspan=\"1\">"
   echo "      <p> References:</p>"
   echo "      <ol>"
   echo "      <li> <a href=\"http://search.maven.org/#artifactdetails|$groupid|$artifactid|$version|jar\">http://search.maven.org/#artifactdetails|$groupid|$artifactid|$version|jar</a> </li>"
   echo "      <li> <a href=\"https://mvnrepository.com/artifact/$groupid/$artifactid/$version\">https://mvnrepository.com/artifact/$groupid/$artifactid/$version</a></li>"
   echo "      </ol></td>"
   echo "      <td colspan=\"1\"> </td>"
   echo "      <td colspan=\"1\"> </td>"
   echo "      <td colspan=\"1\"> </td>"
   echo "      <td colspan=\"1\"> </td>"
   echo "    </tr>"
}

print_table_header(){
   echo " <table>"
   echo "  <tbody>"
   echo "    <tr>"
   echo "      <th>"
   echo "        <div class=\"tablesorter-header-inner\">Scope</div>"
   echo "      </th>"
   echo "      <th>"
   echo "        <div class=\"tablesorter-header-inner\">License</div>"
   echo "      </th>"
   echo "      <th>"
   echo "        <div class=\"tablesorter-header-inner\">Package Dependency</div>"
   echo "      </th>"
   echo "      <th>"
   echo "        <div class=\"tablesorter-header-inner\">Artefacts</div>"
   echo "      </th>"
   echo "      <th colspan=\"1\">"
   echo "        <div class=\"tablesorter-header-inner\">Version</div>"
   echo "      </th>"
   echo "      <th>"
   echo "        <div class=\"tablesorter-header-inner\">Package Page</div>"
   echo "      </th>"
   echo "      <th colspan=\"1\">"
   echo "        <div class=\"tablesorter-header-inner\">Brief Description</div>"
   echo "      </th>"
   echo "      <th colspan=\"1\">"
   echo "        <div class=\"tablesorter-header-inner\">"
   echo "          <p>License Tech Ids /</p>"
   echo "          <p>BA (From PLS)</p>"
   echo "          <p> </p>"
   echo "        </div>"
   echo "      </th>"
   echo "      <th colspan=\"1\">"
   echo "        <div class=\"tablesorter-header-inner\">"
   echo "          <p>Next</p>"
   echo "          <p>Steps</p>"
   echo "        </div>"
   echo "      </th>"
   echo "      <th colspan=\"1\">"
   echo "        <div class=\"tablesorter-header-inner\">Modules</div>"
   echo "      </th>"
   echo "      <th colspan=\"1\">"
   echo "        <div class=\"tablesorter-header-inner\">Notes</div>"
   echo "      </th>"
   echo "    </tr>"
}

print_table_footer(){
  echo "  </tbody>"
  echo " </table>"

}


############### main ##################

DEPENDENCY_LOG_FILE=$1

#echo "Search string is $dependency_list_str"

print_table_header

while read line; do
#echo $line;

#echo "Processing line --> $line"
#echo "Search for dependency resolution string ? $find_dependency_resolution_string"
#echo "Process dependencies ? $process_dependencies"
if [ $find_dependency_resolution_string == "true" ];then
  if [[ $line =~ $dependency_list_str ]];then
   find_dependency_resolution_string="false" 
   process_dependencies="true"
   continue 
  fi
fi

if [ $process_dependencies == "true" ];then
 # echo $line
 # following regex truncates leading and trailing whitespaces 
  whitespaces_truncated_string="${line// }"
 # echo "whitespace truncated string : $whitespaces_truncated_string"
  if [[ ${line// } =~ $flag_switch_string ]];then
   find_dependency_resolution_string="true" 
   process_dependencies="false" 
  else
#   echo $line
# cuts string based on ' ' , and then stores everything after first
# occurence to variable dependency_str
   format_dependency $line
  fi
fi;

done<$DEPENDENCY_LOG_FILE
print_table_footer
