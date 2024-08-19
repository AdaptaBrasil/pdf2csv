# pdf2csv
Convert table PDF docs to CSV files.

This script uses **tabula** Python lib that encapsulates [tabula-java](https://github.com/tabulapdf/tabula-java).

To run it is necessary to install tabula-py as described [here](https://pypi.org/project/tabula-py/). 
I tried to use ```pip install tabula-py``` in Windows as suggested in tabula-py link but it didn't work. Then I tried ```pip install tabula-py[jpype]``` and it worked nicely.

Then, to run the script you must run:

```
python pdf2csv --input_folder <path to pdf files>
```

It will process all pdf files that exist in <path to pdf files> generating a new file with the same name and csv extension.
