#!/usr/bin/python3


import sys
from subprocess import call
from os import path, listdir, getcwd
from configparser import ConfigParser
from process_scancode_toolkit_output import dump_parsed_scancode_result, process_copyright_and_license_information
from dump_html import GenerateProjectWiki
from config import TargetRepoConfig, DependencyConfig

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
  project_wiki = open(repo_name + ".html", mode='a', encoding='utf-8')
  call(["java", "-cp", copyright_jar, "org.glassfish.copyright.Copyright", "-g", "-c", "-N",
        repo_to_be_scanned], stdout=project_wiki)
  project_wiki.close()


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
  return codescan_toolkit_path


def scancode():
  codescan_toolkit_path = get_codescan_toolkit_path()
  project_wiki = open(repo_name + ".html", mode='a', encoding='utf-8')
  call([path.join(codescan_toolkit_path, "scancode"),
       '--diag', '-n', '10', '--format', 'json', '-c', '-l', '-p', '-u', '-e', '-i',
       repo_to_be_scanned, str(repo_to_be_scanned).split("/")[-1] + ".json"], stderr=project_wiki)
  project_wiki.close()


def execute_maven_dependency_list():
  print(DependencyConfig.get_exclude_groups())
  dependency_list_output = open(repo_name + "-dependency-list.txt", mode='w', encoding='utf-8')
  call(['mvn', 'dependency:list', '-DexcludeGroupIds=' + DependencyConfig.get_exclude_groups()+"'"],
       cwd=TargetRepoConfig.get_path(), stdout=dependency_list_output)
  dependency_list_output.close()


def parse_mvn_dependency_output():
  cwd = getcwd()
  process_discrepancy_path = path.join(cwd, "process-dependency.sh")
  project_wiki = open(repo_name + ".html", mode='a', encoding='utf-8')
  call([process_discrepancy_path, TargetRepoConfig.get_repo_name() + "-dependency-list.txt"], stdout=project_wiki)
  project_wiki.close()

# main ##

if __name__ ==  "__main__":

  repo_name = TargetRepoConfig.get_repo_name()
  repo_to_be_scanned = TargetRepoConfig.get_path()
  print("Scanning " + repo_name + " repository:")
  output_wiki = GenerateProjectWiki(repo_name + ".html")
  output_wiki.dump_header()
  output_wiki.dump_project_details()
  print("Starting copyright check..")
  output_wiki.dump_copyright_check_header()
  copyright_check()
  output_wiki.dump_copyright_check_footer()
  print("Copyright check done.")
  print("Starting copyright repair..")
  copyright_repair()
  print("Copyright repair done.")
  print("starting code scan..")
  output_wiki.dump_scancode_toolkit_header()
  scancode()
  output_wiki.dump_scancode_toolkit_footer()
  print("code scanning done.")
  print("Scancode results being dumped to html..")
  dump_parsed_scancode_result(process_copyright_and_license_information(repo_name + ".json"), repo_name + ".html")
  print("Results dumped to html.")
  output_wiki.dump_dependency_details_header()
  # maven dependency run #
  execute_maven_dependency_list()
  # maven dependency analysis #
  # maven dependency table enrichment with release date/latest release#
  parse_mvn_dependency_output()
  output_wiki.dump_footer()



