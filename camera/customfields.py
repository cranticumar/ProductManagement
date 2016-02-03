'''
Created on Jan 2, 2016

@author: bkranthi
'''
from django.db.models import CharField


class CustomCaseCharField(CharField):
    '''
    classdocs
    '''

    def __init__(self, char_case='lower', * args, **kwargs):
        super(CustomCaseCharField, self).__init__(*args, **kwargs)
        self.char_case = char_case

    def to_python(self, value):
        # smart_text in the super class encodes the value to text anyways
        value = super(CustomCaseCharField, self).to_python(value)
        if isinstance(value, basestring):
            if self.char_case == 'title':
                return value.title()
            elif self.char_case == 'upper':
                return value.upper()
            elif self.char_case == 'lower':
                return value.lower()
        else:
            return None


class UpperCaseCharField(CharField):
    system_check_removed_details = {
        'msg': (
            'UpperCaseCharField has been removed except for support in '
            'historical migrations.'
        ),
        'hint': 'Use CustomCaseCharField instead.',
        'id': 'fields.E1001'
    }
