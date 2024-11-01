import re

# The string to extract from
text = 'name="Description" content="Well organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, Python, PHP, Bootstrap, Java, XML and more."'

# Use regex to capture the content inside content="..."
content = re.search(r'content="([^"]+)"', text).group(1) # type: ignore

# Check if there is a match and print the content
if content:
    print("Content:",content ) 
else:
    print("No content found.")
