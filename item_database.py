#this file is an example when a team is working in different parts
#we need this database for our price_map, but we cant wait  for it to be implemented
#thats why we have to use the mocking function
class ItemDatabase:
    def __init__(self) -> None:
        pass

    def get(self, item: str) -> float:
        pass