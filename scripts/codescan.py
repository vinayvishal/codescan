#!/usr/bin/python3


import sys
from subprocess import call
from os import path, listdir
from configparser import ConfigParser
from process_scancode_toolkit_output import dump_html, process_copyright_and_license_information

# copyright check #


def get_copyright_plugin_jar_path():
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
        print("Copyright plugin directory doesn't have a target folder. Please run mvn clean install.")
        exit(1)
  else:
    print("Specified copyright plugin path doesn't exist.")
    exit(1)

  if path.exists(copyright_jar):
    return copyright_jar
  else:
    print("Copyright plugin jar doesn't exist in  target directory")


def copyright_check():
  copyright_jar = get_copyright_plugin_jar_path()
  call(["java", "-cp", copyright_jar, "org.glassfish.copyright.Copyright", "-g", "-c", "-N", repo_to_be_scanned])


def copyright_repair():
  copyright_jar = get_copyright_plugin_jar_path()
  call(["java", "-cp", copyright_jar, "org.glassfish.copyright.Copyright", "-g", "-c", "-q", "-r", "-N", repo_to_be_scanned])# copyright repair #

# codescan-toolkit-run #


def get_codescan_toolkit_path():
  config = ConfigParser()
  config.read("codescan.ini")
  codescan_toolkit_path = config['CODESCAN_TOOLKIT']['PATH']
  if not path.isdir(codescan_toolkit_path):
    print("Specified toolkit path " + codescan_toolkit_path + " is not a directory.")
    exit(1)
  print(codescan_toolkit_path)
  print(str(codescan_toolkit_path).split("/")[-1])
  return codescan_toolkit_path

def scancode():
  codescan_toolkit_path = get_codescan_toolkit_path()
  call([path.join(codescan_toolkit_path, "scancode"),
       '--diag', '-n', '10', '--format', 'json', '-c', '-l', '-p', '-u', '-e', '-i',
       repo_to_be_scanned, str(repo_to_be_scanned).split("/")[-1] + ".json"])
# )
# process-scancode-tookit-json-output #


# maven dependency run #

# maven dependency analysis #

# maven dependency table enrichment with release date/latest release#

# main ##

# main() #

if __name__ == "__main__":

  repo_to_be_scanned = sys.argv[1]
  repo_name = str(repo_to_be_scanned).split("/")[-1]
  print("Scanning " + repo_name + " repository:")
  print("Starting copyright check..")
  copyright_check()
  print("Copyright check done.")
  print("Starting copyright repair..")
  copyright_repair()
  print("Copyright repair done.")
  print("starting code scan..")
  scancode()
  print("code scanning done.")
  print("Scancode results being dumped to html..")
  dump_html(process_copyright_and_license_information(repo_name + ".json"), repo_name + ".html")
  print("Results dumped to html.")



