#!/usr/bin/python3
import requests
import xml.etree.ElementTree as ET
import json
import sys
import re

class dependencyDetailsFetcher():
  
  def fetchPOM(self, groupId, artifactId, version):
    print "GAV"," ",groupId,":",artifactId,":",version
    url = self.constructPOMURL(groupId,artifactId,version)
    print "POM url:" + url

    response = requests.get(url)
    pom = response.text
    print pom
    root = ET.fromstring(pom)
    print "Printing root tag:"
    print root.tag
    print "Printing root attributes:"
    print root.attrib

    # for dependency in root.iter('dependency'):
    #   for child in dependency:
    #     print child.tag

    print "Iterating root childs"
    for dependencies in root:
      if dependencies.tag.endswith('dependencies'):
        print dependencies.tag
        for dependency in dependencies:
          gav = ""
          for child in dependency:
            match = re.search(r'(\{http://[\w.]+/POM/[\d.]+\})([\w]+)',child.tag)
            if match:
            # print "Schema -->" + match.group(1)
              element = match.group(2)
              if element == "groupId":
                groupId = child.text
              elif element == "artifactId":
                artifactId = child.text
              elif element == "version":
                version = child.text
            # print child.tag
            # print child.text
            # gav += child.text + ":"
          # print dependency.tag
          gav = groupId + ":" + artifactId + ":" + version
          print gav
        continue
      # print discrepancy.tag
      # print "printing child tag:"
      # print child.tag
      # print "printing child attributes:"
      # print child.attrib
      # for grandchild in child:
      #   print "Printing grandchild details:"
      #   print grandchild.tag

#    for modelVersion in project.findall("modelVersion"):
#      print modelVersion.tag, modelVersion.attrib

#    for dependencies in project.findall("dependencies"):
#      for dependency in dependencies.findall("dependency"):
#        print dependency.find("groupId").text



  def constructPOMURL(self,groupId,artifactId,version):     
    __url = "" 
    groupIdList = groupId.split('.')
    for group in groupIdList:
      __url += group + "/"

    __url = "http://search.maven.org/remotecontent?filepath=" + __url + artifactId + "/" + version + "/" + artifactId + "-" + version + ".pom"
    return __url

if __name__ == "__main__":
  groupId = sys.argv[1]
  artifactId = sys.argv[2]
  version = sys.argv[3] 
  ddf = dependencyDetailsFetcher()
  ddf.fetchPOM(groupId,artifactId,version)
