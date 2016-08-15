from .service import Service


class UserService(Service):

    def get_current_user(self):
        r = self.get('user/')
        self.print_user_info(r)

    def print_user_info(self, r):
        print("")
        print("********** "+r['username']+" **********")
        print("")
        print("Slogan: \t"+str(r['slogan']))
        print("Website:\t"+str(r['website']))
        print("Interests:\t"+str(r['interests']))
        print("Skills:   \t"+str(r['skills']))
        print("")
        print("Status:   \t"+str(r['status']))
        print("Joined Groups:   \t"+str(r['status']))
        print("")

user = UserService()