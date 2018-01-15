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
      f.write("    <ri:attachment ri:filename=\"" + TargetRepoConfig.get_repo_name() + "-dependency-list.txt\"\n")
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


# <h2>Project details</h2>
# <p>Repository: <a href="https://github.com/javaee/javax.transaction">https://github.com/javaee/javax.transaction</a>
# </p>
# <p>Revision: <span style="color: rgb(88,96,105);">Latest commit </span> <a class="commit-tease-sha" href="https://github.com/javaee/javax.transaction/commit/684cdb9c9ed39e33442a98c1279d7c335cab5019">684cdb9</a> <span style="color: rgb(88,96,105);"> </span> <span style="color: rgb(88,96,105);">on 14 Jun 2017</span>
# </p>
# <h2>Glassfish copyright plugin</h2>
# <p>Version used: 1.49</p>
# <p>Copyright issues found</p>
# <ac:structured-macro ac:name="code">
#   <ac:plain-text-body><![CDATA[$ python3 codescan.py /home/vinay/work/repo/javax.transaction
# Executing copyright plugin
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/Transactional.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/TransactionManager.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/Status.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/TransactionScoped.java: Copyright year is wrong; is 2017, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/UserTransaction.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/HeuristicRollbackException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/package.html: Copyright year is wrong; is 2010, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/TransactionalException.java: Copyright year is wrong; is 2017, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/Synchronization.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/SystemException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/xa/package.html: Copyright year is wrong; is 2010, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/xa/Xid.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/xa/XAResource.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/xa/XAException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/HeuristicCommitException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/TransactionRolledbackException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/InvalidTransactionException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/RollbackException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/Transaction.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/NotSupportedException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/TransactionSynchronizationRegistry.java: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/HeuristicMixedException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/java/javax/transaction/TransactionRequiredException.java: Copyright year is wrong; is 2015, should be
# /home/vinay/work/repo/javax.transaction/src/main/resources/META-INF/README: No copyright
# /home/vinay/work/repo/javax.transaction/src/main/javadoc/doc-files/speclicense.html: No copyright
# /home/vinay/work/repo/javax.transaction/osgi.bundle: Copyright year is wrong; is 2013, should be
# /home/vinay/work/repo/javax.transaction/pom.xml: Copyright year is wrong; is 2017, should be
# /home/vinay/work/repo/javax.transaction/CONTRIBUTING.md: No copyright
# /home/vinay/work/repo/javax.transaction/LICENSE: Wrong copyright
# /home/vinay/work/repo/javax.transaction/release.sh: No copyright
# No Copyright:		4
# Wrong Copyright:	1
# Wrong Copyright Date:	25
#
#  ]]></ac:plain-text-body>
# </ac:structured-macro>
# <p> </p>
# <h2>Scancode results</h2>
# <ac:structured-macro ac:name="code">
#   <ac:plain-text-body><![CDATA[$ ./scancode --diag -n 10 --format json -c -l -p -u -e -i ~/work/repo/javax.transaction/ results/javax.transaction.json
# Scanning files for: infos, licenses, copyrights, packages, emails, urls with 10 process(es)...
# Building license detection index...Done.
# Scanning files...
# [####################] 40
# Scanning done.
# Scan statistics: 40 files scanned in 25s.
# Scan options:    infos, licenses, copyrights, packages, emails, urls with 10 process(es).
# Scanning speed:  1.83 files per sec.
# Scanning time:   21s.
# Indexing time:   3s.
# Saving results]]></ac:plain-text-body>
# </ac:structured-macro>
# <p> </p>
# <p>Scancode result: <ac:link>
#     <ri:attachment ri:filename="javax.transaction.json"/>
#   </ac:link>
# </p>
# <p> </p>
# <table>
#   <tbody>
#     <tr>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">No. of Files</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Copyright</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">License</div>
#       </th>
#       <th colspan="2">
#         <div class="tablesorter-header-inner">File Details</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Package Dependency</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Package Version</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Brief Package Description</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">License Tech. IDs / BA (from PLS)</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Next Step</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Notes</div>
#       </th>
#     </tr>
#     <tr>
#       <td> </td>
#       <td>Oracle and/or its affiliates.</td>
#       <td> </td>
#       <td>
#         <table>
#           <tbody>
#             <tr>
#               <th>Extension</th>
#               <th>Name</th>
#             </tr>
#             <tr>
#               <td>.html</td>
#               <td>javax.transaction/src/main/javadoc/doc-files/speclicense.html</td>
#             </tr>
#           </tbody>
#         </table>
#       </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#     </tr>
#     <tr>
#       <td> </td>
#       <td>Oracle and/or its affiliates.</td>
#       <td>CDDL-1.1</td>
#       <td>
#         <table>
#           <tbody>
#             <tr>
#               <th>Extension</th>
#               <th>Name</th>
#             </tr>
#             <tr>
#               <td>.md</td>
#               <td>javax.transaction/CONTRIBUTING.md</td>
#             </tr>
#             <tr>
#               <td>.sh</td>
#               <td>javax.transaction/release.sh</td>
#             </tr>
#             <tr>
#               <td>.bundle</td>
#               <td>javax.transaction/osgi.bundle</td>
#             </tr>
#             <tr>
#               <td>.html</td>
#               <td>javax.transaction/src/main/java/javax/transaction/package.html javax.transaction/src/main/java/javax/transaction/xa/package.html</td>
#             </tr>
#             <tr>
#               <td>.java</td>
#               <td>javax.transaction/src/main/java/javax/transaction/Transactional.java javax.transaction/src/main/java/javax/transaction/TransactionManager.java javax.transaction/src/main/java/javax/transaction/Status.java javax.transaction/src/main/java/javax/transaction/TransactionScoped.java javax.transaction/src/main/java/javax/transaction/UserTransaction.java javax.transaction/src/main/java/javax/transaction/HeuristicRollbackException.java javax.transaction/src/main/java/javax/transaction/TransactionalException.java javax.transaction/src/main/java/javax/transaction/Synchronization.java javax.transaction/src/main/java/javax/transaction/SystemException.java javax.transaction/src/main/java/javax/transaction/HeuristicCommitException.java javax.transaction/src/main/java/javax/transaction/TransactionRolledbackException.java javax.transaction/src/main/java/javax/transaction/InvalidTransactionException.java javax.transaction/src/main/java/javax/transaction/RollbackException.java javax.transaction/src/main/java/javax/transaction/Transaction.java javax.transaction/src/main/java/javax/transaction/NotSupportedException.java javax.transaction/src/main/java/javax/transaction/TransactionSynchronizationRegistry.java javax.transaction/src/main/java/javax/transaction/HeuristicMixedException.java javax.transaction/src/main/java/javax/transaction/TransactionRequiredException.java javax.transaction/src/main/java/javax/transaction/xa/Xid.java javax.transaction/src/main/java/javax/transaction/xa/XAException.java</td>
#             </tr>
#           </tbody>
#         </table>
#       </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#     </tr>
#     <tr>
#       <td> </td>
#       <td>Oracle and/or its affiliates.</td>
#       <td>GPL-2.0-with-classpath-exception</td>
#       <td>
#         <table>
#           <tbody>
#             <tr>
#               <th>Extension</th>
#               <th>Name</th>
#             </tr>
#             <tr>
#               <td>.md</td>
#               <td>javax.transaction/CONTRIBUTING.md</td>
#             </tr>
#             <tr>
#               <td>.sh</td>
#               <td>javax.transaction/release.sh</td>
#             </tr>
#             <tr>
#               <td>.bundle</td>
#               <td>javax.transaction/osgi.bundle</td>
#             </tr>
#             <tr>
#               <td>.html</td>
#               <td>javax.transaction/src/main/java/javax/transaction/package.html javax.transaction/src/main/java/javax/transaction/xa/package.html</td>
#             </tr>
#             <tr>
#               <td>.java</td>
#               <td>javax.transaction/src/main/java/javax/transaction/Transactional.java javax.transaction/src/main/java/javax/transaction/TransactionManager.java javax.transaction/src/main/java/javax/transaction/Status.java javax.transaction/src/main/java/javax/transaction/TransactionScoped.java javax.transaction/src/main/java/javax/transaction/UserTransaction.java javax.transaction/src/main/java/javax/transaction/HeuristicRollbackException.java javax.transaction/src/main/java/javax/transaction/TransactionalException.java javax.transaction/src/main/java/javax/transaction/Synchronization.java javax.transaction/src/main/java/javax/transaction/SystemException.java javax.transaction/src/main/java/javax/transaction/HeuristicCommitException.java javax.transaction/src/main/java/javax/transaction/TransactionRolledbackException.java javax.transaction/src/main/java/javax/transaction/InvalidTransactionException.java javax.transaction/src/main/java/javax/transaction/RollbackException.java javax.transaction/src/main/java/javax/transaction/Transaction.java javax.transaction/src/main/java/javax/transaction/NotSupportedException.java javax.transaction/src/main/java/javax/transaction/TransactionSynchronizationRegistry.java javax.transaction/src/main/java/javax/transaction/HeuristicMixedException.java javax.transaction/src/main/java/javax/transaction/TransactionRequiredException.java javax.transaction/src/main/java/javax/transaction/xa/Xid.java javax.transaction/src/main/java/javax/transaction/xa/XAException.java</td>
#             </tr>
#           </tbody>
#         </table>
#       </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#     </tr>
#     <tr>
#       <td> </td>
#       <td>Oracle and/or its affiliates.</td>
#       <td>GPL-1.0+</td>
#       <td>
#         <table>
#           <tbody>
#             <tr>
#               <th>Extension</th>
#               <th>Name</th>
#             </tr>
#             <tr>
#               <td>.html</td>
#               <td>javax.transaction/src/main/javadoc/doc-files/speclicense.html</td>
#             </tr>
#             <tr>
#               <td>.xml</td>
#               <td>javax.transaction/pom.xml</td>
#             </tr>
#             <tr>
#               <td>.java</td>
#               <td>javax.transaction/src/main/java/javax/transaction/xa/XAResource.java</td>
#             </tr>
#           </tbody>
#         </table>
#       </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#     </tr>
#     <tr>
#       <td> </td>
#       <td>the Free Software Foundation Free Software Foundation, Inc.</td>
#       <td>GPL-2.0 Apache-2.0 CDDL-1.1 GPL-2.0+ GPL-1.0+</td>
#       <td>
#         <table>
#           <tbody>
#             <tr>
#               <th>Extension</th>
#               <th>Name</th>
#             </tr>
#             <tr>
#               <td>N/A</td>
#               <td>javax.transaction/LICENSE</td>
#             </tr>
#           </tbody>
#         </table>
#       </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#     </tr>
#     <tr>
#       <td> </td>
#       <td>Oracle and/or its affiliates.</td>
#       <td>GPL-2.0</td>
#       <td>
#         <table>
#           <tbody>
#             <tr>
#               <th>Extension</th>
#               <th>Name</th>
#             </tr>
#             <tr>
#               <td>.html</td>
#               <td>javax.transaction/src/main/javadoc/doc-files/speclicense.html</td>
#             </tr>
#             <tr>
#               <td>.xml</td>
#               <td>javax.transaction/pom.xml</td>
#             </tr>
#             <tr>
#               <td>.java</td>
#               <td>javax.transaction/src/main/java/javax/transaction/xa/XAResource.java</td>
#             </tr>
#           </tbody>
#         </table>
#       </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#       <td> </td>
#     </tr>
#   </tbody>
# </table>
# <p> </p>
# <h2>Binary Dependencies</h2>
# <p>Dependency list - <ac:link>
#     <ri:attachment ri:filename="jta-dependency.txt"/>
#   </ac:link>
# </p>
# <p>Note: We are ignoring all the dependencies on our code, such as the org.glassfish artifacts and the javax.\* artifacts.</p>
# <p>No other dependencies reported for this project.</p>
# <p> </p>
# <pre>mvn <a href="http://dependencylist">dependency:list</a> -DexcludeGroupIds=javax</pre>
# <table>
#   <tbody>
#     <tr>
#       <th>
#         <div class="tablesorter-header-inner">Scope</div>
#       </th>
#       <th>
#         <div class="tablesorter-header-inner">License</div>
#       </th>
#       <th>
#         <div class="tablesorter-header-inner">Package Dependency</div>
#       </th>
#       <th>
#         <div class="tablesorter-header-inner">Artefacts</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Version</div>
#       </th>
#       <th>
#         <div class="tablesorter-header-inner">Package Page</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Brief Description</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">
#           <p>License Tech Ids /</p>
#           <p>BA (From PLS)</p>
#           <p> </p>
#         </div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">
#           <p>Next</p>
#           <p>Steps</p>
#         </div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Modules</div>
#       </th>
#       <th colspan="1">
#         <div class="tablesorter-header-inner">Notes</div>
#       </th>
#     </tr>
#     <tr>
#       <td colspan="1">provided</td>
#       <td colspan="1"> </td>
#       <td colspan="1"> </td>
#       <td colspan="1">org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.1_spec</td>
#       <td colspan="1">1.0.0.Beta1</td>
#       <td colspan="1"> </td>
#       <td colspan="1">
#         <p>References:</p>
#         <ol>
#           <li>
#             <a>http://search.maven.org/#artifactdetails|org.jboss.spec.javax.interceptor|jboss-interceptors-api_1.1_spec|1.0.0.Beta1|jar</a>
#           </li>
#           <li>
#             <a href="https://mvnrepository.com/artifact/org.jboss.spec.javax.interceptor/jboss-interceptors-api_1.1_spec/1.0.0.Beta1">https://mvnrepository.com/artifact/org.jboss.spec.javax.interceptor/jboss-interceptors-api_1.1_spec/1.0.0.Beta1</a>
#           </li>
#         </ol>
#       </td>
#       <td colspan="1"> </td>
#       <td colspan="1"> </td>
#       <td colspan="1"> </td>
#       <td colspan="1"> </td>
#     </tr>
#   </tbody>
# </table>
# <p> </p>
# <p> </p>
# <h2>Fossology Results</h2>
# <p>Fossology results can be found at - </p>
# <p>Impression - Results are in sync with <code>Scancode</code> results.</p>
# <h2>Remediation</h2>
# <p> </p>
# <p> </p>
