import re

def main():
     text = '''
        def get_data():
            pass

        def _private123(arg1, arg2):
            return True

        def 123not_valid():
            pass

        def __magic__():
            pass

        def mixedCase99(a=1):
            pass
        '''

     print(matched_items(text))

def matched_items(text):
    return re.findall(r"(?<=\bdef\s)[_a-zA-Z][\w]+", text)

if __name__=="__main__":
    main()