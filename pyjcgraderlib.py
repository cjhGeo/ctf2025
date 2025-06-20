import requests as _requests
from hashlib import blake2s as _blake2s
from time import time as _time

class DSGraderClient:
  def __init__(self, endpoint):
    self._endpoint = endpoint
    print("DSGraderClient:", _requests.get(self._endpoint+'ping').text)

  def submitFile(self, file):
    try:
      return _requests.post(self._endpoint+'submission', files={'uploadedFile':open(file, 'rb')}).text
    except:
      print('Error submitting file')

# USAGE
#
# import pyjcgraderlib as ctfgrader
# grader = ctfgrader.DSGraderClient("GRADER_URL")
# grader.submitFile("PATH_TO_FILE")
