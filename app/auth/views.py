from flask import render_template,flash,url_for,abort,request
from ..request import get_quotes
from .forms import Bl