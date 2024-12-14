from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseServerError
from .models import Secret
from django.db.models import Q
import sqlite3
import json
import sys
import logging

logger = logging.getLogger(__name__)

def errorHandler(request, e):
	if type(e) == IndexError:
		return render(request, 'pages/error.html', {'message': 'Please check input!'})
	else:
		return render(request, 'pages/error.html', {'message': str(e)})

@login_required
def getSecretView(request):
	#FLAW-5
	# try:

		#FLAW-4
		# logger.info(f"User: {request.user.username}")

		username = request.GET.get('user')
		user = User.objects.get(username=username)
		#FLAW-3
		# if user.username != request.user.username:
		# 	raise Exception('Wrong value for user!')


		secret_id = int(request.GET.get('id'))

		secret = list(set(secret.secret for secret in Secret.objects.filter(user__username = user, id = secret_id)))

		return HttpResponse(f'<h1>Your secret: {secret[0]}</h1>')
	#FLAW-5
	# except Exception as e:
	# 	return errorHandler(request, e)
		

@login_required
def secretsView(request):
	#FLAW-5
	# try:

		#FLAW-4
		# logger.info(f"User: {request.user.username}")
		if request.user.is_authenticated:
			print('works')
			return JsonResponse({'username': request.user.username, 'secrets': list(set(secret.secret for secret in Secret.objects.filter(user__username=request.user)))})
		else:
			print('messed up')
			return JsonResponse({'username': 'anonymous', 'secrets': ['no secret for you']})
		
	#FLAW-5
	# except Exception as e:
	# 	return errorHandler(request, e)

@login_required
def saveView(request):
	#FLAW-5
	# try:

		#FLAW-4
		# logger.info(f"User: {request.user.username}")
		secret = request.POST.get('secret','').strip()
		user_name = request.user

		#FLAW-1
		# Secret.objects.create(user=user_name, secret=secret)
		user = User.objects.get(username=user_name)
		
		conn = sqlite3.connect('server/db.sqlite3')
		cursor = conn.cursor()
		
		#injection: my_secret'); DELETE FROM pages_secret; SELECT * FROM pages_secret WHERE 'secret' LIKE ('
		cursor.executescript(f"INSERT INTO pages_secret (user_id, secret) VALUES('{user.id}', '{secret}');")
		conn.commit()
		#
		
		return redirect('/')

	#FLAW-5
	# except Exception as e:
	# 	return errorHandler(request, e)


@login_required
def homePageView(request):
	#FLAW-5
	# try:

		#FLAW-4
		# logger.info(f"User: {request.user.username}")

		secrets = Secret.objects.filter(user__username=request.user)
		return render(request, 'pages/index.html', {'secrets': secrets})

	#FLAW-5
	# except Exception as e:
	# 	return errorHandler(request, e)
