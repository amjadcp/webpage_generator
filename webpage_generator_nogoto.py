#! /usr/bin/env python

# from goto import goto, label
import subprocess

def option_1():
   try:
      title = input("What will be title of your webpage? => ")
      name = input("What is your name? => ")
      #label .start_3
      age = int(input("Your age? "))
      no = int(input("Your phone number "))
      #label .start_2
      sex = input("Your gender?")
      if sex=="male" or sex=="female" or sex=="MALE" or sex=="FEMALE" or sex=="m" or sex=="f" or sex=="M" or sex=="F":
        add = input("Address  ")
        file.write("""<html>
                      <head>
                      <title>""" + title +"""</title>
                       </head>
                        <body align="center">
                        Name : """ + name + """
                        Age :""" + str(age) + """
                        Sex :""" + sex + """
                        Phone Number :""" + str(no) + """
                        Address : """ + add + """
                        </body>
                        </html>"""
                         )
        file.close()
        print("""Your sample page created please check generate.html""")
      else:
        print("oops not applicable try again !")
       # goto .start_2
   except ValueError:
      print("oops not applicable try again !")
      #goto .start_3


def option_2():
    title = input("What will be title of your webpage? => ")
    print("""Hey, your sample form created please check generate.html""")
    file.write("""<html>
                  <head>
                  <title>""" + title + """</title>
                  </head>
                  <body>
    <form>
    Name &nbsp;&nbsp; : &nbsp;&nbsp; <input type="text"><br>
    Age &nbsp;&nbsp; : &nbsp;&nbsp; <input type="text"><br>
    Sex &nbsp;&nbsp; : &nbsp;&nbsp; <input type="radio" name="sex"> &nbsp; M &nbsp; <input type="radio" name="sex"> F<br>
    Phone Number &nbsp;&nbsp; : &nbsp;&nbsp; <input type="text"><br>
    Address &nbsp;&nbsp; : &nbsp;&nbsp; <textarea>address</textarea> 
    </form>
    </body>
    </html>""")
    file.close()

#label .start_6
print("""## This is a small application to create a sample webpage based on ur answers

     +++++++++++++++++++++++++++++++++++++++++++++++++
                        MENU
     +++++++++++++++++++++++++++++++++++++++++++++++++
               1 : To display your personal data
               2 : To create a form to add your personal data
               """)
#from goto import goto,label
#label .start_1
option = int(input("Enter your option => "))
file = open("generate.html", "w")
if option == 1:
    option_1()
elif option == 2:
    option_2()
else:
    print("Wrong option try again")
    #goto .start_1

#label .start_4
switch = input("Do you want to change this html code manualy? (y/n)")
if switch=="y" or switch=="Y":
            subprocess.call("nano generate.html", shell=True)
elif switch=="n" or switch=="N":
     print("Thank you!")
else:
    print("oops not applicable please try!")
    #goto .start_4

#label .start_5
switch = input("Do you want to run this application again? !!! your data will be lose !!! (y/n)")
if switch == "y" or switch == "Y":
   """#goto .start_6"""
elif switch == "n" or switch == "N":
    print("Thank you!")
else:
    print("oops not applicable please try!")
    # goto .start_5

print("""

###############################################################################################################################
                
                Hi user your webpage will be store in generate.html you can rename that file or copy it
                
################################################################################################################################""")