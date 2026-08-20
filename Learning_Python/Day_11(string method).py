a="Vinayak"
print(a.upper()) #produces new string which has all the letters of a in uppercase.
#means old string a is not changed. It remains the same. 
print(a.lower()) #produces new string which has all the letters of a in lowercase.
print(a.replace("Vinayak","Ankit")) #produces new string which has all the letters of a replaced with Ankit.
print(a.swapcase()) #produces new string which has all the letters of a in opposite case.

b="!!Hello !!!!! @@@"
print(b.strip("!,@")) #produces new string which has all the letters of b
#if i used rstrip() it would remove the characters from right side of the string and if i used lstrip() it would remove the characters from left side of the string.
print(b.split(" ")) #produces new list which has all the letters of b split by space.

blogHeading="introduction to Python"
print(blogHeading.capitalize()) #produces new string which has first letter of the string in uppercase and all other letters in lowercase.
print(blogHeading.title()) #produces new string which has first letter of each word in uppercase and all other letters in lowercase.
print(blogHeading.count("o")) #produces new integer which has the count of letter o in the string.

c="Welcome to Python"
print(c.center(50,"*")) #produces new string which has the string c in center and rest of the characters are filled with *.
print(c.startswith("Welcome")) #produces new boolean value which checks if the string c starts with Welcome or not.
print(c.endswith("Python")) #produces new boolean value which checks if the string c ends with Python or not. 
print(c.endswith("Python",0,10)) #produces new boolean value which checks if the string c ends with Python or not in the range of index 0 to 9.
print(c.find("Python")) #produces new integer which has the index of first occurrence of Python in the string c. If not found it returns -1.
print(c.index("Python")) #produces new integer which has the index of first occurrence of Python in the string c. If not found it raises ValueError.
print(c.isalnum()) #produces new boolean value which checks if the string c is alphanumeric or not. It returns True if all characters are alphanumeric and there is at least one character, otherwise it returns False.

d="Welcometo9Python\n"
print(d.isalnum()) #produces new boolean value which checks if the string d is alphanumeric or not. It returns True if all characters are alphanumeric and there is at least one character, otherwise it returns False.
print(d.isalpha()) #produces new boolean value which checks if the string d is alphabetic or not. It returns True if all characters are alphabetic and there is at least one character, otherwise it returns False.
print(d.isdigit()) #produces new boolean value which checks if the string d is digit or not. It returns True if all characters are digits and there is at least one character, otherwise it returns False.
print(d.islower()) #produces new boolean value which checks if the string d is in lowercase or not. It returns True if all characters are in lowercase and there is at least one character, otherwise it returns False.
print(d.isupper()) #produces new boolean value which checks if the string d is in uppercase or not. It returns True if all characters are in uppercase and there is at least one character, otherwise it returns False.
print(d.isspace()) #produces new boolean value which checks if the string d is space or not. It returns True if all characters are space and there is at least one character, otherwise it returns False.
print(d.istitle()) #produces new boolean value which checks if the string d is title or not. It returns True if all first letter of all words in the string are capitalizedand there is at least one character, otherwise it returns False.
print(d.isprintable()) #produces new boolean value which checks if the string d is printable or not. It returns True if all characters in the string are printable and there is at least one character, otherwise it returns False.
#false because \n is not printable.
