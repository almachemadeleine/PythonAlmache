import sys
from SocialNetwork import SocialNetwork
from UserAccount import UserAccount
from ProcessString import ProcessStrings

def initializeSocialNetwork():
    socialNetwork = SocialNetwork()
    userA = UserAccount()
    userA.init('userA', followers=ProcessStrings().stringToList("userB,userD,userE,userG", ","))
    userB = UserAccount()
    userB.init('userB', followers=ProcessStrings().stringToList("userC,userJ,userI,userE", ","))
    userC = UserAccount()
    userC.init('userC', followers=ProcessStrings().stringToList("userM,userA,userJ,userI,userZ", ","))
    userZ = UserAccount()
    userZ.init('userZ', followers=ProcessStrings().stringToList("userP,userN,userC,userJ,userK", ","))

    socialNetwork.addUser(userA)
    socialNetwork.addUser(userB)
    socialNetwork.addUser(userC)
    socialNetwork.addUser(userZ)

    return socialNetwork

initialUser = sys.argv[1]
print('Initial User: %s' % (initialUser))

finalUser = sys.argv[2]
print('\nFinal User: %s' % (finalUser))

socialNetwork = initializeSocialNetwork()
distance = socialNetwork.calculateDistanceBetweenUsers(initialUser, finalUser)

print("\n Distancia entre '%s' y '%s', es: %d" % (initialUser, finalUser, distance))