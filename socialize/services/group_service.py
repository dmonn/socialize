from .service import Service
from click import secho


class GroupService(Service):
    def join_group(self, groupname, passphrase=None):
        r = self.post('groups/' + groupname + "/join/", data={})
        self.check_reponse(r, success="Successfully joined the group " + groupname,
                           error="Couldn't join group " + groupname)

    def leave_group(self, groupname):
        r = self.post('groups/' + groupname + "/leave/", data={})
        self.check_reponse(r, success="Successfully left the group " + groupname,
                           error="Couldn't leave group " + groupname)

    def delete_group(self, groupname):
        r = self.post('groups/' + groupname + "/delete/", data={})
        self.check_reponse(r, success="Successfully deleted the group " + groupname,
                           error="Couldn't delete group " + groupname)

    def get_group_messages(self, groupname):
        r = self.get('groups/' + groupname + '/messages/')

        print ""
        for message in r:
            self.display_messages(message)
        print ""

    def post_group_message(self, groupname, message):
        r = self.post('groups/' + groupname + '/messages/post/', data={'message': str(message)})
        self.check_reponse(r, success="Successfully created group message", error="Couldn't create message.")

    def get_group(self, groupname):
        r = self.get('groups/' + groupname + '/')
        self.display_group_info(r)

    def create_group(self, groupname, description=None, passphrase=None):
        r = self.post('groups/' + groupname + '/',
                      data={'description': str(description), 'passphrase': str(passphrase)})
        self.check_reponse(r, success="Successfully created new group " + groupname, error="Couldn't create group.")

    def display_messages(self, m):
        print m['username'] + "> " + m['message']

    def display_group_info(self, g):
        secho("")
        secho("********** " + g['name'] + " **********", bg='blue', fg='white')
        secho("# "+g['description'], fg="white")
        secho("")
        secho(str(g['member_count']) + " members")
        secho("")


groups = GroupService()
