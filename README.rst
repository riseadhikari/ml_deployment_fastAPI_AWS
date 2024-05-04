Machine Learning Model Deployment with FastAPI & AWS
======================================================

Hi There: 

      In this project, I will be deploying a Machine Learning model using FastAPI and AWS. The model is a 	simple Neural Network, that predicts an image's class. I used FashionMNIST dataset and Pytorch to train the model. Anyway the model is not the main focus here. The main focus here is to learn and understand the flow of deploying a machine learning model in production, utilizing standard tools. This info is just for the context. Le't get started! :)


What's Covered
--------------

1. Creating a RestAPI for our trained model using FastAPI
2. Testing the API by writing tests
3. Initializing, Committing, and Pushing the code to GitHub

To be Covered Soon
------------------

1. Allow Image as input. [ For now, I have used string of comma separated pixel values as input to keep things simple. ]
2. Set-up Linting and Formatting
3. Set up Continuous Integration
4. Deploy the API using AWS ECR and AWS AppRunner
5. Set-up Continuous Deployment
6. Make a YouTube Video, explaining the whole process.


How To Run The Code:
--------------------

Note: I am using Python 3.9.6 [ fyi ]. It should work with any Python >= 3.9 or even less. Try it out.

1. pip install -r requirements.txt
2. pytest test_app.py
3. uvicorn app:app --reload
4. Paste The Url into the browser: 127.0.0.1:8000 [ yours maybe different if you launched differently ].
5. FastAPI comes with Swagger Docs and I encourage you to use it to make your life easier: 127.0.0.1:8000/docs


I will let you figure out the API endpoints and how to use them. If you have any questions, feel free to ask:


Linkedin: www.linkedin.com/in/rise-adhikari

Email: adhikari.rize@gmail.com

Happy Coding! :)