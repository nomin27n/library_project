class BookNotFound(Exception):
    """책이 존재하지 않을 경우"""
    pass

class BookHasNoBorrowHistory(Exception):
    """대출 이력이 없을 경우"""
    pass
