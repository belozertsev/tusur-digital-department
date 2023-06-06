from django.http import HttpResponse
import json

import blog.handlerFunctions as handler


def register(req):
    if req.method == "POST":
        body = json.loads(req.body)
        username = body["username"]
        password = body["password"]

        if (handler.areCredentialsCorrect(username, password)):
            result = handler.register(username, password)

            if (result):
                return HttpResponse(json.dumps({
                    "status": True,
                    "message": "New user is registered",
                    "token": handler.generateToken(username, password)
                }), content_type="application/json")

            else:
                return HttpResponse(json.dumps({
                    "status": False,
                    "message": "New user is not registered"
                }), content_type="application/json")

        else:
            return HttpResponse(json.dumps({
                "status": False,
                "message": "Credentials are not correct"
            }), content_type="application/json")

    else:
        return HttpResponse(json.dumps({
            "status": False,
            "message": "Wrong method"
        }), content_type="application/json")


def login(req):
    if req.method == "POST":
        body = json.loads(req.body)
        username = body["username"]
        password = body["password"]

        if (handler.areCredentialsCorrect(username, password)):
            result = handler.login(username, password)

            if (result):
                return HttpResponse(json.dumps({
                    "status": True,
                    "message": "You have just successfully logged in",
                    "token": handler.generateToken(username, password)
                }), content_type="application/json")

            else:
                return HttpResponse(json.dumps({
                    "status": False,
                    "message": "Wrong password for this user or user does not exist"
                }), content_type="application/json")

        else:
            return HttpResponse(json.dumps({
                "status": False,
                "message": "Credentials are not correct"
            }), content_type="application/json")

    else:
        return HttpResponse(json.dumps({
            "status": False,
            "message": "Wrong method"
        }), content_type="application/json")
