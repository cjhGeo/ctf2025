import requests

# Grader endpoint URL
grader_url = "http://52.184.80.178:5001/grade"

# Submit the file
def grade(file_path="predictions.csv"):
  with open(file_path, "rb") as f:
      files = {"file": (file_path, f)}
      response = requests.post(grader_url, files=files)
  
  # Handle response
  if response.ok:
      result = response.json()
      print(response.text)
  else:
      print("Submission failed:", response.text)


# USAGE
#
# import pyjcgraderlib as ctfgrader
# ctfgrader.grade("PATH_TO_FILE")
