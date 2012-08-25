
class RomanDecimal(object):
    ''' 
    converts 
        - modern roman numerals to integers
        - integers to modern roman numerals.
    '''
    def int_to_roman(self, n):
        ''' 
            given and integer, n, that is greater than 0 and less than, 4000
            return its modern roman numeral represenation
        '''

        if not 0 < n < 4000:
            raise ValueError, "n must be between 1 and 3999"   
