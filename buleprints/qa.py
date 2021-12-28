from flask import (
    Blueprint,
    render_template,
    request,
    g,
    redirect,
    url_for,
    flash
)
from decorators import login_required
from .forms import QuestionForm, AnswerForm
from models import Question, Answer
from exts import db
from sqlalchemy import or_

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    questions = Question.query.order_by(db.text('-create_time')).all()
    return render_template('index.html', questions=questions)


@bp.route('/question/public', methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = Question(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            flash('标题或内容格式错误!')
            return redirect(url_for('qa.public_question'))


@bp.route('/question/<int:question_id>')
def question_detail(question_id):
    question = Question.query.get(question_id)
    return render_template('detail.html', question=question)


@bp.route('/answer/<int:question_id>', methods=['POST'])
@login_required
def answer(question_id):
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        answer_model = Answer(content=content, author=g.user, question_id=question_id)
        db.session.add(answer_model)
        db.session.commit()
        return redirect(url_for('qa.question_detail', question_id=question_id))
    else:
        flash('表单验证失败!')
        return redirect(url_for('qa.question_detail', question_id=question_id))


@bp.route('/search')
def search():
    q = request.args.get('q')
    # filter_by: 直接使用字段名称
    # filter: 使用模型.字段名称
    questions = Question.query.filter(or_(Question.title.contains(q), Question.content.contains(q))).order_by(
        db.text('-create_time'))
    return render_template('index.html', questions=questions)
