from .service import Service


class MessageService(Service):
    def send_message(self, user, message):
        r = self.post('message/send/', data={'to_user': user, 'message': message})
        self.check_reponse(r, success="Message successfully sent.", error="Message couldn't be sent.")

    def get_unread_messages(self):
        r = self.get('message/unread/')
        self.show_inbox(r)

    def read_message(self, id):
        r = self.get('message/read/'+str(id)+'/')
        self.show_message(r)

    def get_conversation(self, user):
        r = self.get('message/conversations/'+user+'/')
        self.show_convo(r)

    def get_conversations(self):
        r = self.get('message/conversations/')
        self.show_convos(r)

    def show_inbox(self, i):
        for message in i:
            print("> Found message [id: "+str(message['id'])+"] from user " + str(message['user']))

    def show_message(self, m):
        if(str(m) != '404'):
            print(str(m['sender'] + "> "+str(m['content'])))
        else:
            print("Message not found.")

    def show_convos(self, c):
        print("")

        for conversation in c:
            print(">>> " + str(conversation['username']))

        print("")

    def show_convo(self, c):
        print("")
        for message in c:
            print(str(message['user']) + "> "+str(message['content']))

        print("")

messages = MessageService()