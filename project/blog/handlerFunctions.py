from .models import User, Post, Right



def register(_username, _password):
    if User.objects.filter(username=_username).exists():
        return False
    else:
        candidate = User(username=_username, password=_password)
        candidate.save()
        return True


def login(_username, _password):
    if not User.objects.filter(username=_username).exists():
        return False
    else:
        user = User.objects.get(username=_username)
        if user.password == _password:
            return True
    return False


def areCredentialsCorrect(_username, _password):
    if len(_username) > 2 and len(_password) > 4:
        return True
    return False


def generateToken(_username, _password):
    return f'token:{_username}!{_password}!secret(should be encrypted)'


def checkToken(_token, _username, _password):
    return _token == f'token:{_username}!{_password}!secret(should be encrypted)'

def checkRight(applicant, target, right_type):
    if applicant == target:
        return True
    else:
        result = Right.objects.filter(username=target, applicant=applicant).values_list(right_type, flat=True)[0]
        return result

def getUserByPostId(postId):
    result = Post.objects.filter(id=postId).values_list('username', flat=True)
    return result[0]

def createPost(_post):
    post = Post(username=_post["username"],
                creator=_post["creator"],
                header=_post["header"],
                text=_post["text"])
    post.save()
    return True

def deletePost(_postId):
    Post.objects.filter(id=_postId).delete()
    return True

def getSettings(_username):
    return list(Right.objects.filter(username=_username).values())

def updateSettings(_username, _settings):
    Right.objects.filter(username=_username).delete()
    
    for row in _settings:
        Right(username=row["username"],
              applicant=row["applicant"],
              get_right=row["get_right"],
              post_right=row["post_right"],
              put_right=row["put_right"],
              delete_right=row["delete_right"]).save()
    return True

def addSetting(username, row):
    if (username != row["applicant"]):
        Right(username=row["username"],
              applicant=row["applicant"],
              get_right=row["get_right"],
              post_right=row["post_right"],
              put_right=row["put_right"],
              delete_right=row["delete_right"]).save()
        return True
    else:
        return False

def getFriends(targetUser):
    return list(Right.objects.filter(applicant=targetUser).values())
