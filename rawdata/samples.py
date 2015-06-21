#!/usr/bin/python3
# samples.py


def main():
    """
    Generates sample tables - run main() to see examples
    but normal operation is to call from program or api.
    """
    print('samples.py')
    print('Creates random data and strings in various formats')

def Samples(object):
    """
    Definitions are stored in /rawdata/samples/*.sample
    import rawdata.samples as sample
    s = sample.Sample()
    print(s.list())    # shows list of available samples
    s1 = s.show('finance.bank_transactions') 
    s2 = s.show('course.subjects') 
    """
    def __init__(self):
        self.sample_list = []
        
        
    def __str__(self):
        res = 'List of available sample definitions\n'
        for d in self.sample_list:
            res += d
        return d

if __name__ == '__main__':
    main()	
    
        