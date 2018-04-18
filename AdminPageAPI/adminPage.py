import os
from flask import render_template, json

def admin():
    data = readJSON()

    users = []
    userTime = []

    for user in data.iterkeys():
        users.append(user)

    for user in data.itervalues():
        userTime.append(user.get('time'))

    return render_template("admin.html", users = users, userTime = userTime)

def is_admin(self):
    return self.data.get('admin')

def readJSON():
    file = getFile()
    if not os.path.exists(file):
        return {}
    with open(file) as f:
        data = json.loads(f.read())
    return data

def getFile():
    file = os.path.join('user/users.json')
    return file

def testReadJSON():
    file = ('tests/usersTest.json')
    if not os.path.exists(file):
        return {}
    with open(file) as f:
        data = json.loads(f.read())
    return data

def testAdmin():
    data = testReadJSON()

    users = []
    userTime = []

    for user in data.iterkeys():
        users.append(user)

    for user in data.itervalues():
        userTime.append(user.get('time'))

    if (len(users) > 0) and (len(userTime) > 0):
        return True