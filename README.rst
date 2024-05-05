Machine Learning Model Deployment with FastAPI & AWS
======================================================

Hi There: 

      In this project, I will be deploying a Machine Learning model using FastAPI, Docker and AWS. The model is a simple Neural Network, that predicts an image's class. I used FashionMNIST dataset and Pytorch to train the model. Anyway the model is not the main focus here. The main focus here is to learn and understand the flow of deploying a machine learning model in production, utilizing standard tools. This info is just for the context. Le't get started! :)


What's Covered
--------------

1. Creating a RestAPI for our trained model using FastAPI
2. Testing the API by writing tests
3. Initializing, Committing, and Pushing the code to GitHub
4. Set-up Linting and Formatting.
5. Dockerize the project.

To be Covered Soon
------------------

1. Allow Image as input. [ For now, I have used string of comma separated pixel values as input to keep things simple. ]
2. Set up Continuous Integration.
3. Deploy the API using AWS ECR and AWS AppRunner.
4. Set-up Continuous Deployment.
5. Make a YouTube Video, explaining the whole process.


How To Run The Code:
--------------------

Note: I am using Python 3.9.6 [ fyi ]. It should work with any Python >= 3.9 or even less. Try it out.

Without Docker:
---------------

1. pip install -r requirements.txt
2. pre-commit install [ optional but recommended ]
3. pytest test_app.py
4. uvicorn app:app --reload
5. Paste The Url into the browser: 127.0.0.1:8000 [ yours maybe different if you launched differently ].
6. FastAPI comes with Swagger Docs and I encourage you to use it to make your life easier: 127.0.0.1:8000/docs

With Docker:
------------

1. docker-compose -f local.yml build
2. docker-compose -f local.yml up

Note: You may use the Makefile to run tests.

Suggested Method:
-----------------

1. Clone the repo.
2. Create a virtual environment. [ python -m venv venv ]
3. Activate the virtual environment. [ source venv/bin/activate if linux/Mac or venv\Scripts\activate if windows ]
4. Install the requirements. [ pip install -r requirements.txt ]
5. Set-up pre-commit. [ pre-commit install ]
6. Run the tests. [ pytest test_app.py ]
7. Run the app. [ uvicorn app:app --reload ]

8. Only Test With Docker before deploying. [ Saves time. Just a suggestion. ]

I will let you figure out the API endpoints and how to use them. If you have any questions, feel free to ask:


Linkedin: www.linkedin.com/in/rise-adhikari

Email: adhikari.rize@gmail.com

Happy Coding! :)