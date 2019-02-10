# pythonCLIPiping
Python CLI pipeline example. Produce prime numbers in the range specified.

## Pipeline
[Windows pipeline](https://docs.microsoft.com/en-us/powershell/scripting/learn/understanding-the-powershell-pipeline?view=powershell-6)  
[Unix pipeline](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29)

## Usecase
This is an example of how to handle piping inside Windows or Linux based OS's.
Program reads-in parameters from 2 possible sources: command line arguments or standart input(stdin).  
``python primeList.py 1 100`` will output all the primary numbers between numbers 1 and 100.  
``type data.txt | python primeList.py`` will output all the primary number between first 2 integers of the file ``data.txt``.  

## Example
Windows Command below will take data from data.txt and pipe it to the python running primeList.py, where first 2 integers from the file are used as parameters for range of primary numbers.   
``type data.txt | python primeList.py -s -f results2.txt``  
With ``-s`` argument the process will eun silently, without any notifications.  
With ``-f`` argument the output will be saved into file with the filename equal to the next argument after ``-f``.  
  
![example](https://github.com/MartinRep/pythonCLIPiping/blob/master/Media/pythonCLIpiping_exam.gif)
