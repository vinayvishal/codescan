#!/usr/bin/python3

import requests
import json
import sys
from datetime import datetime
from time import time

class dependencyDetailsFetcher():

  def fetchReleaseYear(self,groupId,artifactId,version):
    url = self.constructArtifactURL(groupId, artifactId)
    print url
    response = requests.get(url)
    artifactJson = json.loads(response.text);

    artifacts = artifactJson["response"]["docs"]
    for artifact in artifacts:
      id = artifact["id"]
      # print "Id as returned in response:", id
      # print "Constructed GAV", self.constructGAV(groupId,artifactId,version)
      if id == self.constructGAV(groupId,artifactId,version):
        timestamp = artifact["timestamp"]
        # print "Timestamp", timestamp
        print "Id:", id, "Time:",  datetime.fromtimestamp(timestamp/1000).strftime("%Y-%m-%d")
        break

    artifactTimestampDict = {}
    artifactVersionDict = {}
    for artifact in artifacts:
      artifactTimestampDict[artifact["timestamp"]] = artifact["id"]
      artifactVersionDict[artifact["id"]] = artifact["timestamp"]


    timestamps = sorted(artifactTimestampDict.iterkeys(),reverse=True)
    fetchedartifacts = sorted(artifactVersionDict.iterkeys(),reverse=True)

    latesttimestamp = timestamps[0]
    latestVersion = fetchedartifacts[0]

    print "Last updated version: " + artifactTimestampDict.get(latesttimestamp) + " Updated on "\
          + datetime.fromtimestamp(latesttimestamp/1000).strftime("%Y-%m-%d")

    print "Last released version: " + latestVersion + " Released on "\
          + datetime.fromtimestamp((artifactVersionDict.get(latestVersion))/1000).strftime("%Y-%m-%d")


      # print json.dumps(artifact)

    # print json.dumps(artifacts)

  def constructGAV(self,groupId,artifactId,version):
    return groupId + ":" + artifactId + ":" + version

  def processGAV(self,gav):
    gavValues = gav.split(":")
    for value in gavValues:
      print value

    groupId = gavValues[0]
    artifactId=gavValues[1]
    version=gavValues[2]

    return groupId, artifactId, version



  def fetchLastUpdatedYearFromFile(self, groupId, artifactId):

    f = open("input-complete-truncated-truncated-formatted.json", 'r')
    if f.mode == 'r':
      jsoninput = f.read()
      artifactJson = json.loads(jsoninput)
      artifacts = artifactJson['response']['docs']
      print json.dumps(artifacts)

  def constructArtifactURL(self,groupId,artifactId):
    __url = ""
    groupIdList = groupId.split('.')
    for group in groupIdList:
      __url += group + "/"


    __url = "http://search.maven.org/solrsearch/select?q=g:%22" \
            + groupId + "%22+AND+a:%22" + artifactId \
            + "%22&core=gav&rows=500&wt=json"
    return __url

if __name__ == "__main__":
  gav = sys.argv[1]
  ddf = dependencyDetailsFetcher()
  processedGAV = ddf.processGAV(gav)
  groupId = processedGAV[0]
  artifactId = processedGAV[1]
  version = processedGAV[2]

  print groupId,artifactId,version

  ddf.fetchReleaseYear(groupId, artifactId,version)
  # ddf.fetchLatestReleaseAndYear(groupId, artifactId)
