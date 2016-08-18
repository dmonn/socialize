from .service import Service
from click import secho


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
        secho("")
        secho("********** " + r['username'] + " **********", bg='blue', fg='white')
        secho("")
        secho("Slogan: \t" + str(r['slogan']))
        secho("Website:\t" + str(r['website']))
        secho("Interests:\t" + str(r['interests']))
        secho("Skills:   \t" + str(r['skills']))
        secho("")
        secho("Status:   \t" + str(r['status']))
        secho("Groups:   \t" + str(r['groups']))
        secho("")

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
