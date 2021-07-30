import unittest

import shlex

import scripts.arguments 

def parseString(arg):
    return vars(scripts.arguments.argparser.parse_args(shlex.split(arg)))


class Test_arguments(unittest.TestCase):
    def test_nameset(self):
        argsname=set(parseString("").keys())
        self.assertSetEqual({"source","result","path1","path2","exp1","exp2","direction"},argsname)
        
    def tryflag(self,flag,dest,value="a"):
        args=parseString(shlex.join([flag,value]))
        self.assertEqual(args[dest],value)
        del args[dest]
        self.assertNotIn(value,args)

    def test_source(self):
        self.tryflag("--source","source")
        
    def test_src(self):
        self.tryflag("--src","source")

    def test_in(self):
        self.tryflag("-in","source")

    def test_result(self):
        self.tryflag("--result","result")

    def test_rzt(self):
        self.tryflag("--rzt","result")

    def test_out(self):
        self.tryflag("-out","result")
        
    def test_path1(self):
        self.tryflag("--path1","path1","./a")

    def test_p1(self):
        self.tryflag("-p1","path1","./a")

    def test_path2(self):
        self.tryflag("--path2","path2","./a")

    def test_p2(self):
        self.tryflag("-p2","path2","./a")
        
    def test_regexp1(self):
        self.tryflag("--regexp1","exp1","\\\\d+")
        
    def test_r1(self):
        self.tryflag("-r1","exp1","\\\\d+")
        
    def test_regexp2(self):
        self.tryflag("--regexp2","exp2","\d+")
        
    def test_r2(self):
        self.tryflag("-r2","exp2","\d+")
        
    def test_direction_forward(self):
        self.tryflag("--direction","direction","forward")
    def test_direction_backward(self):
        self.tryflag("--direction","direction","backward")

if __name__ == '__main__':
    unittest.main()
