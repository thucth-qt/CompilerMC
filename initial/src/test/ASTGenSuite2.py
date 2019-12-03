import unittest
from TestUtils import TestAST
from AST import *
class ASTGenSuite(unittest.TestCase):
    def test_declare_int_variable(self):
        """AST 1: Declare a variable type int"""
        input = """int a;"""
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_declare_float_variable(self):
        """AST 2: Declare a variable type float"""
        input = """float a;"""
        expect = str(Program([VarDecl(Id("a"),FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_declare_string_array(self):
        """AST 3: Declare a array 3 elements type string"""
        input = """int a[10];"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(IntLiteral(10),IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_declare_boolean_variable(self):
        """AST 4: declare 2 variable type boolean inline"""
        input = """boolean a,b,c;"""
        expect = str(Program([VarDecl(Id("a"),BoolType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_declare_many_variables(self):
        """AST 5: declare a variable and a array type int inline"""
        input = """int a,b[100];"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),ArrayType(IntLiteral(100),IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_many_variables_in_line(self):
        """AST 6: declare 2 variable in multiple line"""
        input = """int a;
                   float b;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_many_variables_in_line_2(self):
        """AST 7: declare variable and array in multiple line"""
        input = """string a;
                   boolean b[3];"""
        expect = str(Program([VarDecl(Id("a"),StringType()),VarDecl(Id("b"),ArrayType(IntLiteral(3),BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_declare_main_function(self):
        """AST 8: declare function no paramater no body"""
        input = """int main(){}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_declare_function_with_paramater(self):
        """AST 9: declare function 1 paramater with float type"""
        input = """float main(string st){}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("st"),StringType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_declare_function_with_paramater_2(self):
        """AST 10: declare function with 1 paramater array pointer type"""
        input = """string main(int a[]){}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),ArrayPointerType(IntType()))],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_declare_function_with_many_paramater(self):
        """AST 11: declare function with many paramater 2"""
        input = """boolean main(string a, boolean b){}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),StringType()),VarDecl(Id("b"),BoolType())],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_declare_function_with_many_paramater_2(self):
        """AST 12: declare function with many paramater 3"""
        input = """string main(int a, boolean b[]){}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),ArrayPointerType(BoolType()))],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_declare_function_return_array(self):
        """AST 13: declare function return array pointer type int"""
        input = """int[] main(int a){}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType())],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_declare_function_return_array_2(self):
        """AST 14: declare function return array pointer type float"""
        input = """float[] main(string a[]){}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_declare_function_and_variable(self):
        """AST 15: declare variable and function"""
        input = """
            int a;
            float main(){}
        """
        expect = str(Program([VarDecl(Id("a"),IntType()),FuncDecl(Id("main"),[],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_declare_function_and_variable_2(self):
        """AST 16: declare many variable and function"""
        input = """
            int a,b[3];
            float main(){}
            boolean c;
            string[] foo(int d){}
        """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),ArrayType(IntLiteral(3),IntType())),FuncDecl(Id("main"),[],FloatType(),Block([])),VarDecl(Id("c"),BoolType()),FuncDecl(Id("foo"),[VarDecl(Id("d"),IntType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_return_statement_no_expression(self):
        """AST 17: return statement no expression"""
        input = """int main(){return;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_return_statement_with_expression(self):
        """AST 18: return statement with boolean"""
        input = """int main() {
                    return true;            
                }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_break_statement(self):
        """AST 19: break statement"""
        input = """int main(){break;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_continue_statement(self):
        """AST 20: continue statement"""
        input = """int main(){continue;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_simple_if_statement(self):
        """AST 21: simple if statement no else"""
        input = """
            int main(){
                if(true) return; 
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_simple_if_else_statement(self):
        """AST 22: simple if else statement"""
        input = """
                int main(){
                    if(false) break;
                    else return;
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(False),Break(),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_assign_operator(self):
        """AST 23: assign operator"""
        input = """
            int main(){
                a = b;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_math_operator(self):
        """AST 24: math operator"""
        input = """
         int main(){
         a + b;
         a - b;
         a * b;
         a / b;
         a % b;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("a"),Id("b")),BinaryOp("*",Id("a"),Id("b")),BinaryOp("/",Id("a"),Id("b")),BinaryOp("%",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_multiple_math_operator(self):
        """AST 25: multiple math operator"""
        input = """
            int main(){
                a%1 - 1.2*a + a/3;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",BinaryOp("-",BinaryOp("%",Id("a"),IntLiteral(1)),BinaryOp("*",FloatLiteral(1.2),Id("a"))),BinaryOp("/",Id("a"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_and_or_operator(self):
        """AST 26: AND OR operator"""
        input = """
            int main(){
                a||b;
                a&&b;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("||",Id("a"),Id("b")),BinaryOp("&&",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_multiple_equal_operator(self):
        """AST 27: equal operator"""
        input =  """
            int main(){
                a != 3;
                a == 1.2;
                a == true;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("!=",Id("a"),IntLiteral(3)),BinaryOp("==",Id("a"),FloatLiteral(1.2)),BinaryOp("==",Id("a"),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_compare_operator(self):
        """AST 28: compare operator"""
        input =   """
        int main(){
            a > 1;
            a < 1.2;
            a >= 1.2e3;
            a <= 2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp(">",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),FloatLiteral(1.2)),BinaryOp(">=",Id("a"),FloatLiteral(1200.0)),BinaryOp("<=",Id("a"),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_unary_operator(self):
        """AST 29: unary operator"""
        input =   """
        int main(){
             !a;
             !1;
             -2;
             -1.2e-3;
         }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("!",Id("a")),UnaryOp("!",IntLiteral(1)),UnaryOp("-",IntLiteral(2)),UnaryOp("-",FloatLiteral(0.0012))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_multiple_unary_operator(self):
        """AST 30: multiple unary operator"""
        input =   """
         int main(){
            !!a;
            -!1;
            --1.2;
            ---false;
         }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("!",UnaryOp("!",Id("a"))),UnaryOp("-",UnaryOp("!",IntLiteral(1))),UnaryOp("-",UnaryOp("-",FloatLiteral(1.2))),UnaryOp("-",UnaryOp("-",UnaryOp("-",BooleanLiteral(False))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_multiple_assign_operator(self):
        """AST 31: multiple assign operator"""
        input =   """
        int main(){
            a=1="string"=1.2e3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",IntLiteral(1),BinaryOp("=",StringLiteral("string"),FloatLiteral(1200.0))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_nested_if_else_statement(self):
        """AST 32: nested if else statement inline"""
        input =  """
        void func(){
            if(a>1) if(a>2) a=1; else a=2;    
        }
        """
        expect = str(Program([FuncDecl(Id("func"),[],VoidType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(1)),If(BinaryOp(">",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_if_else_statement_with_block_statement(self):
        """AST 33: if else statement with block statement"""
        input =  """
            int main(){
                if(exp1){}
                else{}
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("exp1"),Block([]),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_nested_if_else_statement_with_block_statement(self):
        """AST 34: nested if else statement with block statement"""
        input = """
        int main(){
            if(a>1){
                if(a>2) a=1;
            }
            else a=2;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(1)),Block([If(BinaryOp(">",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),IntLiteral(1)))]),BinaryOp("=",Id("a"),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_for_statement(self):
        """AST 35: for statement"""
        input = """
        int main(){
            for (i=1;i<10;i=i+1) print(i);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),CallExpr(Id("print"),[Id("i")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_nested_for_statement(self):
        """AST 36: nested for statement"""
        input = """
            int main(){
                for(i=1;i<10;i=i+1)
                    for(j=1;j<10;j=j+1)
                        print(i+j);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<",Id("j"),IntLiteral(10)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),CallExpr(Id("print"),[BinaryOp("+",Id("i"),Id("j"))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_nested_for_statement_with_block_stmt_2(self):
        """AST 37: nested for statement with block statement"""
        input = """
        int main(){
            for(i=1;i<10;i=i+1){
                for(j=1;j<10;j=j+1){
                    print(i);
                    print(j);
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<",Id("j"),IntLiteral(10)),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([CallExpr(Id("print"),[Id("i")]),CallExpr(Id("print"),[Id("j")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_do_while_statement(self):
        """AST 38: do while statement"""
        input = """
            int main(){
                do 
                    a=a+1;
                    a=a+2;
                while(a<10);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))],BinaryOp("<",Id("a"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_do_while_statement_with_many_stmt(self):
        """AST 39: do while with many statement"""
        input = """
            int main(){
                int i;
                i = 1;
                do {
                    i = i * 2;
                    print(i);
                }
                while(i<10);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),Dowhile([Block([BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(2))),CallExpr(Id("print"),[Id("i")])])],BinaryOp("<",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_do_while_statement_with_many_stmt_2(self):
        """AST 40: do while with many statement"""
        input = """
            int main(){
                int i,j;
                i = 1; j = 1;
                do {
                    x = i + j;
                    print(x);
                }
                while(i<10 && j<10);
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType()),BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("j"),IntLiteral(1)),Dowhile([Block([BinaryOp("=",Id("x"),BinaryOp("+",Id("i"),Id("j"))),CallExpr(Id("print"),[Id("x")])])],BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("<",Id("j"),IntLiteral(10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_do_while_statement_4(self):
        """AST 41: do while with many block statement"""
        input = """
            int main(){
                do{
                    a=a+1;
                }{
                    a=a+2;
                }
                while(a<10);
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))])],BinaryOp("<",Id("a"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_variable_declare_in_block(self):
        """AST 42: declare variable in block statement"""
        input = """
            int main(){
                int a;
                float b[3];
                string c,d[3];
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),ArrayType(IntLiteral(3),FloatType())),VarDecl(Id("c"),StringType()),VarDecl(Id("d"),ArrayType(IntLiteral(3),StringType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_variable_declare_in_block_2(self):
        """AST 43: declare and intital variable in block statement"""
        input = """
            int main(){
                int a;
                a = 1;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),BinaryOp("=",Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_declare_and_if_statement(self):
        """AST 44: declare and if statement"""
        input = """
            int main(){
                int a;
                a=1;
                if(a>0) println("a la so nguyen duong");
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),BinaryOp("=",Id("a"),IntLiteral(1)),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("println"),[StringLiteral("a la so nguyen duong")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_factory_function(self):
        """AST 45: factory function"""
        input = """
            int fact(int n){
                if(n<=0) return 1;
                else return n*fact(n-1);
            }
            """
        expect = str(Program([FuncDecl(Id("fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([If(BinaryOp("<=",Id("n"),IntLiteral(0)),Return(IntLiteral(1)),Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_sum_function(self):
        """AST 46: sum function"""
        input = """
            int sum(int n){
                int s,i;
                s=0;
                 for(i=1;i<=n;i=i+1) s=s+i;
                 return s;
            }
            """
        expect = str(Program([FuncDecl(Id("sum"),[VarDecl(Id("n"),IntType())],IntType(),Block([VarDecl(Id("s"),IntType()),VarDecl(Id("i"),IntType()),BinaryOp("=",Id("s"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),Id("i")))),Return(Id("s"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_funcall_function(self):
        """AST 47: funcall expression"""
        input = """
            int main(){
                sum(10);
                fact(10);
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("sum"),[IntLiteral(10)]),CallExpr(Id("fact"),[IntLiteral(10)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_index_operator(self):
        """AST 48: index operator"""
        input = """
            int main(){
                int a[1];
                a[0]=5;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(IntLiteral(1),IntType())),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_array_function(self):
        """AST 49: array function"""
        input = """
                int[] array(int a,int b){
                    int arr[2];
                    arr[0]=a;
                    arr[1]=b;
                    return arr;
                }
                """
        expect = str(Program([FuncDecl(Id("array"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],ArrayPointerType(IntType()),Block([VarDecl(Id("arr"),ArrayType(IntLiteral(2),IntType())),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(0)),Id("a")),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(1)),Id("b")),Return(Id("arr"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_funcall_with_index_operator(self):
        """AST 50: funcall with index operator"""
        input = """
                    int main(){
                        array(1,2)[0];
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(CallExpr(Id("array"),[IntLiteral(1),IntLiteral(2)]),IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_expression_with_bracket(self):
        """AST 51: expression with bracket"""
        input = """
                int main(){
                    int a;
                    a=(1+2)*sum(2);
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),BinaryOp("=",Id("a"),BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(2)),CallExpr(Id("sum"),[IntLiteral(2)])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_nested_funcall_statement(self):
        """AST 52: nested funcall statement"""
        input = """
                    int main(){
                        sum(fact(10));
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("sum"),[CallExpr(Id("fact"),[IntLiteral(10)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_expression_With_bracket(self):
        """AST 53: funcall with many paramater"""
        input = """
                   int main(){
                        complex(a[2]+1*fact(2)/-2-5,true,1.23);
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("complex"),[BinaryOp("-",BinaryOp("+",ArrayCell(Id("a"),IntLiteral(2)),BinaryOp("/",BinaryOp("*",IntLiteral(1),CallExpr(Id("fact"),[IntLiteral(2)])),UnaryOp("-",IntLiteral(2)))),IntLiteral(5)),BooleanLiteral(True),FloatLiteral(1.23)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_if_statement_inner_for_statement(self):
        """AST 54: if statement inner for statement"""
        input = """
                   int main(){
                        int i;
                        for(i=0;i<10;i=i+1)
                            if(i%2==0) print(i);
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("print"),[Id("i")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_if_statement_inner_dowhile_statement(self):
        """AST 55: if statement inner do while statement"""
        input = """
                int main(){
                    int i;
                    i=0;
                    do
                        if(i%2==0) print(i);
                        i=i+1;
                    while(i<10);
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),BinaryOp("=",Id("i"),IntLiteral(0)),Dowhile([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("print"),[Id("i")])),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_continue_inner_for_statement(self):
        """AST 56: continue innner for statement"""
        input = """
                int main(){
                    int i;
                    for(i=0;i<10;i=i+1){
                        if(i%2!=0) continue; 
                        print(i);
                    }
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("!=",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Continue()),CallExpr(Id("print"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_break_inner_dowhile_statement(self):
        """AST 57: break inner do while statement"""
        input = """
                int main(){
                    int i;
                    i=0;
                    do
                        if(i%2==0) print(i);
                        i=i+1;
                        if(i>=10) break;
                    while(true);
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),BinaryOp("=",Id("i"),IntLiteral(0)),Dowhile([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("print"),[Id("i")])),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp(">=",Id("i"),IntLiteral(10)),Break())],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_declare_global_and_local_variable(self):
        """AST 58: declare global and local variable"""
        input = """
                    int a;
                    int main(){
                        float a;
                        string a[3];
                    }
                """
        expect = str(Program([VarDecl(Id("a"),IntType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),FloatType()),VarDecl(Id("a"),ArrayType(IntLiteral(3),StringType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_nested_to_dowhile_statement(self):
        """AST 59: nested do while statement"""
        input = """
            int main(){
                int i,j;
                i=0;j=0;
                do 
                    do
                        print(i);
                        print(j);
                        j=j+1; 
                    while(j<10);
                    i=i+1; 
                while(i<10);
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType()),BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("j"),IntLiteral(0)),Dowhile([Dowhile([CallExpr(Id("print"),[Id("i")]),CallExpr(Id("print"),[Id("j")]),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))],BinaryOp("<",Id("j"),IntLiteral(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_for_statement_inner_dowhile_statement(self):
        """AST 60: for statement innner do while statement"""
        input = """
            int main(){
                int i,j;
                i=0;j=0;
                do 
                    do
                        print(i);
                        print(j);
                        j=j+1; 
                    while(j<10);
                    i=i+1; 
                while(i<10);
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType()),BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("j"),IntLiteral(0)),Dowhile([Dowhile([CallExpr(Id("print"),[Id("i")]),CallExpr(Id("print"),[Id("j")]),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))],BinaryOp("<",Id("j"),IntLiteral(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_many_assign_and_equal_operator(self):
        """AST 61: many assign and equal operator"""
        input = """
                int main(){
                    (a=b==c)!=d=e;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",BinaryOp("!=",BinaryOp("=",Id("a"),BinaryOp("==",Id("b"),Id("c"))),Id("d")),Id("e"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_many_compare_operator(self):
        """AST 62: many compare operator"""
        input = """
                int main(){
                    (a>b)>=c==(d<e)<=f;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("==",BinaryOp(">=",BinaryOp(">",Id("a"),Id("b")),Id("c")),BinaryOp("<=",BinaryOp("<",Id("d"),Id("e")),Id("f")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362)) 
    def test_return_a_funcall(self):
        """AST 63: return a funcall"""
        input = """
                int main(){
                    return sum(10);
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(CallExpr(Id("sum"),[IntLiteral(10)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_return_a_string(self):
        """AST 64: return a string"""
        input = """
                string main(){
                    return "String";
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],StringType(),Block([Return(StringLiteral("String"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364)) 
    def test_return_a_expression(self):
        """AST 65: return a expression"""
        input = """
                float main(){
                    return 1.23+4*a%5/b;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([Return(BinaryOp("+",FloatLiteral(1.23),BinaryOp("/",BinaryOp("%",BinaryOp("*",IntLiteral(4),Id("a")),IntLiteral(5)),Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_return_a_float(self):
        """AST 66: return a float"""
        input = """
                float main(){
                    return 1.23E-4;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([Return(FloatLiteral(0.000123))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_mix_up_operator(self):
        """AST 67: mix-up operator"""
        input = """
                int foo(){
                    foo(2)[3]=a||b&&(c-35.4e10)*9+10.0/4+true;
                }
            """
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(3)),BinaryOp("||",Id("a"),BinaryOp("&&",Id("b"),BinaryOp("+",BinaryOp("+",BinaryOp("*",BinaryOp("-",Id("c"),FloatLiteral(354000000000.0)),IntLiteral(9)),BinaryOp("/",FloatLiteral(10.0),IntLiteral(4))),BooleanLiteral(True)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367)) 
    def test_program_with_line_comment(self):
        """AST 68: program with line comment"""
        input = """
            //Main Function
            int main(){
                //Body
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368)) 
    def test_program_with_block_comment(self):
        """AST 69: program with block comment"""
        input = """
            int main(){
                /* Empty
                Body */
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369)) 
    def test_complex_index_expression(self):
        """AST 70: complex index expression"""
        input = """
            int main(){
                int a[10];
                return a[(i-j)*(i+j)%2];
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),ArrayType(IntLiteral(10),IntType())),Return(ArrayCell(Id("a"),BinaryOp("%",BinaryOp("*",BinaryOp("-",Id("i"),Id("j")),BinaryOp("+",Id("i"),Id("j"))),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_dowhile_statement_for_statement(self):
        """AST 71: do while statement innner for statement"""
        input = """
            int main(){
            int i,j;
            j=0;
            for(i=0;i<10;i=i+1)
                do
                    print(i);
                    print(j);
                    j==j+1;
                while i<10;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType()),BinaryOp("=",Id("j"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Dowhile([CallExpr(Id("print"),[Id("i")]),CallExpr(Id("print"),[Id("j")]),BinaryOp("==",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))],BinaryOp("<",Id("i"),IntLiteral(10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_if_else_statement(self):
        """AST 72: if else stmt with a function call in condition part"""
        input = """
           void main(){
                if(sum(5)) a=b;
                else c=d;
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(CallExpr(Id("sum"),[IntLiteral(5)]),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("c"),Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_dowhile_stmt_with_condition(self):
        """AST 73: do while stmt with conditional expression is index expression"""
        input = """
            void main(){
                do
                    a=a+1;
                while array[1];
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],ArrayCell(Id("array"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_many_block_statement_in_block_statement(self):
        """AST 74: many block statement in block statement"""
        input = """
            int main(){
            {
                {
                    {
                        {
                            {
                                return 0;
                            }
                        }
                    }   
                }
            }
            }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([Block([Block([Return(IntLiteral(0))])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_do_while_stmt_with_condition_is_funcall(self):
        """AST 75: do while stmt with conditional expression is a function call"""
        input = """
                void main(){
                    do
                         a=a+1;
                    while sum(3);
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],CallExpr(Id("sum"),[IntLiteral(3)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375)) 
    def test_return_an_or_statement(self):
        """AST 76: return an or statement"""
        input = """
                void main(){
                    return a||b;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(BinaryOp("||",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_minus_sign_before_bracket(self):
        """AST 77: minus sign before bracket"""
        input = """
                int main(){
                    -(1+2);
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_minus_sign_with_index_expression(self):
        """AST 78: minus sign with index expression"""
        input = """
                int main(){
                    -array[1];
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("-",ArrayCell(Id("array"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_minus_sign_with_substract_operator_in_expression(self):
        """AST 79: minus sign with subtract operator in expression"""
        input = """
                int main(){
                    -1--2--3;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("-",BinaryOp("-",UnaryOp("-",IntLiteral(1)),UnaryOp("-",IntLiteral(2))),UnaryOp("-",IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_nested_index_operator(self):
        """AST 80: nested index operator"""
        input = """
                int main(){
                    array[array[array[1]]];
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("array"),ArrayCell(Id("array"),ArrayCell(Id("array"),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_expression_stmt_with_only_a_operand(self):
        """AST 81: expression statement with only a operand"""
        input = """
                void main(){
                    1;
                    a;
                    1.E-2;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([IntLiteral(1),Id("a"),FloatLiteral(0.01)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_or_with_not_of_a_variable(self):
        """AST 82: or, and with not of a variable"""
        input = """
                void main(){
                    a || !b;
                    a && !b;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("||",Id("a"),UnaryOp("!",Id("b"))),BinaryOp("&&",Id("a"),UnaryOp("!",Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_math_operator_1(self):
        """AST 83: add, sub a number with a negative number"""
        input = """
                void main(){
                    a + -b;
                    a - -b;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),UnaryOp("-",Id("b"))),BinaryOp("-",Id("a"),UnaryOp("-",Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_math_operator_2(self):
        """AST 84: mul, div, mod a number with a negative number"""
        input = """
                void main(){
                    a % -b;
                    a / -b;
                    a * -b;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("%",Id("a"),UnaryOp("-",Id("b"))),BinaryOp("/",Id("a"),UnaryOp("-",Id("b"))),BinaryOp("*",Id("a"),UnaryOp("-",Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_bracket_and_none_associativity(self):
        """AST 85: bracket and none associativity"""
        input = """
                 void main(){
                    (a == b) == c;
                    a = b == c = d == e;
                    a = b == c = d;
                    a=b=c=d;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("==",BinaryOp("==",Id("a"),Id("b")),Id("c")),BinaryOp("=",Id("a"),BinaryOp("=",BinaryOp("==",Id("b"),Id("c")),BinaryOp("==",Id("d"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("=",BinaryOp("==",Id("b"),Id("c")),Id("d"))),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_two_kind_of_none_associativity(self):
        """AST 86: two kind of none associativity"""
        input = """
                void main(){
                    a == b >= c;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("==",Id("a"),BinaryOp(">=",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test_for_do_while_stmt_inside_block(self):
        """AST 87: for,do while statement inside block of statement"""
        input = """
                void main(){
                    for(i=0;i<3;i=i+1) a=a+1;
                    do
                        a=a+1;
                    while true;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(3)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))),Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test_ucln_function(self):
        """AST 88: ucln function"""
        input = """
                int ucln(int a, int b){
                    int u;
                    if (a<b) u=a;
                    else u=b;
                    do u=u-1;
                    while((a%u!=0)||(b%u!=0));
                }
            """
        expect = str(Program([FuncDecl(Id("ucln"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([VarDecl(Id("u"),IntType()),If(BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("u"),Id("a")),BinaryOp("=",Id("u"),Id("b"))),Dowhile([BinaryOp("=",Id("u"),BinaryOp("-",Id("u"),IntLiteral(1)))],BinaryOp("||",BinaryOp("!=",BinaryOp("%",Id("a"),Id("u")),IntLiteral(0)),BinaryOp("!=",BinaryOp("%",Id("b"),Id("u")),IntLiteral(0))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test_read_a_file(self):
        """AST 89: program read a file"""
        input = """
                 int main(){
                    fp = fopen("file.txt", "r");
                    fclose(fp);
                    return 0;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("fp"),CallExpr(Id("fopen"),[StringLiteral("file.txt"),StringLiteral("r")])),CallExpr(Id("fclose"),[Id("fp")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_complex_expression(self):
        """AST 90: complex expression"""
        input = """
                 void foo(){
                        -1.23+!array[2]*sum(3);
                }
            """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([BinaryOp("+",UnaryOp("-",FloatLiteral(1.23)),BinaryOp("*",UnaryOp("!",ArrayCell(Id("array"),IntLiteral(2))),CallExpr(Id("sum"),[IntLiteral(3)])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_none_associativity(self):
        """AST 91: none associativity of >= and >"""
        input = """
                void main(){
                    a >= (b > c);
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">=",Id("a"),BinaryOp(">",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_none_associativity_2(self):
        """AST 92: none associativity of <= and <"""
        input = """
                void main(){
                    (a < b) <= c;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<=",BinaryOp("<",Id("a"),Id("b")),Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_nested_block_stmt(self):
        """AST 93: nested block statement"""
        input = """
                void main(){
                {
                    int a, b;
                    a = b;
                    {
                        int c;
                        c = 0;
                    }
                }
                }   
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),BinaryOp("=",Id("a"),Id("b")),Block([VarDecl(Id("c"),IntType()),BinaryOp("=",Id("c"),IntLiteral(0))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_return_an_expression(self):
        """AST 94: return an expression"""
        input = """
                void main(){
                    return a+1==b*2 = c%3!=d/4;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(BinaryOp("=",BinaryOp("==",BinaryOp("+",Id("a"),IntLiteral(1)),BinaryOp("*",Id("b"),IntLiteral(2))),BinaryOp("!=",BinaryOp("%",Id("c"),IntLiteral(3)),BinaryOp("/",Id("d"),IntLiteral(4)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_do_while_statement_with_many_declare(self):
        """AST 95: do while statement"""
        input = """
                void main(){
                    do
                    a = b;
                    c = c + 1;
                    foo();
                    {
                        int a;
                        int b;
                        a = b;
                    }
                     while a == 0;
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("c"),BinaryOp("+",Id("c"),IntLiteral(1))),CallExpr(Id("foo"),[]),Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),BinaryOp("=",Id("a"),Id("b"))])],BinaryOp("==",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_hello_world_program(self):
        """AST 96: Hello Word"""
        input = """
                int main(){
                    print("Hello Word\\n");
                }
            """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("print"),[StringLiteral("Hello Word\\n")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test_fibonacci_program(self):
        """AST 97: fibonacci program"""
        input = """
                int fibo(int n){
                    if(n==0) return 0;
                    if(n==1) return 1;
                    else return fibo(n-1)+fibo(n-2);
                }
                int main(){
                    int i;
                    for(i=0;i<10;i=i+1) print(fibo(i));
                }
            """
        expect = str(Program([FuncDecl(Id("fibo"),[VarDecl(Id("n"),IntType())],IntType(),Block([If(BinaryOp("==",Id("n"),IntLiteral(0)),Return(IntLiteral(0))),If(BinaryOp("==",Id("n"),IntLiteral(1)),Return(IntLiteral(1)),Return(BinaryOp("+",CallExpr(Id("fibo"),[BinaryOp("-",Id("n"),IntLiteral(1))]),CallExpr(Id("fibo"),[BinaryOp("-",Id("n"),IntLiteral(2))]))))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("i"),IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),CallExpr(Id("print"),[CallExpr(Id("fibo"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_bouble_search_function(self):
        """AST 98: bouble search function"""
        input = """
                int[] bouble(int array[], int n){
                    int i, j, swap;
                    for(i=0; i<n-1; i=i+1){
                        for (j=0; j<n-i-1; j=j+1){
                            if (array[j]>array[j+1]){
                                swap=array[j];
                                array[j]=array[j+1];
                                array[j+1]=swap;
                            }
                        }
                    }
                }
            """
        expect = str(Program([FuncDecl(Id("bouble"),[VarDecl(Id("array"),ArrayPointerType(IntType())),VarDecl(Id("n"),IntType())],ArrayPointerType(IntType()),Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType()),VarDecl(Id("swap"),IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),BinaryOp("-",BinaryOp("-",Id("n"),Id("i")),IntLiteral(1))),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp(">",ArrayCell(Id("array"),Id("j")),ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1)))),Block([BinaryOp("=",Id("swap"),ArrayCell(Id("array"),Id("j"))),BinaryOp("=",ArrayCell(Id("array"),Id("j")),ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1)))),BinaryOp("=",ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1))),Id("swap"))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_check_leap_year_function(self):
        """AST 99 check leap year function"""
        input = """
            boolean isLeapYear(int year){
                if (year < 0 )
                    cout ("This is a invalid Year." ,endl);
                else
                if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
                    return true;
                else
                return false;
            }
            """
        expect = str(Program([FuncDecl(Id("isLeapYear"),[VarDecl(Id("year"),IntType())],BoolType(),Block([If(BinaryOp("<",Id("year"),IntLiteral(0)),CallExpr(Id("cout"),[StringLiteral("This is a invalid Year."),Id("endl")]),If(BinaryOp("||",BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(400)),IntLiteral(0)),BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("year"),IntLiteral(4)),IntLiteral(0)),BinaryOp("!=",BinaryOp("%",Id("year"),IntLiteral(100)),IntLiteral(0)))),Return(BooleanLiteral(True)),Return(BooleanLiteral(False))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    def test_compare_two_string_function(self):
        """AST 100: compare two string function"""
        input = """
                int compareString(string str1, string str2){
                    int result;
                    if (strlen(str1) >= strlen(str2)){
                        for (i = 0; i < strlen(str2); i)
                            result =abs(str1[i] - str2[i]);
                        for (i = strlen(str2); i < strlen(str1); i)
                            result =str1[i];
                    }
                    else{
                        for(i=0;i<strlen(str1);i)
                            for (i = strlen(str1); i < strlen(str2); i)
                                result = str2[i];
                        }
                    return result;
                }
            """
        expect = str(Program([FuncDecl(Id("compareString"),[VarDecl(Id("str1"),StringType()),VarDecl(Id("str2"),StringType())],IntType(),Block([VarDecl(Id("result"),IntType()),If(BinaryOp(">=",CallExpr(Id("strlen"),[Id("str1")]),CallExpr(Id("strlen"),[Id("str2")])),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str2")])),Id("i"),BinaryOp("=",Id("result"),CallExpr(Id("abs"),[BinaryOp("-",ArrayCell(Id("str1"),Id("i")),ArrayCell(Id("str2"),Id("i")))]))),For(BinaryOp("=",Id("i"),CallExpr(Id("strlen"),[Id("str2")])),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str1")])),Id("i"),BinaryOp("=",Id("result"),ArrayCell(Id("str1"),Id("i"))))]),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str1")])),Id("i"),For(BinaryOp("=",Id("i"),CallExpr(Id("strlen"),[Id("str1")])),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str2")])),Id("i"),BinaryOp("=",Id("result"),ArrayCell(Id("str2"),Id("i")))))])),Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    