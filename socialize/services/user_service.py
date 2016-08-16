from .service import Service


class UserService(Service):
    def get_current_user(self):
        r = self.get('user/')
        self.print_user_info(r)

    def set_attr(self, slogan=None, website=None, interests=None, skills=None):
        r = self.post('user/', data={
            'slogan': slogan,
            'website': website,
            'interests': interests,
            'skills': skills,
        })

        self.check_reponse(r, "Profile successfully updated.")

    def get_user(self, name):
        r = self.get('user/' + name + "/")

        if r != 404:
            self.print_user_info(r)
        else:
            print("The user was not found. Maybe you typed the username wrong?")

    def print_user_info(self, r):
        print("")
        print("********** " + r['username'] + " **********")
        print("")
        print("Slogan: \t" + str(r['slogan']))
        print("Website:\t" + str(r['website']))
        print("Interests:\t" + str(r['interests']))
        print("Skills:   \t" + str(r['skills']))
        print("")
        print("Status:   \t" + str(r['status']))
        print("Joined Groups:   \t" + str(r['status']))
        print("")

    # Following

    def follow_user(self, username):
        r = self.post('user/follow/' + username + '/', data={})

        self.check_reponse(r, success="Successfully followed user " + username,
                           error="Unable to follow user " + username + ".")

    def unfollow_user(self, username):
        r = self.post('user/unfollow/' + username + '/', data={})

        self.check_reponse(r, success="Successfully unfollowed user " + username,
                           error="Unable to cancel follow for user " + username + ". Are you really following this user?")


usermanagement = UserService()
