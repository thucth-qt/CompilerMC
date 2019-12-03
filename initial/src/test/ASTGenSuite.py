import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Test variable declaration
    def test_single_variable(self):
        input = """int x;"""
        expect = "Program([VarDecl(x,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_array_declaration_float(self):
        input = """float x,y;"""
        expect = "Program([VarDecl(x,FloatType),VarDecl(y,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_array_declaration_int(self):
        input = """int x; float y,z;"""
        expect = "Program([VarDecl(x,IntType),VarDecl(y,FloatType),VarDecl(z,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_multi_variable_declaration(self):
        input = """boolean a[10],b;"""
        expect = "Program([VarDecl(a,ArrayType(BoolType,10)),VarDecl(b,BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_multi_declaration(self):
        input = """boolean a[10],b[5];"""
        expect = "Program([VarDecl(a,ArrayType(BoolType,10)),VarDecl(b,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_mix_declaration(self):
        input = """boolean a[10]; float b[5];"""
        expect = "Program([VarDecl(a,ArrayType(BoolType,10)),VarDecl(b,ArrayType(FloatType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_program_multi_variable_declaration(self):
        input = """int a; float b; boolean c; string d;"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,BoolType),VarDecl(d,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_program_multi_array_declaration(self):
        input = """int a[5]; float b[6]; boolean c[7];"""
        expect = "Program([VarDecl(a,ArrayType(IntType,5)),VarDecl(b,ArrayType(FloatType,6)),VarDecl(c,ArrayType(BoolType,7))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_program_multi_variable_array(self):
        input = """int a; float b; string a[10]; boolean d[5];"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(a,ArrayType(StringType,10)),VarDecl(d,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_program_multi_variable_array_hard(self):
        input = """int a,x,f; float b,z; string a[10], l[6], r; boolean d[5];"""
        expect = "Program([VarDecl(a,IntType),VarDecl(x,IntType),VarDecl(f,IntType),VarDecl(b,FloatType),VarDecl(z,FloatType),VarDecl(a,ArrayType(StringType,10)),VarDecl(l,ArrayType(StringType,6)),VarDecl(r,StringType),VarDecl(d,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_expr_recursion1(self):
        input = """int a1[10], a2[3];"""
        expect = "Program([VarDecl(a1,ArrayType(IntType,10)),VarDecl(a2,ArrayType(IntType,3))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # Test function declaration with parameters
    def test_function_para_empty1(self):
        input = """void main() {}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_function_single_para2(self):
        input = """int main(string x) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(x,StringType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_function_multi_para3(self):
        input = """void main(boolean a, float b) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,BoolType),VarDecl(b,FloatType)],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_function_single_array4(self):
        input = """void main(float a[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(FloatType))],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_function_multi_array5(self):
        input = """int main(boolean a[], float b[], int k) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(BoolType)),VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(k,IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    # Test program with mamy functions
    def test_function_type_array(self):
        input = """int main() {}   void main2() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(main2),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_function_void_type_array(self):
        input = """void main(int a) {} void main2(string a) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType)],VoidType,Block([])),FuncDecl(Id(main2),[VarDecl(a,StringType)],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_program_multi_function(self):
        input = """int[] main() {} float pow() {}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],FloatType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_program_multi_function_variable(self):
        input = """int[] main() {} float[] pow() {} int a,b,c;"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_program_multi_function_array(self):
        input = """int[] main(int k[]) {} float[] pow() {} int a[5],b[5],c[5];"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(k,ArrayTypePointer(IntType))],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(a,ArrayType(IntType,5)),VarDecl(b,ArrayType(IntType,5)),VarDecl(c,ArrayType(IntType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # Test if statement
    def test_if_stmt_base(self):
        input = """int main() {if(true) print("hello");}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BooleanLiteral(true),CallExpr(Id(print),[StringLiteral(hello)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_if__else_stmt_base(self):
        input = """void main() {if(true) return 1; else foo(5);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),Return(IntLiteral(1)),CallExpr(Id(foo),[IntLiteral(5)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_if_stmt_hard(self):
        input = """void main() 
            {
                if(a==4) {
                    print("hello");
                    a = a || 100;
                }
            }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(==,Id(a),IntLiteral(4)),Block([CallExpr(Id(print),[StringLiteral(hello)]),BinaryOp(=,Id(a),BinaryOp(||,Id(a),IntLiteral(100)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_if_else_stmt_hard(self):
        input = """int main() {if(a || c) print("hello"); else foo(x);}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(||,Id(a),Id(c)),CallExpr(Id(print),[StringLiteral(hello)]),CallExpr(Id(foo),[Id(x)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_if_else_stmt_mix(self):
        input = """void main() {
            if(a || b && c) {
                int a[5];
                foo(a);
            }
            else {
                return;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(||,Id(a),BinaryOp(&&,Id(b),Id(c))),Block([VarDecl(a,ArrayType(IntType,5)),CallExpr(Id(foo),[Id(a)])]),Block([Return()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    # Test do while statement
    def test_do_while_base(self):
        input = """void main(int k) {do foo(k1); while(a%6==0);}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(k,IntType)],VoidType,Block([Dowhile([CallExpr(Id(foo),[Id(k1)])],BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(6)),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_do_while_medium(self):
        input = """void main() {do i = a; print(a); while(a==2);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([BinaryOp(=,Id(i),Id(a)),CallExpr(Id(print),[Id(a)])],BinaryOp(==,Id(a),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_do_while_hard(self):
        input = """void main(int args[]) {do {if(false) print("2");} while(div(a));}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(IntType))],VoidType,Block([Dowhile([Block([If(BooleanLiteral(false),CallExpr(Id(print),[StringLiteral(2)]))])],CallExpr(Id(div),[Id(a)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    # Test for statemet
    def test_for_base(self):
        input = """void printout() {for(i=0;i<100;i=i+1) print(i);}"""
        expect = "Program([FuncDecl(Id(printout),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(print),[Id(i)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_for_medium(self):
        input = """void main() {for(i=0;i && 1;i=i+1) {print(i*3);}}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(&&,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(print),[BinaryOp(*,Id(i),IntLiteral(3))])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_for_hard(self):
        input = """void main() {for(i = 1+a[len(a)];a[i]>=1e-10;i = i-10) print(i/5);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),CallExpr(Id(len),[Id(a)]))));BinaryOp(>=,ArrayCell(Id(a),Id(i)),FloatLiteral(1e-10));BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(10)));CallExpr(Id(print),[BinaryOp(/,Id(i),IntLiteral(5))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
        
    # Test break and continue
    def test_break(self):
        input = """void main() {for(i = a[6];a[i]>=(2*5);i = 10/i/80) continue;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),ArrayCell(Id(a),IntLiteral(6)));BinaryOp(>=,ArrayCell(Id(a),Id(i)),BinaryOp(*,IntLiteral(2),IntLiteral(5)));BinaryOp(=,Id(i),BinaryOp(/,BinaryOp(/,IntLiteral(10),Id(i)),IntLiteral(80)));Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_continue(self):
        input = """void main() {for(i = 1+a[6];a[i]>=(7/5);i = 10%i) continue;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),IntLiteral(6))));BinaryOp(>=,ArrayCell(Id(a),Id(i)),BinaryOp(/,IntLiteral(7),IntLiteral(5)));BinaryOp(=,Id(i),BinaryOp(%,IntLiteral(10),Id(i)));Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_assign(self):
        input = """void main() {return a == 5;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Return(BinaryOp(==,Id(a),IntLiteral(5)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_or(self):
        input = """void main() {a = a || !a;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(||,Id(a),UnaryOp(!,Id(a))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_and(self):
        input = """void main() {a = a && true;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(&&,Id(a),BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_equal(self):
        input = """void main() {a[9] = a == 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,ArrayCell(Id(a),IntLiteral(9)),BinaryOp(==,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_not_equal(self):
        input = """void main() {a = !a != 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(!=,UnaryOp(!,Id(a)),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_less_than(self):
        input = """void main() {boolA = a < a*4;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(boolA),BinaryOp(<,Id(a),BinaryOp(*,Id(a),IntLiteral(4))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_less_equal(self):
        input = """void main() {result = a <= 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(result),BinaryOp(<=,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_great_than(self):
        input = """void main() {a = a > a*10;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(>,Id(a),BinaryOp(*,Id(a),IntLiteral(10))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_great_equal(self):
        input = """void main() {a = bool1 >= b[1];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(>=,Id(bool1),ArrayCell(Id(b),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_add(self):
        input = """void main() {a = a + a + 3;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(+,BinaryOp(+,Id(a),Id(a)),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_subtract(self):
        input = """void main() {a[10] = a[10] - 100;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,ArrayCell(Id(a),IntLiteral(10)),BinaryOp(-,ArrayCell(Id(a),IntLiteral(10)),IntLiteral(100)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_mul(self):
        input = """void main() {a = a * 20;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(20)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_div(self):
        input = """void main() {a = b / 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(/,Id(b),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_mod(self):
        input = """void main() {a = a % 5;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(%,Id(a),IntLiteral(5)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_not(self):
        input = """void main() {a = !true;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),UnaryOp(!,BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_sub(self):
        input = """void main() {a = 30-59;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(-,IntLiteral(30),IntLiteral(59)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    # Test array cell

    def test_array_cell_base(self):
        input = """void main() {y=a[5]+b[1];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(y),BinaryOp(+,ArrayCell(Id(a),IntLiteral(5)),ArrayCell(Id(b),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_array_cell_medium(self):
        input = """void main() {a[5+x]*b[0];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(*,ArrayCell(Id(a),BinaryOp(+,IntLiteral(5),Id(x))),ArrayCell(Id(b),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_array_cell_hard(self):
        input = """void main() {array[foo(10)];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(array),CallExpr(Id(foo),[IntLiteral(10)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_array_cell_expr_base(self):
        input = """void main() {return A[x];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Return(ArrayCell(Id(A),Id(x)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_array_cell_expr_medium(self):
        input = """void main() {foo(a);return a[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[Id(a)]),Return(ArrayCell(Id(a),IntLiteral(5)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_array_cell_expr_hard(self):
        input = """void main() {(foo(arr)[5])[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(ArrayCell(CallExpr(Id(foo),[Id(arr)]),IntLiteral(5)),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_array_cell_expr_super_hard(self):
        input = """void main() {foo(foo(foo(foo()[5])[5])[5])[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[]),IntLiteral(5))]),IntLiteral(5))]),IntLiteral(5))]),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_cal_func_base(self):
        input = """void main() {foo(50);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[IntLiteral(50)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_cal_func_single_variable(self):
        input = """void main() {foo(a*b);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[BinaryOp(*,Id(a),Id(b))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_cal_func_single_array(self):
        input = """void main() {return foo(a[5])*foo(foo(arr[1]));}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Return(BinaryOp(*,CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(5))]),CallExpr(Id(foo),[CallExpr(Id(foo),[ArrayCell(Id(arr),IntLiteral(1))])])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_cal_func_multi_variable(self):
        input = """void main() {foo(a, b, c, 10);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[Id(a),Id(b),Id(c),IntLiteral(10)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_cal_func_multi_array(self):
        input = """void main() {a[5]; b[c[5]];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),IntLiteral(5)),ArrayCell(Id(b),ArrayCell(Id(c),IntLiteral(5)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_cal_func_multi_variable_array(self):
        input = """void main(int k) {foo(a, b[6], foo1(70));}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(k,IntType)],VoidType,Block([CallExpr(Id(foo),[Id(a),ArrayCell(Id(b),IntLiteral(6)),CallExpr(Id(foo1),[IntLiteral(70)])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    # # Test program with multi function declaration
    def test_multi_function_declaration(self):
        input = """void main1() {} boolean main2() {} string main3() {}"""
        expect = "Program([FuncDecl(Id(main1),[],VoidType,Block([])),FuncDecl(Id(main2),[],BoolType,Block([])),FuncDecl(Id(main3),[],StringType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_multi_function_variable_declaration(self):
        input = """void main(int k) {} int a; void main() {} float a1b2[5];"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(k,IntType)],VoidType,Block([])),VarDecl(a,IntType),FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(a1b2,ArrayType(FloatType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    # Test long program
    def test_long_program_1(self):
        input = r"""
        void main(){
            for (a=1;a<100;a=a*2){
                continue;
            }
            for(x=1;d!=1;d=d+1){
                int e;
                e = d;
                break;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(100));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([Continue()])),For(BinaryOp(=,Id(x),IntLiteral(1));BinaryOp(!=,Id(d),IntLiteral(1));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),Break()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_long_program_2(self):
        input = r"""
        void main(){
            for (a=1;a!=10;a=a*2){
                for(b=2;b!=10;b=b*2){
                    for(c=100;c!=0;c=c%2){
                        for(d=1000;d>0;d=d%10){
                            int e;
                            e = d;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(!=,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(!=,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    def test_long_program_3(self):
        input = r"""
        void main(){
            for (a=1;a<100;a=a+1){
                for(b=1;b<10;b=b+10){
                    for(c=1;c<50;c=c+1){
                        if (c){
                            boolean xl;
                            xl = c=="true";
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(100));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(<,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(10)));Block([For(BinaryOp(=,Id(c),IntLiteral(1));BinaryOp(<,Id(c),IntLiteral(50));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([If(Id(c),Block([VarDecl(xl,BoolType),BinaryOp(=,Id(xl),BinaryOp(==,Id(c),StringLiteral(true)))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_long_program_4(self):
        input = r"""void main(int args){
            string c;
            for (a=1; true; a=a+1){
                if (a % 2 == 0){
                    for (b=0; b != 1;b=b+2){
                        int a;
                        float b;
                        b = a;
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,IntType)],VoidType,Block([VarDecl(c,StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BooleanLiteral(true);BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,FloatType),BinaryOp(=,Id(b),Id(a))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_long_program_5(self):
        input = r"""void main(){
            int a;
            string b;
            for (a=1; a=!true; a=a+1){
                if (a % 2 == 0){
                    for (b=0; b != 1;b=b+2){
                        b = a/b;
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(=,Id(a),UnaryOp(!,BooleanLiteral(true)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([BinaryOp(=,Id(b),BinaryOp(/,Id(a),Id(b)))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_long_program_6(self):
        input = r"""void main(){
            for (a=1;a<10;a=a+1){
                for(b=2;b%10==0;b=b+1){
                    int c;
                    float d;
                    c = b;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,BinaryOp(%,Id(b),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(c,IntType),VarDecl(d,FloatType),BinaryOp(=,Id(c),Id(b))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_long_program_7(self):
        input = r"""void main(){
            int b;
            boolean c;
            for (a=1; a < 10; a=a+1){
                for (b=0; b != 10; b=b+1){
                    c = b;
                }
                b = a + 1;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(b,IntType),VarDecl(c,BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([BinaryOp(=,Id(c),Id(b))])),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_long_program_8(self):
        input = r"""void main(){
            int b;
            boolean c;
            for (a=1; a < 10; a=a+1){
                if (a % 2 == 0){
                    c = false;
                    b = b + 1;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(b,IntType),VarDecl(c,BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp(=,Id(c),BooleanLiteral(false)),BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_long_program_9(self):
        input = r"""void main(){
            int a;
            a = true;
            if (true){
                if (a == true){
                    if (!a){
                        a = false;
                        string b;
                        b = a;
                    }
                    else{
                        if ((a == b || c != b) && a > b){
                            int e;
                            e = a;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a))]),Block([If(BinaryOp(&&,BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(c),Id(b))),BinaryOp(>,Id(a),Id(b))),Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(a))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_long_program_10(self):
        input = r"""void main(){
            int a;
            a = true;
            if (!true){
                if (a == !true){
                    if (!a){
                        a = false;
                        string b;
                        b = a;
                    }
                    else{
                        string b;
                        b = a;
                    }
                }
                else{
                    return a != false;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(UnaryOp(!,BooleanLiteral(true)),Block([If(BinaryOp(==,Id(a),UnaryOp(!,BooleanLiteral(true))),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a))]),Block([VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a))]))]),Block([Return(BinaryOp(!=,Id(a),BooleanLiteral(false)))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))


    def test_more_simple_program(self):
        """More complex program"""
        input = """int main () {
            putIntlit(foo(3));
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntlit),[CallExpr(Id(foo),[IntLiteral(3)])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            return getIntLn();
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return(CallExpr(Id(getIntLn),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_true_and_false(self):
           
        input = """void f(int a,float b, float c){
            return true && false || (2 > 3/5);
        }"""
        expect = "Program([FuncDecl(Id(f),[VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,FloatType)],VoidType,Block([Return(BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),BinaryOp(>,IntLiteral(2),BinaryOp(/,IntLiteral(3),IntLiteral(5)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_more_call_function(self):
        input = """int main () {
            print(putIntLn(4));
            ar[12];
            foo(a[10],r);
            break;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[CallExpr(Id(putIntLn),[IntLiteral(4)])]),ArrayCell(Id(ar),IntLiteral(12)),CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(10)),Id(r)]),Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_if_not_semi(self):
        input = """int main (int args) {
            if( (c > x) < d){
                int a,b[10];
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,IntType)],IntType,Block([If(BinaryOp(<,BinaryOp(>,Id(c),Id(x)),Id(d)),Block([VarDecl(a,IntType),VarDecl(b,ArrayType(IntType,10))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_nested_if_Statements(self):
        input = """
        int foo (int i) 
        {
            if (a+1) 
            {
                {
                    {
                        {
                            if(b+a) foo(a/4);
                        }
                    }
                }
            } 
            else 
            {
                if (c+d) t+a; else func(a(b(c)))[f+6*d()];
            }
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(i,IntType)],IntType,Block([If(BinaryOp(+,Id(a),IntLiteral(1)),Block([Block([Block([Block([If(BinaryOp(+,Id(b),Id(a)),CallExpr(Id(foo),[BinaryOp(/,Id(a),IntLiteral(4))]))])])])]),Block([If(BinaryOp(+,Id(c),Id(d)),BinaryOp(+,Id(t),Id(a)),ArrayCell(CallExpr(Id(func),[CallExpr(Id(a),[CallExpr(Id(b),[Id(c)])])]),BinaryOp(+,Id(f),BinaryOp(*,IntLiteral(6),CallExpr(Id(d),[])))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_return_nothing(self):
        input = """int[] ham(int a[], float b[]) {
            return none;
        }"""
        expect = "Program([FuncDecl(Id(ham),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([Return(Id(none))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_nested_func_Call(self):
        input = """void foo() {
            do{ 
                f(foo(fr(aaa(e(r()))))); 
            } while !(a>d);
        }"""
        expect = "Program([FuncDecl(Id(foo),[],VoidType,Block([Dowhile([Block([CallExpr(Id(f),[CallExpr(Id(foo),[CallExpr(Id(fr),[CallExpr(Id(aaa),[CallExpr(Id(e),[CallExpr(Id(r),[])])])])])])])],UnaryOp(!,BinaryOp(>,Id(a),Id(d))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_bool_in_do(self):
        input = """
        int main () {
           do return true||false; while false && true;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Return(BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false)))],BinaryOp(&&,BooleanLiteral(false),BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_if_in_Dowhile(self):
        input = """
        float d () {
            do 
                if (a!=s) {
                    if (t>a) 
                        if (d>=e) 
                            if (a<y) {x+1;}
                } 
            while foo();
        }"""
        expect = "Program([FuncDecl(Id(d),[],FloatType,Block([Dowhile([If(BinaryOp(!=,Id(a),Id(s)),Block([If(BinaryOp(>,Id(t),Id(a)),If(BinaryOp(>=,Id(d),Id(e)),If(BinaryOp(<,Id(a),Id(y)),Block([BinaryOp(+,Id(x),IntLiteral(1))]))))]))],CallExpr(Id(foo),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_complicated_array_element(self):
        input = """
        int foo(int a){
            for(i = 0;i!= 100; i=i+1){
                if(a[a[a[a[a[4]]]]]) i=i*2;
                else i = i -1;
            }
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(!=,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(ArrayCell(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(4)))))),BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(2))),BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_if_with_complex_arr_index(self):
        input = """
        int j;
        void main() {
            if(a[a[a[40]]]==true) break;
        }"""
        expect = "Program([VarDecl(j,IntType),FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(==,ArrayCell(Id(a),ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(40)))),BooleanLiteral(true)),Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_var_many_decl(self):
        input = """
        int a; 
        float b[90],c,d[3]; 
        boolean e; 
        void main(int k){}
        """
        expect = "Program([VarDecl(a,IntType),VarDecl(b,ArrayType(FloatType,90)),VarDecl(c,FloatType),VarDecl(d,ArrayType(FloatType,3)),VarDecl(e,BoolType),FuncDecl(Id(main),[VarDecl(k,IntType)],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_println_complex_array_index(self):
        input = """void b(int a[],int b){
                          int a;
                          a=1;
                          println(a);
                          {
                            println(b[b[b[b[4]]]]);
                          }
                }"""
        expect = "Program([FuncDecl(Id(b),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,IntType)],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(1)),CallExpr(Id(println),[Id(a)]),Block([CallExpr(Id(println),[ArrayCell(Id(b),ArrayCell(Id(b),ArrayCell(Id(b),ArrayCell(Id(b),IntLiteral(4)))))])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_func_empty(self):
        input = """
        void Calculate(){
        //comment here
        //no statement inside
        }"""
        expect = "Program([FuncDecl(Id(Calculate),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_print_Boolit(self):
        input = """void foo(){
                boolean b ;
                b = true;
                if( !b == false) 
                    println(" b is true");
                else print("b is false");
            }"""
        expect = "Program([FuncDecl(Id(foo),[],VoidType,Block([VarDecl(b,BoolType),BinaryOp(=,Id(b),BooleanLiteral(true)),If(BinaryOp(==,UnaryOp(!,Id(b)),BooleanLiteral(false)),CallExpr(Id(println),[StringLiteral( b is true)]),CallExpr(Id(print),[StringLiteral(b is false)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_normal_func(self):
        input = """
        void main(){
            int sum,arr[10],i;
            sum=0;
            for (i=0;i<10;i=i+1)
                sum=sum+arr[1];
            return sum;
                  
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(sum,IntType),VarDecl(arr,ArrayType(IntType,10)),VarDecl(i,IntType),BinaryOp(=,Id(sum),IntLiteral(0)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),ArrayCell(Id(arr),IntLiteral(1))))),Return(Id(sum))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_find_max(self):
        input = """
                int max(int arr[]){
                    int max;
                    max=arr[0];
                    for(i=1;i<len(arr);i=i+1){
                        if (max<arr[i])
                            max=arr[i];
                    }
                }
                      
        """
        expect = "Program([FuncDecl(Id(max),[VarDecl(arr,ArrayTypePointer(IntType))],IntType,Block([VarDecl(max,IntType),BinaryOp(=,Id(max),ArrayCell(Id(arr),IntLiteral(0))),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),CallExpr(Id(len),[Id(arr)]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,Id(max),ArrayCell(Id(arr),Id(i))),BinaryOp(=,Id(max),ArrayCell(Id(arr),Id(i))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
                    

    def test_breakstmt(self):
        input = """
                void main(){
                    for(walker=0;walker<10;walker=walker+1)
                    {
                        println(arr[walker]);
                        break;
                        break;
                        break;
                    }
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(walker),IntLiteral(0));BinaryOp(<,Id(walker),IntLiteral(10));BinaryOp(=,Id(walker),BinaryOp(+,Id(walker),IntLiteral(1)));Block([CallExpr(Id(println),[ArrayCell(Id(arr),Id(walker))]),Break(),Break(),Break()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_do_while(self):
        input = """
                void main(){
                    do {
                      println("alibaba");
                      i=i+1;
                      if(i==9)
                        break;
                    }
                    while(i<10);
                    do {continue;} while (true);
                }         
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([CallExpr(Id(println),[StringLiteral(alibaba)]),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),If(BinaryOp(==,Id(i),IntLiteral(9)),Break())])],BinaryOp(<,Id(i),IntLiteral(10))),Dowhile([Block([Continue()])],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_many_brackets(self):
        input = """
        void main() {
                print(((((((((((((((3*((((((4)))))))))))))))))))));
        }
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(print),[BinaryOp(*,IntLiteral(3),IntLiteral(4))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_few_brackets(self):
        input = """
        void main() {yeah = ((((((n))/2)))) + nice;}
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(yeah),BinaryOp(+,BinaryOp(/,Id(n),IntLiteral(2)),Id(nice)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_many_blocks(self):
        input = """
        void main() {
            {}
            {}
            {}
            {print("something");}
            {print("this is a block");}
            {print("something");}
            {print("this is a block");}
            {print("something");}
            {print("this is a block");}
            {print("something");}
            {print("this is a block");}
            {}
            {}
            {}
        }
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Block([]),Block([]),Block([]),Block([CallExpr(Id(print),[StringLiteral(something)])]),Block([CallExpr(Id(print),[StringLiteral(this is a block)])]),Block([CallExpr(Id(print),[StringLiteral(something)])]),Block([CallExpr(Id(print),[StringLiteral(this is a block)])]),Block([CallExpr(Id(print),[StringLiteral(something)])]),Block([CallExpr(Id(print),[StringLiteral(this is a block)])]),Block([CallExpr(Id(print),[StringLiteral(something)])]),Block([CallExpr(Id(print),[StringLiteral(this is a block)])]),Block([]),Block([]),Block([])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_many_ifs(self):
        input = """
        void main() {
            if(1)
                if(2) 
                    if(3) 
                        if(4) 
                            if(5) 
                                if(6) 
                                    if(7) 
                                        print(i);
                                    else print("hihi");
                                else break;
        }
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(IntLiteral(1),If(IntLiteral(2),If(IntLiteral(3),If(IntLiteral(4),If(IntLiteral(5),If(IntLiteral(6),If(IntLiteral(7),CallExpr(Id(print),[Id(i)]),CallExpr(Id(print),[StringLiteral(hihi)])),Break()))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_many_dowhiles(self):
        input = """
        void main() {
            do{
                do{
                    do{
                        do{
                            print("hihi");
                        }
                        while(true);
                    }
                    while(true);
                }
                while(true);
            }
            while(true);
        }

                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([Dowhile([Block([Dowhile([Block([Dowhile([Block([CallExpr(Id(print),[StringLiteral(hihi)])])],BooleanLiteral(true))])],BooleanLiteral(true))])],BooleanLiteral(true))])],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

