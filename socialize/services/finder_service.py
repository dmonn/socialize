from .service import Service


class FinderService(Service):

    def random_users(self):
        r = self.get('finders/random/users/')
        self.format_user_list(r)

    def find_users(self, name):
        r = self.get('finders/users/'+name+'/')
        self.format_friend_list(r)

    def find_group(self, name):
        r = self.get('finders/groups/'+name+'/')
        self.format_group_list(r)


    def format_user_list(self, u):
        for user in u:
            print(str(user['username']) + ' - Interested in ' + str(user['interests']))

    def format_friend_list(self, f):
        for friend in f:
            print("Found user " + str(friend['username']))

    def format_group_list(self, g):
        for group in g:
            print("Found group '" + str(group['name']) + "' - "+ str(group['description']))

finders = FinderService()