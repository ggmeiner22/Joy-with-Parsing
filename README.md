# Joy-with-Parsing

For this problem, we will use the command line to accept the grammar file, and get the input string
from standard input. So, if you named your program parser.py, then we could run your program
the following way.

~~~python3 parser.py grammar-expr < input-expr~~~

To grade your program, we use the diff utility to compare the output of your program against the
expected output.

~~~python3 parser.py grammar-expr < input-expr > out
diff out output-expr~~~
