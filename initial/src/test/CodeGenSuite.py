import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """

        int a;
        void main() {
             
            a=1;
            putIntLn(a);
            {
                int a;
                a=2;
                putIntLn(a);
            }
            putIntLn(a);
        }
        //int b;
        """
        expect = "ahihihi"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
        #void main(){   
        #   putInt(5); 
        #}
        # class MCClass extends (java.lang.Object){
        #       public void static main(string agrs[]){
        #           putInt(5);
        #       }
        # }

    	# expect = "5"
    	# self.assertTrue(TestCodeGen.test(input,expect,501))
