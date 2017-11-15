# `process-dependency.sh`

The output of `maven dependency:list` lists out the bunch of discrepancies for a the particular project. This script takes this output as input and produces output in html tabular format. This output can directly be used in an html page instead of manually copy-pasting the details onto a web page.

## `mvn dependency:list` output

Here is the snippet from `maven depedency:list`, this is the input to the script `process-dependency.sh`.

```bash
[INFO]
[INFO] --- maven-dependency-plugin:2.8:list (default-cli) @ grizzly-thrift ---
[INFO]
[INFO] The following files have been resolved:
[INFO]    org.apache.zookeeper:zookeeper:jar:3.4.8:compile

```

## Executing `process-dependency.sh` script

```bash
./process-dependency.sh <mvn dependency:list output>
```
```bash
./process-dependency.sh ../samples/process-dependencies/maven-dependency.txt | tee ../samples/process-dependencies/html-output.txt
```

## html output

```bash
<table>
 <tbody>
   <tr>
     <th>
       <div class="tablesorter-header-inner">Scope</div>
     </th>
     <th>
       <div class="tablesorter-header-inner">License</div>
     </th>
     <th>
       <div class="tablesorter-header-inner">Package Dependency</div>
     </th>
     <th>
       <div class="tablesorter-header-inner">Artefacts</div>
     </th>
     <th colspan="1">
       <div class="tablesorter-header-inner">Version</div>
     </th>
     <th>
       <div class="tablesorter-header-inner">Package Page</div>
     </th>
     <th colspan="1">
       <div class="tablesorter-header-inner">Brief Description</div>
     </th>
     <th colspan="1">
       <div class="tablesorter-header-inner">
         <p>Ids</p>
       </div>
     </th>
     <th colspan="1">
       <div class="tablesorter-header-inner">
         <p>Next steps</p>
       </div>
     </th>
     <th colspan="1">
       <div class="tablesorter-header-inner">Modules</div>
     </th>
     <th colspan="1">
       <div class="tablesorter-header-inner">Notes</div>
     </th>
   </tr>
   <tr>
     <td colspan="1">compile</td>
     <td colspan="1"> </td>
     <td colspan="1"> </td>
     <td colspan="1">org.apache.zookeeper:zookeeper</td>
     <td colspan="1">3.4.8</td>
     <td colspan="1"> </td>
     <td colspan="1"> </td>
     <td colspan="1"> </td>
     <td colspan="1"> </td>
     <td colspan="1"> </td>
     <td colspan="1"> </td>
   </tr>
 </tbody>
</table>

```
This is how the table looks like:

Scope|License|Package Dependency|Artefacts|Version|Package Page|Brief Description|Modules|Notes
-----|-------|------------------|---------|-------|------------|-----------------|-------|-----
compile|||org.apache.zookeeper:zookeeper|3.4.8||||
