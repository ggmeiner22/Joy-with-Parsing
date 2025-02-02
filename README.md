# Joy-with-Parsing

To run, use the command line to accept the grammar file, and get the input string
from standard input. So, if you named your program parser.py, then we could run your program
the following way.
~~~
python3 parser.py grammar-expr < input-expr.in1
~~~
To evaluate the program, we use the diff utility to compare the output of thr program against the
expected output.
~~~
python3 parser.py grammar-expr < input-expr.in1 > out
diff out output-expr
~~~
