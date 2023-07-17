# Create your models here.
class SocketChannel:
    _instance = None    
    channel_name = None

    @staticmethod
    def get_instance():
        if SocketChannel._instance is None:
            SocketChannel._instance = SocketChannel()

        return SocketChannel._instance

    def set_channel_name(self, channel_name):
        self.channel_name = channel_name
