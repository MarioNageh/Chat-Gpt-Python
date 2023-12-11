"""
this module contains the ChatCompletionResult class, which is used to represent the
result of a chat completion request
"""
from typing import Optional


class ChatCompletionResult:
    """
    This class represents the result of a chat completion request
    """
    def __init__(self, result_data):
        """
        default constructor
        :param result_data:
        """
        self.result_data = result_data

    @property
    def id(self):
        """
        get the id of the result
        :return:
        """
        return self.result_data.get('id')

    @property
    def object_type(self):
        """
        get the object type of the result
        :return:
        """
        return self.result_data.get('object')

    @property
    def created(self):
        """
        get the created timestamp of the result
        :return:
        """
        return self.result_data.get('created')

    @property
    def model(self):
        """
        get the model of the result
        :return:
        """
        return self.result_data.get('model')

    @property
    def choices(self):
        """
        get the choices of the result
        :return:
        """
        return self.result_data.get('choices', [])

    @property
    def usage(self):
        """
        get the usage of the result
        :return:
        """
        return self.result_data.get('usage', {})

    @property
    def system_fingerprint(self):
        """
        get the system fingerprint of the result
        :return:
        """
        return self.result_data.get('system_fingerprint')

    @property
    def first_message_content(self) -> Optional[str]:
        """
        get the content of the first message in the result choices
        :return:
        """
        if self.choices:
            first_choice = self.choices[0]
            if 'message' in first_choice:
                message = first_choice['message']
                if 'content' in message:
                    return message['content']
        return None
