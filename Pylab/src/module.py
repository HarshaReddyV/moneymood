

class Module:
    def __init__(self,
                 com = None,
                 gen = None,
                 cso = None,
                 dso = None
                 ):
# Compulsory Modules allocation

        if com is None:
            self.com = {
                'CIS0001': 'Python Programming',
                'CIS0002': 'Data Structure and algorithms'
            }
        else:
            self.com = com
        
#General Optinal Modules Allocation

        if gen is None:
            self.gen = {
                'CIS1001': 'Computational Thinking',
                'CIS1002': 'Design Patterns',
                'CIS1003': 'Test Driven Development',
                'CIS1004': 'SQL Relational Databases'
            }
        else:
            self.gen = gen
        
#CS optional Modules allocation

        if cso is None:
            self.cso = {
                'CIS2001': 'Software quality assurance principles',
                'CIS2002': 'software reliabilities',
                'CIS2003': 'Formal methods to the system verification',
                'CIS2004': 'Algorithm complexity'
            }
        else:
            self.cso = cso
        
#DS optional Modules Allocation

        if dso is None:
            self.dso = {
                'CIS3001': 'Data visualisation',
                'CIS3002': 'An introduction to Artificial intelligence',
                'CIS3003': 'An introduction to Machine learning',
                'CIS3004': 'Statistical Methods'
            }
        else:
            self.dso = dso
        
    def list_com(self):
        for keys, values in self.com.items():
            print(f'{keys}: {values}')   

    def list_gen(self):
        for keys, values in self.gen.items():
            print(f'{keys}: {values}') 

    def list_cso(self):
        for keys, values in self.cso.items():
            print(f'{keys}: {values}') 

    def list_dso(self):
        for keys, values in self.dso.items():
            print(f'{keys}: {values}')  


    def printer(self):

        print('-'*20)
        print('COMPULSORY MODULES:')
        print('-'*20)
        self.list_com()
        print('\n')

        print('-'*20)
        print('GENERAL MODULES:')
        print('-'*20)
        self.list_gen()
        print('\n')

        print('-'*20)
        print('CS  MODULES:')
        print('-'*20)
        self.list_cso()
        print('\n')
        
        print('-'*20)
        print('DS  MODULES:')
        print('-'*20)
        self.list_dso()
        print('\n')
    

