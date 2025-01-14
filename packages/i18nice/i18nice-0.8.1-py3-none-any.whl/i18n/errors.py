class I18nException(Exception):
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value


class I18nFileLoadError(I18nException):
    pass


class I18nInvalidStaticRef(I18nException):
    pass


class I18nInvalidFormat(I18nException):
    pass
