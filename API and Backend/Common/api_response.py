from flask import jsonify


class ApiResponse:
    """
    Class which will be returned as json from the api endpoints
    """

    def __init__(self, message='not set', status='unknown', **kwargs):
        self.message = message
        self.status = status
        self.errors = kwargs.get('errors', [])
        self.success = kwargs.get('success', [])

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        """
        Return a json with MIME_TYPE as application/json
        """
        return jsonify(self.to_dict())
