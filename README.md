# Create-Oracle-Cloud-Instance
This is a python script which can be used to automatically register oracle cloud server. Download  the .py and the .bat files. You need to manually edit your username, email, and password for oracle in the .py file, and edit the path to python and path to the script in .bat. The default option of shape is the Ampere VM.Standard.A1.flex-the best config you can get with always-free.

## The Python Script
It needs your username, email, and password to log into your oracle cloud account, and you need to pin the *instance* to your home page, and it will download the SSH key and try to create an instance. If it fails, it will write the result *No resource available*  to a .txt file.  
## The .BAT File
You can use this file to run this python script and add it to your Windows task scheduler so that it automatically tries to create instances. You will have to edit the .bat file so that the command line can find the python interpreter and the python script above. The content should be
`"path_to_python" "path_to_script"`
