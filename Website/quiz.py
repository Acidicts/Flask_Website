from flask import Flask, Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import db 

quiz = Blueprint("quiz", __name__)

global question_id
global sco
question_id = 0
sco = 0

questions = [
  'Hair Colour',
  'Crush',
  'has a crush on her',
  'Favourite Ginger',
  'Favorite short person',
  'Favorite Tall person'
]

answers = [
  'black',
  'osca',
  'oscar',
  'toby',
  'toby',
  'esme'
]

def increase_id(correct=False):
    global question_id
    global sco
    sco +=1
    question_id += 1

@quiz.route('/reset')
def reset():
  global question_id
  question_id=0
  return redirect('/quiz')

@quiz.route('/score', methods=['GET', 'POST'])
def score(total, sc):
  if request.method == 'POST':
    reset()
    return redirect(url_for("views.home"))
    
  return render_template("score.html", user=current_user, score=str(sc), total=str(total))

@quiz.route("/quiz", methods=["GET", "POST"])
def q():
    global sco
    global question_id
    if request.method == 'POST':
      answer = str(request.form.get("answer")).lower()
      
      if answer == answers[question_id]:
        flash("Correct!", category="success")
        if question_id <= len(questions)-2:
          increase_id(True)
          return render_template("quiz.html", user=current_user, questions=questions, id=question_id)
        else:
          return score(sc=sco, total=6)
      else:
        flash("Wrong", category="error")
        increase_id()
          

    return render_template("quiz.html", user=current_user, questions=questions, id=question_id)