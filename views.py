from cgi import print_arguments
from wsgiref.util import request_uri
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website.models import Note
from controller import *
from routes.dcms import *

#from . import db 
import json

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == 'POST':
        #note = request.form.get('note')

        '''if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            #db.session.add(new_note)
            #db.session.commit()
            flash('Note added!', category='success')'''

    return render_template("home.html", user=current_user)

@views.route('/editpatients', methods=['GET', 'POST'])
def editpatients():
    return render_template("editpatients.html", user=current_user)

@views.route('/test', methods=['GET', 'POST'])
def test():
    return render_template("test.html", user=current_user)

@views.route('/addpatient', methods=['GET', 'POST'])
def addpatient():
    return render_template("addpatient.html", user=current_user)

@views.route('/appointment', methods=['GET', 'POST'])
def appointment():
    return render_template("appointment.html", user=current_user)

@views.route('/reception', methods=['GET', 'POST'])
def reception():
    return render_template("reception.html", user=current_user)

@views.route('/staff', methods=['GET', 'POST'])
def staff():
    return render_template("staff.html", user=current_user)
    
@views.route('/patients', methods=['GET', 'POST'])
def patients():
    return render_template("patients.html", user=current_user)

@views.route('/branches', methods=['GET', 'POST'])
def branches():
    return render_template("branches.html", user=current_user)

@views.route('/branch1', methods=['GET', 'POST'])
def branch1():
    return render_template("branch1.html", user=current_user)

@views.route('/branch2', methods=['GET', 'POST'])
def branch2():
    return render_template("branch2.html", user=current_user)

@views.route('/branch3', methods=['GET', 'POST'])
def branch3():
    return render_template("branch3.html", user=current_user)

@views.route('/branch4', methods=['GET', 'POST'])
def branch4():
    return render_template("branch4.html", user=current_user)

@views.route('/branch5', methods=['GET', 'POST'])
def branch5():
    return render_template("branch5.html", user=current_user)

@views.route('/branch6', methods=['GET', 'POST'])
def branch6():
    return render_template("branch6.html", user=current_user)

@views.route('/branch7', methods=['GET', 'POST'])
def branch7():
    return render_template("branch7.html", user=current_user)


@views.route('/branch8', methods=['GET', 'POST'])
def branch8():
    return render_template("branch8.html", user=current_user)

@views.route('/api/branches', methods=['GET'])
def branchapi():
    return render_template(user=current_user)