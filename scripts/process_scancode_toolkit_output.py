#!/usr/bin/python3

import json
import sys
import re
from models import FileMetadata
from dump_html import ScancodeTableHtmlGenerator


def process_license_files(current_file, file_name, file_metadata_dict):
  license_array = []
  copyright_array = []
  licenses = current_file['licenses']
  for lic in licenses:
    license_array.append(lic['spdx_license_key'])

  copyrights = current_file['copyrights']
  for cprt in copyrights:
    # holders = "\n".join(cprt['holders'])
    holders = cprt['holders']
    for holder in holders:
      copyright_array.append(holder)

  file_metadata = FileMetadata(" ".join(set(copyright_array)), " ".join(set(license_array)))
  file_metadata_dict[file_metadata] = {"N/A": [file_name]}


def process_copyright_and_license_information(scancode_output_file):
  f = open(scancode_output_file, "r")

  if f.mode == 'r':
    file_contents = f.read()
    parsed_json = json.loads(file_contents)
    files = parsed_json['files']

    file_metadata_dict = {}

    for current_file in files:
      file_name = current_file['path']
      file_ext = current_file['extension']
      if not re.match("license", str(file_name).split("/")[-1], re.IGNORECASE):
        if len(file_ext) == 0:
          file_ext = "N/A"
        # Most of the file has got just one copyright. To get unique combination of license +
        # copyright # ,get the first copyright information from copyright array
        try:
          copyrights = current_file['copyrights']
          if len(copyrights) != 0:
            cprt = copyrights[0]
            holders = cprt['holders']
            if len(holders) != 0:
              cprt_holder = holders[0]
            else:
              cprt_holder = "N/A"
          else:
            cprt_holder = "N/A"
        except KeyError:
          cprt_holder = "N/A"

        try:
          licenses = current_file['licenses']
          # iterate over array of licenses for this file
          for lic in licenses:
            file_metadata = FileMetadata(cprt_holder, lic['spdx_license_key'])
            if file_metadata not in file_metadata_dict:
              file_ext_dic = {file_ext: [file_name]}
              file_metadata_dict[file_metadata] = file_ext_dic
            else:
              existing_file_ext_dic = file_metadata_dict.get(file_metadata)
              if file_ext in existing_file_ext_dic:
                contained_files = existing_file_ext_dic[file_ext]
                # print(contained_files)
                if file_name not in contained_files:
                  contained_files.append(file_name)
              else:
                existing_file_ext_dic[file_ext] = [file_name]
        except KeyError:
          file_metadata = FileMetadata(cprt_holder, "N/A")
          if file_metadata not in file_metadata_dict:
            file_ext_dic = {file_ext: [file_name]}
            file_metadata_dict[file_metadata] = file_ext_dic
          else:
            existing_file_ext_dic = file_metadata_dict.get(file_metadata)
            if file_ext in existing_file_ext_dic:
              contained_files = existing_file_ext_dic[file_ext]
              # print(contained_files)
              if file_name not in contained_files:
                contained_files.append(file_name)
            else:
              existing_file_ext_dic[file_ext] = [file_name]
      else:
        process_license_files(current_file, file_name, file_metadata_dict)

    # print_file_metadata(file_metadata_dict)

  return file_metadata_dict


def print_file_metadata(file_metadata_dict):
  for file_metadata in file_metadata_dict:
    print(file_metadata)
    file_ext_dic = file_metadata_dict.get(file_metadata)
    for file_ext in file_ext_dic:
      print('\t\t' + file_ext)
      contained_files = file_ext_dic[file_ext]
      for filename in contained_files:
        print('\t\t\t' + str(filename))


def dump_parsed_scancode_result(file_metadata_dict, output_file):
    html_generator = ScancodeTableHtmlGenerator(output_file, file_metadata_dict)
    html_generator.dump_scan_code_table()


# main() #

# if __name__ == "__main__":
#   scancode_results_file = sys.argv[1]
#   dump_html(process_copyright_and_license_information(scancode_results_file))
