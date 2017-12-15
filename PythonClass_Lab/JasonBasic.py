import json

#Reading data from a JASON file
File = open("C:/Users/pankaj.kumar1/Desktop/PythonLib/Images/Test_JSON.txt","r")
FileContent = json.load(File)
File.close()

#Printing the data to the Json object
print (FileContent)

FileContent['Class'] = 25

print(FileContent)


#Copy the json data to the new file and store the directory

NewFile = open("C:/Users/pankaj.kumar1/Desktop/PythonLib/Images/Test_New_JSON.txt","w")
json.dump(FileContent,NewFile)
NewFile.close()