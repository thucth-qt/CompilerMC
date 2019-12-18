import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """
        int foo(int i){
            int j;
            /*for (j=0; j<10; j=j+1){
                putInt(j);
                if (j>5) break;
                putString("\\n");
            } */
            if (true)
                putInt(100);
            else
                putInt(200);
            return 1;
        }

        void main() {
            foo(10);
        }
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
