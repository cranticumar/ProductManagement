'''
Created on Feb 5, 2016

@author: bkranthi
'''


class ModelHelper(object):
    """
    Model helpers
    """
    @staticmethod
    def enum_to_choices(enum):
        """
        """
        choices_list = list()
        for k, v in enum.__members__.items():
            choices_list.append((v.value, k))

        return choices_list
