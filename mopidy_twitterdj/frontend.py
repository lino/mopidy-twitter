import pykka
import logging

from mopidy import core


class TwitterDJFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(TwitterDJFrontend, self).__init__()
        self.core = core
        logger = logging.getLogger()