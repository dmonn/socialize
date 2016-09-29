from .service import Service


class StatusService(Service):

    def get_feed(self):
        r = self.get('status/feed/')
        print("")
        for status in r:
            self.print_status(status)
        print("")

    def post_status(self, message):
        r = self.post('status/', data={'message': str(message)})
        self.check_reponse(r, success="Successfully posted a new status")

    def print_status(self, status):
        print(str(status['username'])+"> "+str(status['message']))


statusmanagement = StatusService()
