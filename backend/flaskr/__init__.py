import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
import random
import sys

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_questions = questions[start:end]
  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  app.config.from_object('config')
  setup_db(app)
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  '''
  @TODO: Set up CORS. Allow '*' for origins. 
  Delete the sample route after completing the TODOs
  '''
  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add(
      'Access-Control-Allow-Headers', 
      'Content-Type,Authorization,true'
      )
    response.headers.add(
      'Access-Control-Allow-Methods', 
      'GET,PUT,POST,DELETE,OPTIONS'
      )
    return response

   # REST ENDPOINT GET - All categories
  @app.route('/categories', methods=['GET'])
  def retrieve_categories():
    categories =  Category.query.all()
    dict_categories = {
      category.id: category.type for category in categories
      }

    return jsonify({
      'success': True,
      'categories': dict_categories,
      'total_categories': len(categories)
    })

  # REST ENDPOINT GET - Questions with pagination 
  @app.route('/questions', methods=['GET'])
  def retrieve_questions():
    questions = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, questions)
    current_category  = request.args.get('categories', None, type=int)

    # Get categories
    categories =  Category.query.all()

    # Format the categories to a dict. A array will not be taken from the FE
    dict_categories = {
      category.id: category.type for category in categories
      }

    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions':len(questions),
      'categories': dict_categories,
      'current_category' : None
    })

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_questions(question_id):
    # look if id is exiting
    try:
      question = Question.query.filter(
                    Question.id == question_id).one_or_none()
      #if not existing - 404 error
      if question is None:
        abort(404)
      #delete from db
      question.delete()

      return jsonify({
        'success': True,
        'deleted': question_id,
      })

    except Exception as e:
      print(e)
      abort(422)

  # REST ENDPOINT: POST New question or search for question
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()
    search_term = body.get('searchTerm', None)
    
    # if search_term is contained in request, then it is a search
    if search_term is not None:
      return search_questions(request, body)

    # else a new question is created if all required data is conainted
    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_category = body.get('category', None)
    new_diffculty = body.get('difficulty', None)

    try:
      question = Question(question=new_question, 
                            answer=new_answer, 
                            category=new_category,
                            difficulty=new_diffculty
                            )
      question.insert()

      return jsonify({
        'success': True,
        'created': question.id,
      })

    except Exception as e:
      print(e)
      abort(422)
  
  # Search for questions
  def search_questions(request, body):

    search_term = body.get('searchTerm', None)
    questions = Question.query.filter(
      Question.question.ilike('%'+search_term+'%')
      ).all()
    current_questions = paginate_questions(request, questions)

    # Get categories
    categories =  Category.query.all()

    # Format the categories to a dict. A array will not be taken from the FE
    dict_categories = {
      category.id: category.type for category in categories
      }

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions':len(questions),
      'categories': dict_categories,
    })

  # REST ENDPOINT: GET Questions for a specific category
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def retrieve_questions_by_category(category_id):
    selection = Question.query.filter(
      Question.category==category_id).order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)

    # Get categories
    categories =  Category.query.all()

    # Format the categories to a dict. A array will not be taken from the FE
    dict_categories = {
      category.id: category.type for category in categories
      }

    if len(selection) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions':len(selection),
      'categories': dict_categories,
      'current_category' : category_id
    })

  @app.route('/quizzes', methods=['POST'])
  def play_game():
    #get request data
    body = request.get_json()
    quiz_category = body.get('quiz_category')
    previous_questions = body.get('previous_questions')

    # 404 when category or previous question message is missing
    if quiz_category is None or previous_questions is None:
      return abort(422)

    # Select categories for all categories
    if int(quiz_category['id']) == 0:
      question = Question.query.filter(
          Question.id.notin_(previous_questions)
          ).order_by(func.random()).first()
    # Filter for Category  
    else:
      question = Question.query.filter(
        Question.category==int(quiz_category['id'])).filter(
          Question.id.notin_(previous_questions)
          ).order_by(func.random()).first()
    # if no questions is left return "None" as question
    if question is None:
      return jsonify({
        'success': True,
        'question': None
        })
    # if a question is left, send it
    else: 
      return jsonify({
        'success': True,
        'question': question.format()
        })


  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400
  
  return app

    