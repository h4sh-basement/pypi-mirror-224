from datetime import datetime
from agora_config import config
from agora_utils import AgoraTimeStamp


class MessageHeader:
    message_id = -1

    def __init__(self):
        self.SrcModule = config["Name"]
        self.MessageType = "NotSet"
        self.ConfigVersion = -1
        if MessageHeader.message_id == -1:
            MessageHeader.message_id = MessageHeader.__get_message_id()
        MessageHeader.message_id = MessageHeader.message_id + 1
        self.MessageID = MessageHeader.message_id
        self.TimeStamp = AgoraTimeStamp()

    def __get_message_id():
        utcnow = datetime.utcnow()
        beginning_of_year = datetime(utcnow.year, 1, 1)
        time_difference = utcnow - beginning_of_year
        return int(time_difference.total_seconds()*10)
