import requests

# Grader endpoint URL
grader_url = "http://grader-server-ip:5001/grade/challenge1"

# Submit the file
grade(file_path="predictions.csv"):
  with open(file_path, "rb") as f:
      files = {"submission": (file_path, f)}
      response = requests.post(grader_url, files=files)
  
  # Handle response
  if response.ok:
      result = response.json()
      print("Score:", result.get("score"))
      print("Flag:", result.get("flag"))
  else:
      print("Submission failed:", response.text)


# USAGE
#
# import pyjcgraderlib as ctfgrader
# grader = ctfgrader.grade("PATH_TO_FILE")
