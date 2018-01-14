#!/usr/bin/python3


class ScancodeTableHtmlGenerator(object):

    def __init__(self, output_html, file_metadata_dict):
        self.output_file = open(output_html, "w+")
        self.file_metadata_dict = file_metadata_dict

    def dump_scan_code_table(self):

        # self.output_file = open(self.output_html,"w")
        self.output_file.write("<html>\n")
        self.output_file.write("<head>\n")
        self.output_file.write("<style>\n")
        self.output_file.write("table, th, td {\n")
        self.output_file.write("border: 1px solid black;\n")
        self.output_file.write("border-collapse: collapse;\n")
        self.output_file.write("}\n")
        self.output_file.write("</style>\n")
        self.output_file.write("</head>\n")
        self.output_file.write("<body>\n")
        self.output_file.write("<table>\n")
        self.output_file.write("<tbody>\n")
        self.dump_scancode_table_header()
        self.dump_scancode_table_data()
        self.dump_scancode_table_footer()
        self.output_file.close()

    def dump_scancode_table_header(self):
        self.output_file.write("<tr>\n")
        self.output_file.write("   <th colspan=\"1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">No. of Files</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">Copyright</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">License</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"2\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">File Details</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">Package Dependency</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">Package Version</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">Brief Package Description</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"\1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">License Tech. IDs / BA (from PLS)"
                               "</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"\1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">Next Step</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("   <th colspan=\"\1\">\n")
        self.output_file.write("     <div class=\"tablesorter-header-inner\">Notes</div>\n")
        self.output_file.write("   </th>\n")
        self.output_file.write("</tr>\n")

    def dump_scancode_table_footer(self):
        self.output_file.write("</tbody>\n")
        self.output_file.write("</table>\n")
        self.output_file.write("</body>\n")
        self.output_file.write("</html>")

    def dump_scancode_table_data(self):
        for file_metadata in self.file_metadata_dict:
            self.output_file.write("<tr>\n")
            self.output_file.write("<td></td>\n")
            self.output_file.write("<td>" + str(file_metadata.copyright) + "</td>\n")
            self.output_file.write("<td>" + str(file_metadata.license) + "</td>\n")
            self.output_file.write("<td\n>")
            self.dump_file_details(file_metadata)
            self.output_file.write("</td\n>")
            # self.dump_file_details(file_metadata)
            self.output_file.write("<td></td>\n")
            self.output_file.write("<td></td>\n")
            self.output_file.write("<td></td>\n")
            self.output_file.write("<td></td>\n")
            self.output_file.write("<td></td>\n")
            self.output_file.write("<td></td>\n")
            self.output_file.write("<td></td>\n")
            self.output_file.write("</tr>\n")

    def dump_file_details(self, file_metadata):
        file_ext_dic = self.file_metadata_dict.get(file_metadata)
        self.output_file.write("<table>\n")
        self.output_file.write("<tbody>\n")
        self.output_file.write("  <tr>\n")
        # self.output_file.write("     <th colspan=\"1\">\n")
        self.output_file.write("     <th>Extension</th>\n")
        # self.output_file.write("     <th colspan=\"1\">\n")
        self.output_file.write("     <th>Name</th>\n")
        self.output_file.write("  </tr>\n")
        for file_ext in file_ext_dic:
            self.output_file.write("  <tr>\n")
            self.output_file.write("    <td>" + file_ext + "</td>\n")
            self.output_file.write("    <td>" + "\n".join(file_ext_dic.get(file_ext)) + "</td>\n")
            self.output_file.write("  <tr>\n")
        self.output_file.write("</tbody>\n")
        self.output_file.write("</table>\n")
