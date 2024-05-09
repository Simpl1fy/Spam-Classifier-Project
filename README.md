## SMS/Email Spam Classifier

This Project is my final year project based on Machine Learning/Deep Learning/AI and is used to classify spam messages received through SMS or Email.

### Technologies Used
- python
- pandas
- numpy
- flask
- scikit-learn
- nltk
- pickle

### Why this technologies were used :

- python - Readability, Extensive, Libraries and Frameworks.
- pandas - Great way to read csv(comma separated values) and manipulate dataframes
- numpy  - Used to perform array operations which are faster that python lists for operations
- flask - minimalistic python framework to host web application
- scikit-learn - python library for preprocessing and model training
- nltk - Python's language processing library for processing the data
- pickle - used to store the model, and preprocessor for the web application

## How to install and run Project

Clone the repository in your system
```
git clone https://github.com/Simpl1fy/Spam-Classifier-Project.git
```

Open the directory in VSCode terminal(cmd) or CommandPrompt(cmd) and
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate.bat
```

After enabling the Virtual Enviornment
```
pip install -r requirements.txt
```

This may take some time based on your network speed and speed of your system.
After installation you may run the server
```
python app.py
```