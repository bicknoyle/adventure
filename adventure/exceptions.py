class AdventureError(Exception):
    DEFAULT_MESSAGE = 'An error ocurred'

    def __init__(self, *args, **kwargs):
        if args:
            super().__init__(*args, **kwargs)
        else:
            super().__init__(self.DEFAULT_MESSAGE, **kwargs)

class CommandNotFoundError(AdventureError):
    DEFAULT_MESSAGE = "Can't {} here."

class ExitNotFoundError(AdventureError):
    DEFAULT_MESSAGE = "Can't go {}."

class InventoryNotFoundError(AdventureError):
    DEFAULT_MESSAGE = "You don't have {} in your inventory."

class ItemNotFoundError(AdventureError):
    DEFAULT_MESSAGE = "There is no {} here."

class ItemUseError(AdventureError):
    DEFAULT_MESSAGE = "There is no use for {} here."
