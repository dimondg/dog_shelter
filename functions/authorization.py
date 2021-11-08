COR_PASSWORD = "admin123"


def authorization(password):
    if password == COR_PASSWORD:
        return True
    else:
        return False
