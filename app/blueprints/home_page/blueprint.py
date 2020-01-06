from flask import Blueprint, render_template, request

home_page = Blueprint('home_page', __name__)
@home_page.route('/')
def display():
    return render_template('home_page.html') 
