import unittest

import default
import re


class Test_default(unittest.TestCase):
    def test_direction(self):
        self.assertIn(default.DIRECTION,["forward","backward"])
        
    def test_firstRegExp(self):
        self.assertIsInstance(default.EXPR_FIRST,str)
        re.compile(default.EXPR_FIRST)
    def test_secondRegExp(self):
        self.assertIsInstance(default.EXPR_SECOND,str)
        re.compile(default.EXPR_SECOND)
        
    def test_dataPath(self):
        self.isrelativesafepath(default.PATH_DATA)
    def test_resultPath(self):
        self.isrelativesafepath(default.PATH_RESULT)

    def isrelativesafepath(self,path):
        self.assertIsInstance(path,str)
        #path have to be ralative
        self.assertNotIn(path[0],['/','\\'],"should be relative")
        self.assertNotIn(':',path,"should be relative, and shouldn't contani : ")
        #often forbiden characters
        for forbidden in ['#','%','&','{','}','<','>','*','?',' ','$','!','\'','"',':','@','+','`','|','=']:
            self.assertNotIn(forbidden,path,"shouldn't contain %s"%forbidden)
        #special name meaning
        #names shouldn't start with . or _
        self.assertNotIn(path[0],['.','_','-'],"shouldn't start with . _ -")
        self.assertNotIn(path[len(path)-1],['.','_','-'],"shouldn't end with . _ -")
        for forbidden in ['/.','\\.','/_','\\_','/-','\\-','./','.\\','_/','_\\','-/','-\\']:
            self.assertNotIn(forbidden,path,"shouldn't start or end with %s"%forbidden)

if __name__ == '__main__':
    unittest.main()
