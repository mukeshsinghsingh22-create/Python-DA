# from newmodule import greeting , person1
# import newmodule

# # Example usage of the newmodule functions
# a = newmodule.greeting("Alice")
# print(a)
# b = newmodule.person1["age"]
# print(b)
# print(greeting("Alice"))
# print(person1["age"])
# print(person1["name"])
# print(person1["country"])

import platform
print(platform.system())

import datetime
x= datetime.datetime.now()
# print(x)
# print("Current date and time: ", x.strftime("%Y-%m-%d %H:%M:%S"))
# print("Current year: ", x.year)
# print("Current month: ", x.month)
# y=datetime.datetime(2020, 5, 17)
# print("Specific date: ", y.strftime("%Y-%m-%d"))
# print(y.strftime("%Y-%m-%d %H:%M:%S"))    
print(x.strftime("%a")) #Weekday as a short name
print(x.strftime("%A")) #Weekday as locale’s full name.
print(x.strftime("%w")) #Weekday as a decimal number, where 0 is Sunday and 6 is Saturday
print(x.strftime("%d")) #Day of the month as a zero-padded decimal number
print(x.strftime("%b"))  #Month name, short version
print(x.strftime("%B"))  #Month name, full version
print(x.strftime("%m"))  #Month as a zero-padded decimal number 
print(x.strftime("%y"))  #Year, short version, without century
print(x.strftime("%Y"))  #Year, full version
print(x.strftime("%h"))  #Hour (12-hour clock) as a zero-padded decimal number
print(x.strftime("%H"))  #Hour (24-hour clock) as a zero-padded decimal number
print(x.strftime("%I"))  #Hour (12-hour clock) as a zero-padded decimal number
print(x.strftime("%p"))  #AM or PM  
print(x.strftime("%x"))  #Locale’s appropriate date representation
print(x.strftime("%X"))  #Locale’s appropriate time representation
print(x.strftime("%c")) #Locale’s appropriate date and time representation
print(x.strftime("%C")) #Century as a decimal number (the year divided by 100 and truncated to an integer)
print(x.strftime("%U")) #Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number
print(x.strftime("%W")) #Week number of the year (Monday as the first day of the week) as a decimal number
print(x.strftime("%j")) #Day of the year as a zero-padded decimal number
print(x.strftime("%f")) #Microsecond as a decimal number, zero-padded on the left
print(x.strftime("%z")) #UTC offset in the form +HHMM or -HHMM
print(x.strftime("%Z")) #Time zone name