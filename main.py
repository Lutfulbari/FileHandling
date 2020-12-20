                                                    # file
                                                    # open(),close()
                                                # active write mode ---->w


'''f = open("coad.txt")
print(f.read())
f.close()
print(f.read())'''

# same file ---> Old is delete and new create
'''f = open("coed.txt","w")
f.write("i am lutflbarimusa\n")
f.write("i am lutflbarimusa\n")
f.write("i am lutflbarimusa\n")
f.close()

'''
"""f = open("coedinggro.txt","x")
f.close()

f = open("coedinggro.txt","w")
f.write("i am a good web \n")
f.write("i am a good web \n")
f.write("i am a good web \n")
f.write("i am a good web \n")
f.close()
"""

"""f = open("coad.txt","r")
print(f.read(5))
print(f.read(3))
print(f.read(504))
print(f.read())
f.close()
"""
"""
f = open("coad.txt","r")
print(f.read())
for i in f:
    print(i,end="")
f.close()"""


"""f = open("coad.txt","r")
# print(f.read())
for i in f.read():
    print(i)
f.close()"""

#readline()

#f = open("coad.txt","r")
#print(f.read())
#for i in f:
"""print(f.readline(),end="")
print(f.readline(),end="")
"""
"""print(f.readlines())
print(f.readable())
f.close()"""

#                                    plus || text and binary
#                                 active mode --> "w" "a" "x" "r"
#+++---->>>> write and read

"""f = open("coad.txt","r+")
print(f.writable())
print(f.readable())
f.close()
"""
"""f = open("coad.txt","w+")
print(f.writable())
print(f.readable())
f.close()
"""
"""f = open("coad.txt","r")
print(f.read())
f.close()"""
                                                           #t -- >text
"""f = open("musa.docx","rb")
print(f.read())
f.close()
"""
"""f = open("coad.txt","rb")
print(f.read())
f.close()
"""
"""f = open("coad.txt","rb+")
print(f.writable())
print(f.readable())
f.close()"""
#     file
#          append
#     active append moad ---"a"

"""f = open("coad.txt","a")
f.write("\ncodinglhaguf")
f.close()"""
 ################## w , x ,a -----------file create

 #################       with statement
"""f = open("coad.txt","r")
print(f.read(10))
#print(f.read())
f.close()

f = open("coad.txt","r")
#print(f.read(10))
print(f.read())
f.close()

""
#with open("coad.txt","r") as f:
 #   print(f.read(10))
#with open("coad.txt","r") as f:
#    print(f.read())
"""

######                   file
    ##                   update --file records

"""
import re
with open("coad.txt","r") as f:
    f_list = f.readlines()
    print(f_list)
    for i, j in enumerate(f_list):
        if re.search(".*musa.*",j):
            f_list[i]= "this is a lutful\n"

with open("coad.txt","w") as f:
    f.writelines(f_list)

with open("coad.txt","r") as f:
    print(f.read())
    
    """

    #########         file delet

import re
a = 1
with open("coad.txt","r") as f:
    f_list = f.readlines()
    print(f_list)
    for i, j in enumerate(f_list):
        if re.search(".*goat.*",j):
            if i+1 == 3:
                f.list[i]=" "
                a=a+1
with open("coad.txt","w") as f:
    f.writelines(f_list)

with open("coad.txt","r") as f:
    print(f.read())
"""
f = open("coad.txt","w")
f.close()"""
 ###### create  a  new   file  in other dictonary
               #    write () and read   ()

"""import os
os.chdir("C:/Users/lutfu/OneDrive/Desktop")
f = open("coadinglaugh.txt","w")
f.write("ltful: hey i am musa\n")
f.write("ltful: hey i am musa\n")
f.write("ltful: hey i am musa\n")
f.write("ltful: hey i am musa\n")
f.close()"""


###########             file rename and delet file in others directory

import os
change directory
os.chdir("C:/Users/lutfu/OneDrive/Desktop")

rename(
 =----> old file ,new file
os.rename("hey.txt","google.txt")
 removed ()>>>>>>>>directory access

os.remove("C:/Users/lutfu/OneDrive/Desktop/google.txt")

 #                        file
 #                      rename and delete file in same directory


import os
 #getcwd() ->>>> ger current working directory
os.getcwd()
f = open("ho.txt","w")
f.close()
#os.rename("ho.txt","hii.txt")
os.remove("hii.txt")
