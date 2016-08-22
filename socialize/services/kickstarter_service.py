from .service import Service


class KickstarterService(Service):

    def get_supporters(self):
        r = self.get('kickstarter/')
        self.print_supporters(r)


    def print_supporters(self, s):
        for supporter in s:
            print ("%-40s %s" % (supporter['name'], supporter['message']))



kick = KickstarterService()