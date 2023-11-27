import os

# File name to be removed
file_name = "Article.json"

# Checking if the file exists in the current directory
if os.path.exists(file_name):
    # Removing the file
    os.remove(file_name)
    message = f"File '{file_name}' has been successfully removed."
else:
    message = f"File '{file_name}' does not exist in the current directory."

message
