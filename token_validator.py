class TokenNotProvided(Exception):
    def __init__(self, message):
        super(TokenNotProvided, self).__init__(message)


def validate_jwt_token(token):
    if token is None:
        raise TokenNotProvided(message="Token needs to be provided")
    else:
        return token
