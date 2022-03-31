#Meme Generator Project
Meme Generator is a Python based tool for creating memes via various methods

##Overview
In this project we create memes by detecting the data inside different file types present like .pdf,.csv,.docx etc.
we parse this data via various tools which you can find in the code, then we are using the python library Pillow to work with the images and putting the text data of extracted imparser functions over image by creating random function generators.

##Installation
To build the project, you will first need to have Python installed. This project was built with python 3.10 but it should work with 3.8 and above.
You will also need pip and, optionally, virtualenv.
You will need to have the following dependencies installed on your Venv or System for this project work.

```
Flask==2.1.0
pandas==1.4.1
Pillow==9.0.1
python-docx==0.8.11
requests==2.27.1
```

you can get this files in the requirements.txt file and install via the command 
`pip install -r requirements.txt` for a venv or install each directly using pip.

##Usage
this project can be run via two major ways.

###1. Web APP.
To run meme-generator via the web we use the Python Framework flask, first we run the following lines to deploy the app

```
export FLASK_APP=app.py
flask run --host localhost --port 3000 --reload
```
the we open up localhost:3000

The Web app has two interfaces, you can click the random button to generate random default files, or you can click the creator button
to create your own meme by attaching a link, the meme quote and author

###2. CLI
The second way to run the app is through the cli, first you navigate to the meme-generator folder then you run the following line
python3 meme.py to create generate random default memes, you can generate your own memes by giving the --path, --body and --author options
that is `python3 meme.py --path <filepath> --body <meme content> --author <meme author>`
note that the body and the author parameters work together, you can't provide one without the other.

