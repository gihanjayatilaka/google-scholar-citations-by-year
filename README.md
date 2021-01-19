# Google Scholar Citations by Year


## Requirements
```
pip install scholarly
```


## Running

Minimal
```
python Main.py --name "Alan Turing" --year 2020
```

Custom
```
python Main.py --name "Alan Turing" --year 2020 --allDetails True --delaySec 4
```

**allDetails** prints the name of journal, authors and year.
**delaySec** is used to stop google from blocking you.

## Issues

Implement the exact harvard format to print publicaitons.