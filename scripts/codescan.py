#!/usr/bin/python3


import sys
from subprocess import call
from os import path, listdir
from configparser import ConfigParser

# copyright check #

def copyright_check():
  config = ConfigParser()
  config.read("codescan.ini")
  copyright_path = config['COPYRIGHT_PLUGIN']['PATH']
  copyright_jar = ""
  if path.isdir(copyright_path):
    copyright_plugin_target_dir = path.join(copyright_path, "target")
    if path.exists(copyright_plugin_target_dir):
      for filename in listdir(copyright_plugin_target_dir):
          if filename.endswith("jar"):
            copyright_jar = path.join(copyright_plugin_target_dir, filename)
    else:
        print ("Copyright plugin directory doesn't have a target folder. Please run mvn clean install.")
        exit(1)
  else:
    print ("Specified copyright plugin path doesn't exist.")
    exit(1)

  if path.exists(copyright_jar):
    print ("Executing copyright plugin")
    call(["java", "-cp", copyright_jar, "org.glassfish.copyright.Copyright", "-g", "-c", "-r", repo_to_be_scanned])
  else:
    print ("Copyright plugin jar doesn't exist in  target directory")


# copyright repair #

# codescan-toolkit-run #

# process-scancode-tookit-json-output #

# maven dependency run #

# maven dependency analysis #

# maven dependency table enrichment with release date/latest release#

# main ##

# main() #

if __name__ == "__main__":

  repo_to_be_scanned = sys.argv[1]
  copyright_check()
  print (repo_to_be_scanned)

