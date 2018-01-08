#!/usr/bin/python3

import json
import sys
from models import Copyright, License, FileMetadata


def process_copyright_and_license_information(scancode_output_file):
  f = open(scancode_output_file, "r")

  if f.mode == 'r':
    file_contents = f.read()
    parsed_json = json.loads(file_contents)
    files = parsed_json['files']

    file_metadata_dict = {}

    for current_file in files:
      statement = ""
      holder = ""
      copyrights = current_file['copyrights']
      if len(copyrights) != 0:
        copyright = copyrights[0]
        statements = copyright['statements']
        if len(statements) != 0:
          statement = statements[0]
        holders = copyright['holders']
        if len(holders) != 0:
          holder = holders[0]

      copyright_obj = Copyright(statement, holder)
      licenses = current_file['licenses']

      for license in licenses:
        file_metadata = FileMetadata(License(license['spdx_license_key']), copyright_obj)
        if file_metadata not in file_metadata_dict:
          file_metadata_dict[file_metadata] = [current_file['path']]
        else:
          contained_files = file_metadata_dict.get(file_metadata)
          if current_file['path'] not in contained_files:
            contained_files.append(current_file['path'])

    for file_metadata in file_metadata_dict:
      print (file_metadata)
      values = file_metadata_dict.get(file_metadata)
      for value in values:
        print ('\t\t' + str(value))
  return file_metadata_dict


def dump_html():
  return "hello"


# main() #

if __name__ == "__main__":

  scancode_results_file = sys.argv[1]
  process_copyright_and_license_information(scancode_results_file)
