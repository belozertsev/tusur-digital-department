from django.http import HttpResponse, HttpRequest
import json
from django.template.loader import render_to_string

from ..models import User, Post, Right
import blog.handlerFunctions as handler


def posts(req: HttpRequest, _parameter):
    if not User.objects.filter(username=req.headers['Authorization-Username']).exists():
        return HttpResponse(json.dumps({
                "status": False,
                "message": "User does not exist"
            }), content_type="application/json")
    
    if not handler.checkToken(req.headers['Authorization-Token'],
                              req.headers['Authorization-Username'],
                              User.objects.filter(username=req.headers['Authorization-Username']).values_list('password', flat=True)[0]):
        return HttpResponse(json.dumps({
                "status": False,
                "message": "Token is not valid"
            }), content_type="application/json")
        
    if req.method == 'GET':
        targetUser = _parameter
        username = req.headers['Authorization-Username']

        isAllowed = handler.checkRight(username, targetUser, 'get_right')
        if isAllowed:
            return HttpResponse(json.dumps({
                "status": True,
                "message": "Post of required user (array of posts might be empty)",
                "data": list(Post.objects.filter(username=targetUser).values())
            }), content_type="application/json")
        else:
            return HttpResponse(json.dumps({
                "status": False,
                "message": "You dont have rights",
            }), content_type="application/json")

    if req.method == 'POST':
        targetUser = _parameter
        username = req.headers['Authorization-Username']
        body = json.loads(req.body)

        if handler.checkRight(username, targetUser, 'post_right'):
            handler.createPost({
                "username": targetUser,
                "creator": username,
                "header": body["header"] or "Default header",
                "text": body["text"] or "Default text"
            })
            return HttpResponse(json.dumps({
                "status": True,
                "message": "Post is created",
            }), content_type="application/json")
        else:
            return HttpResponse(json.dumps({
                "status": False,
                "message": "You dont have rights",
            }), content_type="application/json")

    if req.method == 'DELETE':
        postId = int(_parameter)
        username = req.headers['Authorization-Username']
        targetUser = handler.getUserByPostId(postId)

        if handler.checkRight(username, targetUser, 'delete_right'):
            handler.deletePost(postId)
            return HttpResponse(json.dumps({
                "status": True,
                "message": "Post is deleted",
            }), content_type="application/json")
        else:
            return HttpResponse(json.dumps({
                "status": False,
                "message": "You dont have rights",
            }), content_type="application/json")

    else:
        return HttpResponse(json.dumps({
            "status": False,
            "message": "Umappropriate request method",
        }), content_type="application/json")


def settings(req):
    if not User.objects.filter(username=req.headers['Authorization-Username']).exists():
        return HttpResponse(json.dumps({
                "status": False,
                "message": "User does not exist"
            }), content_type="application/json")
    
    if not handler.checkToken(req.headers['Authorization-Token'],
                              req.headers['Authorization-Username'],
                              User.objects.filter(username=req.headers['Authorization-Username']).values_list('password', flat=True)[0]):
        return HttpResponse(json.dumps({
                "status": False,
                "message": "Token is not valid"
            }), content_type="application/json")
    
    if req.method == "GET":
        return HttpResponse(json.dumps({
            "status": True,
            "message": "User settings can be obtained by the 'settings' key",
            "settings": handler.getSettings(req.headers['Authorization-Username'])
        }), content_type="application/json")

    if req.method == "POST":
        username = req.headers['Authorization-Username']
        body = json.loads(req.body)

        if not body["settings"]:
            return HttpResponse(json.dumps({
                "status": False,
                "message": "Body must contain settings array",
            }), content_type="application/json")
        else:
            handler.updateSettings(username, body["settings"])
            return HttpResponse(json.dumps({
                "status": True,
                "message": "Settings are updated",
            }), content_type="application/json")


def settingsCheck(req):
    if not User.objects.filter(username=req.headers['Authorization-Username']).exists():
        return HttpResponse(json.dumps({
                "status": False,
                "message": "User does not exist"
            }), content_type="application/json")
    
    if not handler.checkToken(req.headers['Authorization-Token'],
                              req.headers['Authorization-Username'],
                              User.objects.filter(username=req.headers['Authorization-Username']).values_list('password', flat=True)[0]):
        return HttpResponse(json.dumps({
                "status": False,
                "message": "Token is not valid"
            }), content_type="application/json")
    
    body = json.loads(req.body)
    print(body)
    
    username = req.headers['Authorization-Username']
    postId = body['postId']
    rightType = body['rightType']
    targetUser = handler.getUserByPostId(postId)

    if handler.checkRight(username, targetUser, rightType):
        return HttpResponse(json.dumps({
            "status": True,
            "message": "You have required permission"
        }), content_type="application/json")
    else:
        return HttpResponse(json.dumps({
            "status": False,
            "message": "You dont have such a right"
        }), content_type="application/json")


def settingsAdd(req):
    if not User.objects.filter(username=req.headers['Authorization-Username']).exists():
        return HttpResponse(json.dumps({
                "status": False,
                "message": "User does not exist"
            }), content_type="application/json")
    
    if not handler.checkToken(req.headers['Authorization-Token'],
                              req.headers['Authorization-Username'],
                              User.objects.filter(username=req.headers['Authorization-Username']).values_list('password', flat=True)[0]):
        return HttpResponse(json.dumps({
                "status": False,
                "message": "Token is not valid"
            }), content_type="application/json")
    
    body = json.loads(req.body)
    username = req.headers['Authorization-Username']

    if not body["row"]:
        return HttpResponse(json.dumps({
            "status": False,
            "message": "Body must contain row field",
        }), content_type="application/json")
    else:
        if handler.addSetting(username, body['row']):
            return HttpResponse(json.dumps({
                "status": True,
                "message": "New rule is created",
            }), content_type="application/json")
        else:
            return HttpResponse(json.dumps({
                "status": False,
                "message": "New rule is NOT created",
            }), content_type="application/json")


def friends(req):
    if not User.objects.filter(username=req.headers['Authorization-Username']).exists():
        return HttpResponse(json.dumps({
                "status": False,
                "message": "User does not exist"
            }), content_type="application/json")
    
    if not handler.checkToken(req.headers['Authorization-Token'],
                              req.headers['Authorization-Username'],
                              User.objects.filter(username=req.headers['Authorization-Username']).values_list('password', flat=True)[0]):
        return HttpResponse(json.dumps({
                "status": False,
                "message": "Token is not valid"
            }), content_type="application/json")
    
    targetUser = req.headers['Authorization-Username']

    friends = handler.getFriends(targetUser)
    if friends:
        return HttpResponse(json.dumps({
            "status": True,
            "message": "Friends list can be obtained by the 'data' key",
            "data": friends
        }), content_type="application/json")
    else:
        return HttpResponse(json.dumps({
            "status": False,
            "message": "There are no friends",
        }), content_type="application/json")


def returnReactApp(req):
    response_data = render_to_string("index.html")
    return HttpResponse(response_data)