from .service import Service


class KickstarterService(Service):

    def get_supporters(self):
        r = self.get('kickstarter/')
        self.print_supporters(r)


    def print_supporters(self, s):
        for supporter in s:
            print("%-40s %s" % (str(supporter['name']), str(supporter['message'])))



kick = KickstarterService()