#Fancy Printing

Printing functions I never want to rewrite again

```python
$ ipython
Python 2.7.6 (default, Mar  4 2014, 11:53:55)
Type "copyright", "credits" or "license" for more information.

IPython 2.0.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from fprint import *

In [2]: print_info("Hey, some stuff just happened")
[14:05:21 14:24:43] INFO: Hey, some stuff just happened

In [3]: print_warning("Hmmm, I guess that's technically not allowed") # will print in YELLOW
[14:05:21 14:25:14] WARNING: Hmmm, I guess that's technically not allowed

In [4]: print_error("It's a trap!") # will print in RED
[14:05:21 14:25:19] ERROR: It's a trap!

In [5]: print_success("All done!") # will print in GREEN
[14:05:21 14:25:44] SUCCESS: All done!

In [6]: print_time()
[14:05:21 14:25:53]

In [7]: print_color("Check out my lightsaber","blue") # print colors!
Check out my lightsaber

In [8]: fancy_print("What a custom message",time=True,header="HEADER",color="blue") # underlying api
[14:05:21 14:27:30] HEADER: What a custom message

In [9]: repo_info = {'name': 'eric', 'repos': ['fprint', 'ANN.jl', 'Churn']}

In [10]: print_json(repo_info)
{
  "repos": [
    "fprint",
    "ANN.jl",
    "Churn"
  ],
  "name": "eric"
}

In [11]: print_json(repo_info,indent=8)
{
        "repos": [
                "fprint",
                "ANN.jl",
                "Churn"
        ],
        "name": "eric"
}

In [12]: print_info("this will be written to a file",file="tmp.log")

In [13]: print_info("this will be appended to the same file",file="tmp.log")

In [14]: ! cat tmp.log
[14:05:21 14:32:38] INFO: this will be written to a file
[14:05:21 14:32:44] INFO: this will be appened to the same file

In [15]:

```

