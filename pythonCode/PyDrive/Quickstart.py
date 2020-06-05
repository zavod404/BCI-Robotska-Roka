from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.csv','parents': [{'id': '1eeA-y9DjF4zOuH4z5wkOB5nSehRtGneV'}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello, World,!') # Set content of the file from given string.
file1.Upload()

file_list = drive.ListFile({'q' : "'1eeA-y9DjF4zOuH4z5wkOB5nSehRtGneV' in parents and trashed=false" }).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

file5 = drive.CreateFile({'id': file1["id"]})

# Fetches all basic metadata fields, including file size, last modified etc.
file5.FetchMetadata()
print(file5)
"""
# Fetches all metadata available.
file5.FetchMetadata(fields='modifiedDate')
print(file1)
#
# Fetches the 'permissions' metadata field.
file5.FetchMetadata(fields='permissions')
# You can update a list of specific fields like this:
file5.FetchMetadata(fields='permissions,labels,mimeType') 
#
"""