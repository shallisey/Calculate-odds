# Calculate Odds

Simple overview of use/purpose.

<!-- ## Description

An in-depth paragraph about your project and overview of use. -->

## Getting Started

### Dependencies

* Python3 and pip must be installed on your machine.


### Installing

* First clone the repository form github
```
git clone https://github.com/shallisey/Calculate-odds.git
```

* Enter the new directory that was created
```
cd Calculate-odds
```

* Install dependencies
```
pip install -r requirements.txt
```

* Run calc_odds.py
```
python3 calc_odds.py
```


### Executing program

* Make request to http://localhost:58585/calculate_odds
* The body of the request must include 2 arrays. One named **prevYearApplication** and the other **prevYearSuccess**.

Example of request body:
```
Body: {
    "prevYearApplication": [52, 31, 6, 10, 66, 38, 38, 35, 7, 76, 20, 57, 48, 72, 69, 29, 0, 4, 0, 42, 22],
    "prevYearSuccess": [1, 0, 0, 0, 0, 0, 11, 12, 5, 16, 14, 11, 10, 9, 5, 6, 0, 3, 0, 1, 1]
}
```

* You will receive one array back **calculated**.

Example of response returned:
```
"calculated": [52, 51, 31, 6, 10, 66, 38, 27, 23, 2, 60, 6, 46, 38, 63, 64, 23, 0, 1, 0, 62]
```


