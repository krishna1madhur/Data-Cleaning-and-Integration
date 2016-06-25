
Assumptions:

1. All the professor's lastnames are unique and they do not contain any spelling mistake. 
   If they contain spelling mistakes, we must take corpus of the department of CS-UIC and check for the correct names of the professors.

2. 'class.txt' or any other input data file should contain the same format as given 'class.txt' file. Text file should not contain any additional lines.

Instructions:
1. Setup an environment where you can run python files. Please use python 3.4 for the execution.
1. Excute the clean.py by giving input of the text file 'python3 clean.py class.txt'. 
2. You will obtain 'cleaned.txt' 
3. Use 'query.py' to use the 'cleaned.txt' to obtain the desired result. The output is printed on the console.

NOTE: File 'wordlist.txt' is used for the spell checking. This is the additioanl training file that will be required by my algorithm to implement the spell checking.

Websites Referred:
https://docs.python.org/3/library/re.html
http://stackoverflow.com/	
https://pypi.python.org/pypi/autocorrect/0.2.0
For implementing the spell checker- http://norvig.com/spell-correct.html 
For providing data to the spell checker algorithm- https://github.com/dwyl/english-words

Books Referred:
For implementing Edit Distance method - Algorithm Design, by J. Kleinberg, and E. Tardos, Pearson/Addison-Wesley, 2006