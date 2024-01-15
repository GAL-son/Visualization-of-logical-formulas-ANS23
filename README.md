# Visualization-of-logical-formulas-ANS23

<p>Visualization of logical formulas - Project for Software Engeneering subject</p>

## Usage

> **_NOTE:_**  ***For demonstration purposes***

### Requirements

* Python 3.9 or higher
* pip 23.2 or higher
* Node.js v18.15 or higher
* Angular CLI 17 or higher
* npm 9.5 or higher

### Installing packages

For **Python** part go to the project root directory (*referred as* `/`).
Next use pip and `requirements.txt` file to install required Python libraries

```
py -m pip install -r requirements.txt
```

or with Anaconda CLI:

```
pip install -r requirements.txt
```

Next you can install required **node modules**. Head over to the `./frontend` directory.
Type in terminall:

```
node install --force
```

### Runing appliaction

To run aplication you must first run the Angular server.
In directory `./frontend` type:

```
ng serve
```

and wait for server to start running. 
Once this is done server should display adress where you can access application.
In most cases this should be: `http://localhost:4200/`

### Parsing formulas

<p>Once the Angular application is running you can start visualizing graph. 
Because this project is only for demonstration purposes the process isn't seamless.</p>

First you have to parse your formula. To do this copy your ***DIMCAS CNF*** formatted file 
to the `./asset` directory and name it `formula.cnf`

Next you have to run `main.py` file. 

It will create two files `REDUCTION_GRAPH{N}.json` and `WEIGHTED_GRAPH{N}.json` into the `./output` directory, where `N` in the file name is representing number of generated file.

To visualize generated graphs you have input them into Angular app.

Put them into their respective inputs:
* `WEIGHTED_GRAPH{N}.json` -> *Weighted Resolution Graph* input 
* `REDUCTION_GRAPH{N}.json` -> *Resolution Graph With Reduction* input

And then pres button labeled *GENERATE*

Respective graphs should appear below form.

> **_NOTE:_**  To change formula you need to regenerate graph using ***Python***. The new output file will have higher number.

