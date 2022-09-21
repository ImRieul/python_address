import os


__all__ = [i for i in os.listdir() if i.find('.py') != -1 and i != os.path.basename(__file__)]