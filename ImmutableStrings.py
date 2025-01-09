'''1. Once we declare the string we cannot modify it, if we try to modufy the
string it will create new string.

2.If new string does not have any reference variable then it will be removed.

3.Python internally uses String Interning.

4.String Internig is the process of checking String Intern pool before creating
any new object.

5.Whenever we want create new object, Python first will check string intyern pool, 
weather that object already exist or not.

6.When Object already exist in the string intern Records then address of
existing object will be reused.'''
# s1 = 'Kodnest'
# s1 = s1.upper()
# print(s1)

# s1 = 'S'
# print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print('ID of H',id(s1[0]))
print('ID of O',id(s1[-1]))

print('---------------------')

print("Id of W",id(s2[0]))
print("Id of O",id(s2[1]))

print('---------------------')

print("Id of l",id(s1[2]))
print("Id of l",id(s1[3]))
print("Id of l",id(s2[3]))