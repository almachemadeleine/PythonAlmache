class UserAccount:
    login = ''
    followers = {}
    followings = {}

    def init(self, login, followers=[], followings=[]):
        self.login = login
        if len(followers) > 0:
            tmpFollowers = {}
            for key in followers:
                tmpFollowers[key] = key
            self.followers = tmpFollowers
        if len(followings) > 0:
            tmpFollowings = {}
            for key in followings:
                tmpFollowings[key] = key
            self.followings = tmpFollowings
        

    def getFollowers(self):
        return self.followers

    def getLogin(self):
        return self.login