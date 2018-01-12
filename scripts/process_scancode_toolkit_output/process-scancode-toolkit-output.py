#!/usr/bin/python3

import json
import sys
from models import Copyright, License, FileMetadata
from dump_html import ScancodeTableHtmlGenerator


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
      # Most of the file has got just one copyright. To get unique combination of license + copyright \
      # ,get the first copyright information from copyright array
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

      # iterate over array of licenses for this file
      for license in licenses:
        file_metadata = FileMetadata(copyright_obj, License(license['spdx_license_key']))
        if file_metadata not in file_metadata_dict:
          file_ext_dic = {}
          file_ext = current_file['extension']
          if len(file_ext) == 0:
            file_ext = "N/A"
          file_ext_dic[file_ext] = [current_file['path']]
          file_metadata_dict[file_metadata] = [file_ext_dic]
        else:
          existing_file_ext_dic = file_metadata_dict.get(file_metadata)
          contained_files = existing_file_ext_dic.get(file_ext)
          if current_file['path'] not in contained_files:
            contained_files.append(current_file['path'])

    for file_metadata in file_metadata_dict:
      print (file_metadata)
      file_ext_dic = file_metadata_dict.get(file_metadata)
      for file_ext in file_ext_dic:
        print('\t\t' + file_ext)
        contained_files = file_ext_dic[file_ext]
        for filename in contained_files:
          print ('\t\t\t' + str(filename))
  return file_metadata_dict


def dump_html(file_metadata_dict):
  html_generator = ScancodeTableHtmlGenerator("/home/vinay/out.html", file_metadata_dict)
  html_generator.dump_scan_code_table()


# main() #

if __name__ == "__main__":

  scancode_results_file = sys.argv[1]
  dump_html(process_copyright_and_license_information(scancode_results_file))
