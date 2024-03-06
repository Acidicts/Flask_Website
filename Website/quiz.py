from flask import Flask, Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user

quiz = Blueprint("quiz", __name__)

global question_id
question_id = 0

questions = [
  'Hair Colour',
  'Crush',
  'Favourite Ginger'
]

answers = [
  'black',
  'oscar',
  'toby'
]

def increase_id():
    global question_id
    question_id += 1

@quiz.route('/score', methods=['GET', 'POST'])
def score():
  if request.method == 'POST':
    redirect('/')
    
  return render_template("score.html", user=current_user, score="3")

@quiz.route("/quiz", methods=["GET", "POST"])
def q():
    global question_id
    if request.method == 'POST':
      answer = str(request.form.get("answer")).lower()
      
      if answer == answers[question_id]:
        flash("Correct!", category="success")
        if question_id <= 1:
          increase_id()
          return render_template("quiz.html", user=current_user, questions=questions, id=question_id)
        else:
          return redirect(url_for("quiz.score", score=3))
      else:
        flash("Wrong", category="error")
          

    return render_template("quiz.html", user=current_user, questions=questions, id=question_id)