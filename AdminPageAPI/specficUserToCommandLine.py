import argparse

def specificUser(userName):
    """

    This function utilizes the core functionality of the adminPage API with a command line interface to get individual users information.

    :param userName:
    :return:
    """
    data = ['name','sam']
    timeData = ['3/4/15', '3/6/18']

    userIndex = 0

    for user in data:
        if user == userName:
            print "Username: %s" % user
            break
        userIndex = userIndex + 1

    timeIndex = 0
    for time in timeData:
        if timeIndex == userIndex:
            print "Last time logged on: %s" % time
            timeIndex = -1
        timeIndex = timeIndex + 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help='Pass username', required=True)

    args = vars(parser.parse_args())

    specificUser(args['user'])

if __name__ == "__main__":
    main()
