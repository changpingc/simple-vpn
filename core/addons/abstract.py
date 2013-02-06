import abc


class Addon(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, config):
        self.config = config

    def setup(self):
        pass

    def on_session_established(self):
        pass

    def cleanup(self):
        pass
