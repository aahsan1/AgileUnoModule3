# Module 3 Assignment
# Amir Ahsan

myfile = open ("question.txt",  "r+")

myquestion = myfile.read()

myresponse = input(myquestion)

myfile.write(myresponse)

myfile.close()
