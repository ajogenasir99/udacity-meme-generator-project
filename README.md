# Meme Generator Project
Meme Generator is a Python based tool for creating memes via various methods

## Overview
In this project we create memes by detecting the data inside different file types present like .pdf,.csv,.docx etc.
we parse this data via various tools which you can find in the code, then we are using the python library Pillow to work with the images and putting the text data of extracted imparser functions over image by creating random function generators.

## Installation
To build the project, you will first need to have Python installed. This project was built with python 3.10 but it should work with 3.8 and above.
You will also need pip and, optionally, virtualenv.
You will need to have the following dependencies installed on your Venv or System for this project work.

```
Flask==2.1.0
pandas==1.4.1
Pillow==9.0.1
python-docx==0.8.11
requests==2.27.1
MarkupSafe==2.1.1
Jinja2==3.1.1
click==8.1.0
itsdangerous==2.1.2
```

you can get this files in the requirements.txt file and install via the command 
`pip install -r requirements.txt` for a venv or install each directly using pip.
if you going to use a virtual env(which is prefarable)
use the following steps to set up the venv

1. Install virtual env
`pip install virtualenv`

2. Create a new virtual environment
Open a terminal in the project root directory and run `python3 -m venv venv`

3. Activate your virtual environment
Run this command to activate `.\venv\bin\activate\`

4 upgrade your virtual environments pip
run `pip install --upgrade pip`

5. Install the project dependencies
Run `pip install -r requirements.txt`


## Usage
This project can be run in two ways.

### 1. Web APP.
To run meme-generator via the web we use the Python Framework flask, first we run the following lines (from the root of the project) to deploy the app

```
python3 app.py
```
the we open up localhost:3000

#### NOTE
you can also access the app directly using the link provided in the about
section of this repo instead of downloading it locally.

The Web app has two interfaces, you can click the random button to generate random default files, or you can click the creator button
to create your own meme by attaching a link, the meme quote and author

### 2. CLI
The second way to run the app is through the cli, first you navigate to the meme-generator folder then you run the following line
python3 meme.py to create generate random default memes, you can generate your own memes by giving the --path, --body and --author options
that is `python3 meme.py --path <filepath> --body <meme content> --author <meme author>`
note that the body and the author parameters work together, you can't provide one without the other.

