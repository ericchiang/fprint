#Fancy Printing

Printing functions I never want to rewrite again

```python
>>> from fprint import *
>>> print_info("some stuff just happend")
[14:05:20 17:26:52] INFO: some stuff just happend
>>> # errors are printed in red (anyone know how to do that in markdown?)
>>> print_error("It's a trap!")
[14:05:20 17:27:42] ERROR: It's a trap!
>>> repo_info = {'name': 'eric', 'repos': ['fprint', 'ANN.jl', 'Churn']}
>>> print_json(repo_info)
{
  "repos": [
    "fprint",
    "ANN.jl",
    "Churn"
  ],
  "name": "eric"
}
>>> print_json(repo_info,indent=4)
{
    "repos": [
        "fprint",
        "ANN.jl",
        "Churn"
    ],
    "name": "eric"
}
>>> print_time()
[14:05:20 17:28:52]
```
