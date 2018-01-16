#!/usr/bin/python3

from config import ScancodeToolkitConfig, CopyrightPluginConfig, TargetRepoConfig

class ScancodeTableHtmlGenerator(object):

    def __init__(self, project_wiki, file_metadata_dict):
        self.project_wiki = project_wiki
        self.file_metadata_dict = file_metadata_dict

    def dump_scan_code_table(self):
     with open(self.project_wiki, mode='a', encoding='utf-8') as f:
        f.write("<table>\n")
        f.write("<tbody>\n")
        self.dump_scancode_table_header(f)
        self.dump_scancode_table_data(f)
        self.dump_scancode_table_footer(f)

    @staticmethod
    def dump_scancode_table_header(f):
        f.write("<tr>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">No. of Files</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">Copyright</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">License</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"2\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">File Details</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">Package Dependency</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">Package Version</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">Brief Package Description</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">License Tech. IDs / BA (from PLS)"
                               "</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">Next Step</div>\n")
        f.write("   </th>\n")
        f.write("   <th colspan=\"1\">\n")
        f.write("     <div class=\"tablesorter-header-inner\">Notes</div>\n")
        f.write("   </th>\n")
        f.write("</tr>\n")

    @staticmethod
    def dump_scancode_table_footer(f):
        f.write("</tbody>\n")
        f.write("</table>\n")

    def dump_scancode_table_data(self, f):
        for file_metadata in self.file_metadata_dict:
            f.write("<tr>\n")
            f.write("<td></td>\n")
            f.write("<td>" + str(file_metadata.copyright) + "</td>\n")
            f.write("<td>" + str(file_metadata.license) + "</td>\n")
            f.write("<td>\n")
            self.dump_file_details(file_metadata, f)
            f.write("</td>\n")
            f.write("<td></td>\n")
            f.write("<td></td>\n")
            f.write("<td></td>\n")
            f.write("<td></td>\n")
            f.write("<td></td>\n")
            f.write("<td></td>\n")
            f.write("<td></td>\n")
            f.write("</tr>\n")

    def dump_file_details(self, file_metadata, f):
        file_ext_dic = self.file_metadata_dict.get(file_metadata)
        f.write("<table>\n")
        f.write("<tbody>\n")
        f.write("  <tr>\n")
        f.write("     <th>Extension</th>\n")
        f.write("     <th>Name</th>\n")
        f.write("  </tr>\n")
        for file_ext in file_ext_dic:
            f.write("  <tr>\n")
            f.write("    <td>" + file_ext + "</td>\n")
            f.write("    <td>\n")
            files = file_ext_dic.get(file_ext)
            f.write("      <ol>\n")
            for file_name in files:
                f.write("     <li>" + file_name + "</li>\n")
            f.write("      </ol>\n")
            f.write("    </td>\n")
            f.write("  </tr>\n")
        f.write("</tbody>\n")
        f.write("</table>\n")


class GenerateProjectWiki:

  def __init__(self, project_wiki):
    self.project_wiki = project_wiki

  def dump_header(self):
    with open(self.project_wiki, mode='w', encoding='utf-8') as f:
      f.write("<html>\n")
      f.write("<head>\n")
      self.dump_style(f)
      f.write("<title>" + self.project_wiki + "</title>\n")
      f.write("</head>\n")
      f.write("<body>\n")

  def dump_footer(self):
    with open(self.project_wiki, mode='a', encoding='utf-8') as f:
      f.write("</body>\n")
      f.write("</html>\n")

  def dump_project_details(self):
    with open(self.project_wiki, mode='a', encoding='utf-8') as f:
      f.write("<h2>Project Details</h2>\n")
      f.write("<p>Repository:<a href=\""
              + TargetRepoConfig.get_repo() + "\">" + TargetRepoConfig.get_repo() + "</a></p>\n")
      f.write("<p>Revision:</p>\n")

  def dump_copyright_check_header(self):
    with open(self.project_wiki, mode='a', encoding='utf-8') as f:
      f.write("<h2>Glassfish copyright plugin</h2>\n")
      f.write("<p>Version used: " + CopyrightPluginConfig.get_version() + "</p>\n")
      f.write("<ac:structured-macro ac:name=\"code\">\n")
      f.write("  <ac:plain-text-body><![CDATA[")

  def dump_copyright_check_footer(self):
    with open(self.project_wiki, mode='a', encoding='utf-8') as f:
      f.write("  ]]></ac:plain-text-body>\n")
      f.write(" </ac:structured-macro>\n")
      f.write(" <p> </p>\n")

  def dump_scancode_toolkit_header(self):
    with open(self.project_wiki, mode='a', encoding='utf-8') as f:
      f.write("<h2>Scancode results</h2>\n")
      f.write("<p>Version used: " + ScancodeToolkitConfig.get_version() + "</p>\n")
      f.write("<ac:structured-macro ac:name=\"code\">\n")
      f.write("  <ac:plain-text-body><![CDATA[")

  def dump_scancode_toolkit_footer(self):
    with open(self.project_wiki, mode='a', encoding='utf-8') as f:
      f.write("  ]]></ac:plain-text-body>\n")
      f.write(" </ac:structured-macro>\n")
      f.write(" <p> </p>\n")

  def dump_dependency_details_header(self):
    with open(self.project_wiki, mode='a', encoding='utf-8') as f:
      f.write("<h2>Binary Dependencies</h2>\n")
      f.write("<p>Dependency list - <ac:link>\n")
      f.write("    <ri:attachment ri:filename=\"" + TargetRepoConfig.get_repo_name()
              + "-dependency-list.txt\"></ri:attachment>\n")
      f.write("  </ac:link>\n")
      f.write("</p>\n")
      f.write("<p>Note: We are ignoring all the dependencies on our code, "
              "such as the org.glassfish artifacts and the javax.\* artifacts.</p>\n")
      f.write("<p> </p>\n")
      f.write("<pre>mvn dependency:list -DexcludeGroupIds=javax</pre>\n")

  @staticmethod
  def dump_style(f):
    f.write("<style>\n")
    f.write("table, th, td {\n")
    f.write("border: 1px solid black;\n")
    f.write("border-collapse: collapse;\n")
    f.write("}\n")
    f.write("</style>\n")
