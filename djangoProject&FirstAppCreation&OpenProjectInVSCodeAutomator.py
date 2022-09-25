"""
This python module allows you to start your project and first app also open the project level folder in VS code in one go.
All you have To Do is Place This File in Your Favourite Folder Where you create All your Django Projects and just
'Enter your Project & App Name' when prompted to do so.
Please enter the name of your Project & App as per rule of Python Identifiers.
Please refer to 'https://docs.python.org/3/reference/lexical_analysis.html#identifiers' for official information related to python Identifiers.

Prerequisites :
    1. Python must be installed in your system.
    2. Django must be installed in your system.
    3. VS Code must be installed in your system.

"""






import os

#Creating Info String For Taking Input For Project Name Input
info_string_Project = """
You have to input Project name here. 
Please Note : Project name should be correct python Identifiers.
              For more information please visit 'https://docs.python.org/3/reference/lexical_analysis.html#identifiers'

Please Enter Project Name Here [ SHOULD BE CORRECT IDENTIFIERS ] : """


#Creating Info String For Taking Input For App Name 
info_string_App = """
You have to input App name here. 
Please Note : App name should be correct python Identifiers.
              For more information please visit 'https://docs.python.org/3/reference/lexical_analysis.html#identifiers'

Please Enter App Name Here [ SHOULD BE CORRECT IDENTIFIERS ] : """


#takin input for Project Name
project_name = input(info_string_Project)

#Handlin Exceptions of Names Which are Non Identifiers for Project Name
while True:
    if project_name.isidentifier():
        break
    else:
        print(" \n Entered 'PROJECT NAME' is not a correct Identifiers \n ")
        project_name = input(info_string_Project)

#takin input for App Name
app_name = input(info_string_App)

#Handlin Exceptions of Names Which are Non Identifiers for App Name
while True:
    if app_name.isidentifier():
        break
    else:
        print("Entered 'APP NAME' is not a correct Identifiers \n ")
        app_name = input(info_string_App)


#Creting Complete String for Complete Command Which Has To Be Executed
complete_command = 'cmd /c "django-admin startproject {0} & cd {0} & python manage.py startapp {1} & code ." '.format(project_name, app_name)

#Executing The Command
os.system(complete_command)

#Informing User That Process Has Been Completed
("Process Completed")

