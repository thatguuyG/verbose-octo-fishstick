## CSV command line application



## Set up

Clone and cd into the project:

```bash
git clone https://github.com/thatguuyG/verbose-octo-fishstick && cd verbose-octo-fishstick

```

### 1. Create a Virtual Environment:

```bash
python -m venv myenv
```

### 2. Activate the Virtual Environment

#### For Windows PC's
```bash
myenv\Scripts\activate
```

#### For Mac/Linux
```bash
source myenv/bin/activate
```

### 3. Install packages

```bash
pip install -r requirements.txt
```


## Run the project

To run the project, simply run the main.py file

```bash
python main.py -s source.csv -t target.csv -o reconciliation_report.csv
```

Output here will be logged to a new file called reconciliation_report.csv


