# accounts/loginauth.py
import json
from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

