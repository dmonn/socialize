from .service import Service


class ShoutService(Service):

    def get_feed(self):
        r = self.get('shoutout/feed/')
        print("")
        for status in r:
            self.print_shouts(status)
        print("")

    def post_status(self, message, anon=False):
        if anon:
            print("Posting Shoutout as Anonymous")

        r = self.post('shoutout/', data={'message': str(message), 'anon': anon})
        self.check_reponse(r, success="Successfully posted a new shoutout")

    def print_shouts(self, status):
        print(str(status['username'])+"> "+str(status['message']))


shoutouts = ShoutService()
