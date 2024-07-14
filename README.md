# HarvestEye

## Setting up your virtual environment
I'm using Python 3.11.7, [download here](https://www.python.org/downloads/release/python-3117/). 3.11.8 should work as well. 3.12 had issues with some packages I've downloaded in the past, so I avoided it.

1. **Clone the repo**  
   a) Go to a local path on your machine, and enter command window (ctrl+r, and type "cmd", and navigate to your desired location for the folder)  
   b) `git clone https://github.com/JaySachar/HarvestEye.git`

2. **Create the virtual Environment**  
   a) Navigate to the repository you cloned in the command window (ie `cd C:/Users/JaySachar/Documents/Github/HarvestEye`)  
   b) Once in the cloned repo, enter `python -m venv venv` into the command window  
   c) Activate the virtual environment: `cd venv\Scripts`, and on a new line, `activate`  
   d) Navigate to the directory with requirements.txt (`cd ..` takes you up a directory)  
   e) Once in HarvestEye directory, run `pip install -r requirements.txt`
