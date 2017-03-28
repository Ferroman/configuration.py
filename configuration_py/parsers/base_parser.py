class BaseConfigParser(object):

    @property
    def extensions(self):
        raise NotImplementedError

    def parse(self, file_content, context={}):
        raise NotImplementedError
