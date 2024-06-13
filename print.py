print("hello world")

# creating a shape
print(" / |")
print("/__|")

###VARIABLE AND DATA TYPES####

# 1) variable acts as containers to store the data values and modify data values:

#Example1:

Character_name ="salaam"   # when creating variable name and it has 2 words, sepeare it by '_'
Character_age = "35"
print("There is once a " + Character_name+  " aged 27,")
print("And a sai aged 28,")
print("and they are good friends.")

#Example2:

print("There is once a " + Character_name+  " aged "+ Character_age + ",")
print("And a sai aged 28,")

# 2) With variables we can also modify data values:

#Example 3:

Character_name ="Abdul"   # when creating variable name and it has 2 words, sepeare it by '_'
Character_age = "20"
print("There is once a " + Character_name+  " aged "  +Character_age+ ",")
print("And a " + Character_name+ " aged 28,")
print("and they are good friends.")


#We can the variable value in the middle, for example:

print("There is once a " + Character_name+  " aged "  +Character_age+ ",")
Character_name ="Akula"  #So for the Above line output comes as Abdul, but from the below line output comes as for Akula
print("And a " + Character_name+ " aged 28,")
print("and they are good friends.")

#####DATA TYPES####
#Basically we have used String or str(plain text) data like Abdul, Akula in the above example, and numbers. While assigning this  Variable to a strings we need to use "", for data like numbers or float (Ex: 2.6, 5.70) we dont need to use " " while storing value in a variable.
#There are mainly Four Data types:
#String like Abdul,Abhi,Sumanth
#Numbers like 20,10,30
#Floats like 20.14,3.12
#Boolean Like True or False

# a) Working with Strings:

print("Abdul Linkedin")
# \n adds new line (Try for below command)
print("Abdul\nLinkedin")
# OR if you want to add " symbol inbetween, you can mention after blackshash \, so it tells what ever i'm giving after \ add it.
print("Abdul\"Linkedin")