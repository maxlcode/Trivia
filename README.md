# Full Stack API Final Project

## Full Stack Trivia

### Project Description
This project is being developed within the Udacity Fullstack Developer programm to create a full stack web app to play the trivia game
The main function of the project is to play the Trivia game - that means to challenge your knowledge!
Therefore it is possible to
  * Show all existing questions (10 per page) with according category, difficulty and answer
  * Show existing questions filtered by category
  * Search by questions based on a search term
  * Delete existing questions and create new questions
  * Play the game

### Code Style
The procject is developed using PEP8 Code Style

## Getting Started

### Frontend

The front end is a developed as react app.

##Frontend Dependecies
In order to get it started, please make sure you have the latest verison of NODE.JS installed (https://nodejs.com/en/download)

Please open the [`./frontend/`](./frontend/) directory
The execute following commands
```bash
npm install
npm start
```

As default the app will serve on localhost port 3000.
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

For more information please refer to [`./frontend/`](./frontend/README.md)

### Backend

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

Please also refere to [`./backend/`](./backend/README.md) for all backend set up

### Backend Testing

To run the tests, run
```
dropdb trivia
createdb trivia
psql trivia < trivia.psql
python test_flaskr.py
```

## API reference

### Getting Started
* Base URL: 'http://127.0.0.1:5000/'
* Authentification: This version does not need authentification

### Error Handling
Errors are returned as JSON objects in the following format:
```json
{
  "success" : False,
  "error" : 400,
  "message" : "bad request"
}
```

The API will return following errors
* 400: bad request
* 404: ressource not found
* 422: unprocessable

#### GET /categories
General:
* This enpoint gives back all available categories + the total numer of categories

Sample:
* Request: 
```curl http://127.0.0.1:5000/categories```
* Response:
```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

#### GET /questions
General:
* This endpoint gets back all questions that are currently existing
* You are getting paginated results of 10 questions per page
* If you want to have a specific page - please specify in URL - e.g. '?page=2'
* You are also getting total number of questions and all categories

Sample
* Request: 
```curl http://127.0.0.1:5000/questions```
* Response:
```json 
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```

#### POST /questions
General: 
* This Endpoint can be used to either search for a questions that contain a specific searchterm or it can be used to create new questions in the database.
* For a search, a searchTerm must be specified in the request body
* For creating a new question, you must specify the question, answer, category and difficulty 

Sample Search:
* Request
``` curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"searchTerm":"title"}' \
  http://127.0.0.1:5000/questions 
```
  
* Response:
```json
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```
Sample New question: 
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"question":"test question", "answer":"test answer","difficulty":"1","category":"3"}' \
  http://127.0.0.1:5000/questions 
* Request
``` ```
* Response:
```json
{
  "created": 26,
  "success": true
}

```

#### DELETE /questions/{question-id}
General: 
* Using this endpoint you can delete existing questions
* An error will be responded if question-id is not existing

Sample:
* Request
``` 
curl --header "Content-Type: application/json" \
--request DELETE \
http://127.0.0.1:5000/questions/26
```
* Response:
```json
{
  "deleted": 26,
  "success": true
}
```
#### GET /categories/{category-id}/questions
General: 
* With this endpoint you can get all questions of a specific category
* Repsponse will contain all categories, selected categories as well as the questions and total questions
* Pagignation will be same as using /questions endpoint 

Sample:
* Request
```curl http://127.0.0.1:5000/categories/1/questions```
* Response:
```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Test Answer",
      "category": 1,
      "difficulty": 3,
      "id": 24,
      "question": "Test question"
    },
    {
      "answer": "Test Answer",
      "category": 1,
      "difficulty": 3,
      "id": 25,
      "question": "Test question"
    }
  ],
  "success": true,
  "total_questions": 5
}

``` 
#### POST /quizzes
General:
* This endpoint is used to get always one random question.
* By sending a quiz category, you can define the the questions is of this specific category
* If you want to have all catgories, please send category.ID = 0
* In order to not get same questions you can specify the questions ids that already have been used in the previous_questions array 

Sample:
* Request
``` curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"previous_questions":[],"quiz_category":{"type":"Science","id":"1"}}' \
  http://127.0.0.1:5000/quizzes 
```
* Response:
```json
{
  "question": {
    "answer": "Test Answer",
    "category": 1,
    "difficulty": 3,
    "id": 24,
    "question": "Test question"
  },
  "success": true
}

```

## Deployment

No specifics

## Authors

Udacity, Max B.

## Acknowledgements

None
