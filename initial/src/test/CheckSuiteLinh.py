'''
    Le Cong Linh
    1711948
'''

import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    '''Error: Redeclared'''
    def test_redeclared_variable_in_global_with_same_type(self):
        """Simple program: int main() {} """
        input = '''
        int main(){
            a();
            return 1;
        }
        void a(){
            a;
        }
        int a;
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_redeclared_function_in_global(self):
        input = '''
        float foo(int x){
            return 1.2+4;
        }
        int main(){
            foo();
            return 1;
        }
        void foo(){
            foo(1);
            int a;
            a=1;
        }
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_parameter(self):
        input = '''
        float average(int x,int y, float x, float z){
            z= (x+y)/2;
            return z;
        }
        int main(){
            average(10,10,0,0);
            return 1;
        }
        '''
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable_with_parameter(self):
        input = '''
        float average(int x,int y){
            int x;
            x= (x+y)*10/2;
            return x;
        }
        int main(){
            average(10,10);
            return 1;
        }
        '''
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable_with_variable_in_global(self):
        input = '''
        string name;
        int age;
        string sex;
        int main(){
            name= "Linh";
            age=20;
            sex="Male";
            return 1;
        }
        string addr;
        string name[2];
        '''
        expect = "Redeclared Variable: name"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_OK_redeclared_parameter_with_variable_in_local(self):
        input = '''
        string name;
        int age;
        string sex;
        string addName(string name,int age,string sex){
            name= "Linh";
            age=20;
            sex="Male";
            return name;
        }
        int main(){
            string X;
            X= addName("hi",1,"hello");
            return 1;
        }
        string addr;
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_OK_redeclared_variable_with_function_in_local(self):
        input = '''
        int a1, a2, a3[5];
        void mety( int mety) {
            int a1, a2, a3[5];
            return;
        }
        void main() {
            mety(10);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_OK__variable_covered_function(self):
        input = '''
        int a1, a2, a3[5];
        void number( int number) {
            int a1, a2, a3[5];
            return;
        }
        void main() {
            number(10);
            int number;
            number=10;
            number;
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_variable_with_variable_in_local(self):
        input = '''
        int a1, a2, a3[5];
        void PPL( int number) {
            int a1, a2, a3[5];
            string a2;
            a2= "Pass";
            return;
        }
        void main() {
            PPL(10);
            int number;
            number=10;
            number;
            return;
        }
        '''
        expect = "Redeclared Variable: a2"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_OK_redeclared_variable_in_function_diff_scope(self):
        input = '''
        boolean x[2];
        void swap(int a1, boolean a2[], float a3) {
            boolean b1,b2,b3;
            {
                boolean b1,b2;
                int a1,a2,a3;
                {
                    boolean b1,b2;
                }
            }
            return;
        }

        void main() {
            swap(10, x, 10.0);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_undeclared_variable_in_function(self):
        input = '''       
        int main(int main) {
            float x;
            x=83.477;
            return y;
        }
        '''
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_function_in_function(self):
        input = ''' 
        float sum(int x,int y)      {
            return x+y;
        }
        void main(int main) {
            int a,b;
            a=10;
            b=10;
            SUM(1+a,2+b);
        }
        '''
        expect = "Undeclared Function: SUM"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_parameter(self):
        input = ''' 
        void main(int main) {
            int a,b;
            a=10;
            b=10;
            sumOf(1+a,2+b);
        }
        float sumOf(int x,int y)      {
            return x+y+z;
        }
        '''
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_identifier_in_scope(self):
        input = """
        int a1,a2,a3;
        boolean b1,b2,b3;
        void main() {
            a1 = 5;
            {
                a2 = 6;
                b3 = true;
                float d1;
            }

            d1 = 1.1;
            return;
        }
        """
        expect = "Undeclared Identifier: d1"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_identifier_out_of_function(self):
        input = """
        int a1,a2,a3;
        void main() {
            putIntLn(a2);
            for(a1;a2<7;a5){
                putIntLn(a3);
            }
            d1 = 1.1;
            return;
        }
        """
        expect = "Undeclared Identifier: a5"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_hard_undeclared_function(self):
        """Hard Undeclared Function"""
        input = """int a(){
                        return 2;
                   }
                   float[] b(){
                       float A[324];
                       return A;
                   }
                   string c(){
                       return "4123";
                   }
                   boolean[] d(){
                       boolean arr[14];
                       return arr;
                   }
                   float main(){
                       int a;
                       int b;
                       int c;
                        {
                            if (a == 1)
                            {
                                a = a + 1;
                                b = 2;
                                if (true)
                                    a = 1;
                                else
                                    a = 2;
                                MAIN(2,41,324);
                            }
                            else
                                a = 4;
                        }
                        return 32.424;
                   }
                """
        expect = "Undeclared Function: MAIN"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_very_simple_undeclared_identifier(self):
        """Very simple undeclared Identifier """
        input = """int a;
                   float b;
                   string c;
                   boolean d;
                   void main() {
                       a = 2;
                       b = 32;
                       c = "312414";
                       d = true;
                       tong = 341;
                       return;
                   }"""
        expect = "Undeclared Identifier: tong"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_func_undeclared(self):
        """ Undeclared Function """
        input = """
        int main(){
            int a;
            int b;
            a = sum(a, b);
            a = sub(a, b);
            return a;
        }
        int sum(int a, int b){
            return a + b;
        }
        """
        expect = "Undeclared Function: sub"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_identifier_in_arraycell(self):
        input = """
        float p1,p2,p3[5];
        int[] entry(int a1) {
            int a2[5];
            a2[0] = a1;
            a2[1] = a1 + 1;
            a2[2] = a1 + sum(a2);
            a2[3] = a1 * 2;
            a2[3] = a1 % 3;

            return a2;
        }

        int sum(int a[]) {
            return a[1];
        }

        void main() {
            int a,b,c;
            {
                a = sum(entry(1));
                b = sum(entry(2));
                p1=2393.10;
                {
                    p2 = 2.2;
                    p3[0] = 3.33;
                }
            }
            {
                a = 1; b = 2; c = 3;
                a = entry(5)[a + b + c + d];
            }
            return;
        }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_bool_literal_in_if_stmt(self):
        input = """
        void main() {
            int a1,a2,a3;
            a1 = 5;
            if (True)
            {
                a2 = 6;
                float d1,d2;
                d2 = 15e2;
            }
            putInt(a3);
            return;
        }
        """
        expect = "Undeclared Identifier: True"
        self.assertTrue(TestChecker.test(input,expect,419))

    '''Type Miss Match In Stmt'''
    def test_conditinal_expr_in_if_not_boolean(self):
        input = """
        void main() {
            int a;
            if (a)
            {
                int a2;
                a2 = 6;
                float d1,d2;
                d2 = 1.52;
            }
            putInt(a);
            return;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([VarDecl(a2,IntType),BinaryOp(=,Id(a2),IntLiteral(6)),VarDecl(d1,FloatType),VarDecl(d2,FloatType),BinaryOp(=,Id(d2),FloatLiteral(1.52))]))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_callexpr_in_if_conditional(self):
        input = """
        string str(string s){
            return s;
        }
        void main() {
            string name;
            name="linh";
            if (str(name))
            {
                putStringLn(name);
            }
            putInt(a);
            return;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(str),[Id(name)]),Block([CallExpr(Id(putStringLn),[Id(name)])]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_typemismatchinstatement_If_FloatType(self):
        input = """

        int main() {
            int a1,a2,a3,a4;
            a1 = 1; a2 = 2; a3 = 3;
            if (a1 > 1) {
                a4 = 1;
            }
            else a4 = 10;

            if (a2 < 1) {
                a4 = a4 + 1;
            }

            float d1,d2,d3;

            if (a3 >= 1 || a4 <= 2) d1 = 1.1;
            else d1 = 0.1;

            //error here
            if (d2 = 2.5e3) a1 = a1 + 1;
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(d2),FloatLiteral(2500.0)),BinaryOp(=,Id(a1),BinaryOp(+,Id(a1),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_typemismatchinstatement_If_IntType(self):
        input = """

        int main() {
            int a1,a2,a3,a4;
            a1 = 1; a2 = 2; a3 = 3;
            //error here
            if (a1) a1 = a1 + 1;
            return a1+a2/a3-a4;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a1),BinaryOp(=,Id(a1),BinaryOp(+,Id(a1),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_typemismatch_in_if_stmt_with_bool_array(self):
        input = """
        int sum(){
                    int a, b, c;
                    boolean boo;
                    if (boo)
                        a = a + 1;
                    a = a + b;
                    2 == 3;
                    b = 2;
                    (a == 2) || (b != 3);
                    (b == c) && (a == c);
                    return 3;
                }
        float main() {
            sum();
            boolean boo[9];
            if (boo) 
                return 2.1;
            return 1.2;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(boo),Return(FloatLiteral(2.1)))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_expr1_in_for_stmt_not_inttype(self):
        input = """
        int b,a,c;
        void main() {
            boolean boo;
            for (b = 1; b < 10; b = b + 1) {
                a = a + 1;
                if (a >= 5) break;
            } 
            for (c = 2; c < 20; c = c + 1) {
                a = getInt();
                if (c % 10 == 0) 
                    continue;
            }
            for (getFloat(); boo; getInt()) a = a + 1;
        }
        """
        expect = "Type Mismatch In Statement: For(CallExpr(Id(getFloat),[]);Id(boo);CallExpr(Id(getInt),[]);BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_exp2_condition_in_forstmt_not_bool(self):
        """ Mismatch Condition(Float) For Statement """
        input = """
        void main(){
            int i;
            for (i = 1; i + getFloat(); i = i + 1){
                putLn();
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(+,Id(i),CallExpr(Id(getFloat),[]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(putLn),[])]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_exp3_step_in_forstmt_not_inttype(self):
        """ Mismatch Condition(Float) For Statement """
        input = """
        void main(){
            int i;
            int a;
            int b;
            string name;
            for (i = 1; add(a, b) < sub(a, b); name="linh"){
                add(1,2);
                sub(3,4);
            }
        }
        int add(int a, int b){
            return a + b;
        }
        int sub(int a, int b){
            return a - b;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,CallExpr(Id(add),[Id(a),Id(b)]),CallExpr(Id(sub),[Id(a),Id(b)]));BinaryOp(=,Id(name),StringLiteral(linh));Block([CallExpr(Id(add),[IntLiteral(1),IntLiteral(2)]),CallExpr(Id(sub),[IntLiteral(3),IntLiteral(4)])]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_OK_in_for_stmt(self):
        """ Mismatch Condition(Float) For Statement """
        input = """
        int a,b;
        void main(){
            for (add(1,2); add(a, b) == sub(a, b); sub(3,4)){
                int num;
                num= getInt()-2;
            }
        }
        int add(int a, int b){
            return a + b;
        }
        int sub(int a, int b){
            return a - b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_mismatch_exp3_is_arrayType_in_for_stmt(self):
        input = """
        void main(){
            int i;
            int arr[10];
            for (i = 0; i < 10; arr){
                arr[i] = 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));Id(arr);Block([BinaryOp(=,ArrayCell(Id(arr),Id(i)),IntLiteral(1))]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    Dowhile
    def test_condition_not_boolType_in_dowhile_stmt(self):
        input = """
        int main(){
            int a[25];
            do {
                return 1;
            } while(a);
            return a[1];
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([Return(IntLiteral(1))])],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_condition_is_callexpr_with_intType_in_dowhile_stmt(self):
        input = """
        int swap(int a, int b){
            int t;
            t=a;
            a=b;
            a=b;
            return a;
        }
        int main(){
            int a,b,c;
            a=10;
            b=11;
            do {
                c=swap(a,b);
            } while(a-b);
            return swap(b,c);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(c),CallExpr(Id(swap),[Id(a),Id(b)]))])],BinaryOp(-,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_condition_is_callexpr_with_floatType_in_dowhile_stmt(self):
        input = """
        int swap(int a, int b){
            int t;
            t=a;
            a=b;
            a=b;
            return a;
        }
        int main(){
            int a,b,c;
            a=10;
            b=11;
            do {
                c=swap(a,b);
            } while(1.25);
            return swap(b,c);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(c),CallExpr(Id(swap),[Id(a),Id(b)]))])],FloatLiteral(1.25))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_mismatch_condition_stringType_in_dowhile_stmt(self):
        input = """
        string main(){
            string str;
            do {
                putLn();
                putStringLn(str);
            } while(getStr(str));
            return str;
        }
        string getStr(string str){
            return str;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(putLn),[]),CallExpr(Id(putStringLn),[Id(str)])])],CallExpr(Id(getStr),[Id(str)]))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_OK_condition_boolType_in_dowhile_stmt(self):
        input = """
        string main(){
            string str;
            do {
                putLn();
                putStringLn(str);
            } while(true);
            return str;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_dowhile_stmt_expr_condition_not_boolType(self):
        input = """

        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            do
                a = a + 1;
                b = b + 2;
                c = c + 3;
                {
                    int a,b;
                    a = 1; b = 1; c = 1;
                }
            while (a <= 10 && b <= 10 || c <= 20);
            do
            {
                a = a + 1;
            }
            while (a = a + 1);
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,435))

    '''Type Miss Match In Return'''
    def test_intType_func_but_return_voidType(self):
        input = ''' 
        int sum(int x,int y)      {
            return x+y;
        }
        int main(int main) {
            int a,b;
            a=10;
            b=10;
            main = sum(1+a,2+b);
            return putLn();
        }
        '''
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(putLn),[]))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_voidType_fucn_return_not_empty(self):
        input = """
        void main(){
            int arr[10];
            if (arr[5] >= 1)
            {
                arr[3]=getInt();
                arr[4]=getInt();
            }
            return arr;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(arr))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_stringType_func_return_boolType(self):
        input = """
        string main(){
            string str;
            do {
                putLn();
                putStringLn(str);
            } while(1>4 && 5==9);
            return 5/4 != 7+4;
        }
        string getStr(string str){
            return str;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(!=,BinaryOp(/,IntLiteral(5),IntLiteral(4)),BinaryOp(+,IntLiteral(7),IntLiteral(4))))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_OK_return_empty_in_voidType_function(self):
        input = """
        void main() {
            int a1,a2,a3;
            a1 = 5;
            if (true)
            {
                a2 = 6;
                float d1,d2;
                d2 = 152;
            }
            putInt(a3);
            return;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_return_inttype_in_booltype_function(self):
        input = """
        boolean main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            do
                a = a + 1;
                b = b + 2;
                c = c + 3;
                if (c % 10 != 0) continue;
                if (c % 10 == 0) break;
            while (a <= 10 && b <= 10 || c <= 20);
            return a+b+c;
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_OK_return_arrayType_in_arrayPointerType_function(self):
        input = ''' 
        float[] main(int main) {
            float arr[10];
            arr[0]= sumOf(1,2);
            arr[2]= arr[0]+1.3;
            return arr;
        }
        float sumOf(int x,int y)      {
            return x+y;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_return_bool_arrayType_in_float_arrayPointerType_function(self):
        input = ''' 
        boolean[] exchange(boolean a[]) {
            int b[3];
            if (a[0]) b[0] = 1; else b[0] = 10;
            if (a[1]) b[1] = 10; else b[1] = 100;
            if (a[2]) b[2] = 100; else b[2] = 1000;
            return a;
        } 
        float[] connect() {
            int a[2];
            a[0] = 1; a[1] = 2;
            boolean boo[1];
            return exchange(boo);
        }
        void main() {
            int a;
            connect();
            return;
        }
        '''
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(exchange),[Id(boo)]))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_OK_return_intType_in_floatType_function(self):
        input = """
        float main() {
            int a1,a2,a3[5];
            a1 = 1; a2 = 2;
            a3[0] = a1;
            a3[1] = 1; 
            a3[2] = 2;
            a3[3] = a3[1] + a3[2];
            return a1+a2-a3[0];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_return_intArrayPoiterType_in_floatArrayPointerType_function(self):
        input = """
        int[] swap(int arr[]){
            int t;
            t=arr[0];
            arr[0]= arr[1];
            arr[1]=t;
            return arr;
        }
        float[] main() {
            int a1,a2,a3[2];
            a1 = 1; a2 = 2;
            float b1,b2,b3[2];
            b1 = 1.1; b2 = 2.2 * 2 + 3;
            a3[a1] = 1; a3[a2 - 2] = 10;
            b3[a3[0] / 10] = a1 * a2;
            return swap(a3);
        }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(swap),[Id(a3)]))"
        self.assertTrue(TestChecker.test(input,expect,444))

    '''Function Not Return'''
    def test_function_not_return_in_both_if_else(self):
        input = """
        int check(boolean a) {
            if (a == true) {
                return 0;
            }
            else
                a=false;
        }
        int test(boolean a) {
            {
                return 1;
            }
        }
        void main() {
            int a;
            boolean b;
            b = true;
            a = check(b);
            a = test(b);
            return;
        }
        """
        expect = "Function check Not Return "
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_intType_function_not_return(self):
        input = """
        boolean a;
        int explore() {
            if (a == true)
                return 0;
            else
                return 1;
        }
        int main() {
            int a;
            boolean b;
            b = true;
            a = explore();
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_OK_boolType_function_return_boolType(self):
        input = """
        boolean main() {
            {
                {
                    {
                        return true;
                    }
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_a_path_in_function_not_return(self):
        input = """
        int mul(int a, int b){
            return a*b;
        }
        int main(){
            int a;
            int b;
            if(a>b){
                a = sum(a, b);
                return a;
            }
            else
                a = mul(a, b);
        }
        int sum(int a, int b){
            return a + b;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_OK_function_return_valid(self):
        input = """
        int average(int a, int b){
            return (a+b)/2;
        }
        int main(){
            int a;
            int b;
            {
                {
                    do{
            if(a>b)
                a = average(a, b);
            else
                a = found(a, b);
            return a;
            }
            while(a==b);
            }
            }
        }
        int found(int a, int b){
            if(true)
                return a;
            else
                return b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_fuction_only_return_in_for_stmt(self):
        input = """
        int main(){
            int i;
            int a;
            for (i=1;i<10;i=i+1){
                a = a + 1;
                i=i+a-a*i;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_OK_function_return_in_path_execution(self):
        input = """
        int main(int a){
            {
                int a;
                a= 1+2+3;
            }
            {
                {
                    do return a;
                    while (a<1);
                }
            }
            if(a==1){
                return 1;
            }
            else
                a= 6+7+8;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_function_not_return_in_else_stmt(self):
        input = """
        string main(string strings){
            strings = checkString();
            return strings;
        }
        string checkString() {
            string strings;
            strings="linh";
            if (1<2)
            {
                putStringLn(strings);
                return strings;
            }
            else
            {
                int i;
                for (i=0;i<10;i=i+i){
                    putStringLn(strings);
                    return strings;
                }
            }
            strings= "hihihi";
        }
        """
        expect = "Function checkString Not Return "
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_function_return_in_if_no_else_stmt(self):
        input = """
        int testReturnInFunc() {
            int a1,a2,a3,a4;
            a1 = 1; a2 = 2; a3 = 3;
            if (a1<=a2){
                a1 = a1 + 1;
                return a1/a2+a3*a4;
            }
        }
        void main()
        {
            int a;
            a= testReturnInFunc();
        }
        """
        expect = "Function testReturnInFunc Not Return "
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_func_not_return_in_all_path(self):
        input = """
        int main(){
            int i;
            int a;
            for (i=1;i<10;i=i+1)
                {
                    if (true)
                        return a;
                    else
                        a=a+i;
                }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,454))

    '''Break Not In Loop'''
    def test_simple_break_not_in_loop(self):
        input = """
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_break_in_if_stmt_not_loop(self):
        input = """
        void main(){
            if (true){
                int a;
                a = a + 1;
            }
            else {
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_break_in_scope_not_loop(self):
        input = """
        int branch(int a) {
            int b;
            for(b = 0; b < a; b = b + 1) {
                if (b > a / 2) break;
                else continue;
            }
            int c; c = 1;
            for(b = 0; b < a; b = b + 1) {
                c = c + b;
                continue;
            }
            return c;
        }

        int gitHub(int a) {
            {break;}
            return 1;
        }
        void main() {
            int a; 
            a = branch(10);
            a = gitHub(10);
            return;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_break_outside_of_for_stmt(self):
        input = '''
        boolean x[2];
        void swap(int a1, boolean a2[], float a3) {
            boolean b1,b2,b3;
            {
                boolean b1,b2;
                int a1,a2,a3,i;
                for(i=10;i>1;i=i-1)
                    a1= a2+a3;
                break;
            }
            return;
        }

        void main() {
            swap(10, x, 10.0);
            return;
        }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_break_not_in_dowhile_stmt(self):
        input = """
        int main(int a){
            {
                int a;
                a= 1+2+3;
            }
            {
                {
                    break;
                    do return a;
                    while (a<1);
                }
            }
            if(a==1){
                return 1;
            }
            else
                a= 6+7+8;
            return a;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,459))

    '''Continue Not In Loop'''
    def test_simple_continue_not_in_loop(self):
        input = """
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_continue_in_if_stmt_not_loop(self):
        input = """
        void main(){
            if (true){
                int a;
                a = a + 1;
            }
            else {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_continue_in_block_stmt_not_loop(self):
        input = """
                int a;
                void print(string c) {
                    return;
                }
                int main(){
                    do 
                        print("PPL"); 
                        if (a + 2%4 == 2) 
                            a = 1; 
                    while(true && false);
                    {
                        continue;
                    }
                    return 1;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462)) 

    def test_continue_outside_loop(self):
        input = """
                int a;
                int b;
                float c;
                boolean d;
                int main(){
                    if (a / 1 == 0)
                    {
                        a = a + 1;
                        b = 2;
                        if (true)
                            a = 1;
                        else
                            continue;
                        a = 2;
                    }
                    else {
                        a = 4;                   
                    }
                    return a+b;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_continue_not_in_dowhile_stmt(self):
        input = """
        int putNumber(int a){
            {
                {
                    continue;
                    do return a;
                    while (a<1);
                }
            }
            if(a==1){
                return 1;
            }
            else
                a= 6+7+8;
            return 1;
        }
        void main(){
            putNumber(10);
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    '''Not Left Value'''
    def test_LHS_of_assignment_operator_is_not_identifier(self):
        input = """
                void main(){
                    int a;
                    float b;
                    boolean c;
                    2 +4-4= a;
                    return;
                }
                """
        expect = "Not Left Value: BinaryOp(-,BinaryOp(+,IntLiteral(2),IntLiteral(4)),IntLiteral(4))"
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_not_left_value_assignment_op_LHS(self):
        input = """
        int[] findNum(int a) {
            int b[2];
            b[0] = 10 * a;
            b[1] = 100 * a;
            return b;
        }
        void main() {
            int a;
            a = 10;
            findNum(a);
            if (true) 
                findNum(a-10)= a-10;
        }
        """
        expect = "Not Left Value: CallExpr(Id(findNum),[BinaryOp(-,Id(a),IntLiteral(10))])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_LHS_is_callexpr_in_asignment_op(self):
        input = """
        int[] foo(){ 
            int a[4];
            return a;}
        int main(){
            foo()[0] = 1;
            foo() = 1;
            return 0;
        }
                """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_LHS_is_binary_expr_in_asignment_op(self):
        input = """
        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            for(a=1;a<=1;a){
                a = a + 1;
                b +2 = b + 2;
                c = c + 3;
                if (c % 10 != 0) continue;
                if (c % 10 == 0) break;
                }
            return a;
        }
                """
        expect = "Not Left Value: BinaryOp(+,Id(b),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_LHS_is_literal_in_asignment_op(self):
        input = """
        int main() {
            int a; 
            10=10;
            if (a < 10) return a;
            a = 100;
            return a;
        }
                """
        expect = "Not Left Value: IntLiteral(10)"
        self.assertTrue(TestChecker.test(input,expect,469))
        
    '''No Entry Point'''
    def test_simple_no_entry_point(self):
        input = """
        int a,b;
        float c[2];
        boolean foo(){
            return true;
        }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_program_has_no_main_function(self):
        input = """
        int main;
        int[] findNum(int a) {
            int b[2];
            b[0] = 10 * a;
            b[1] = 100 * a;
            return b;
        }
        boolean foo(){
            int a;
            a = 10;
            findNum(a);
            if (true) 
                findNum(a-10)= a-10;
            return false;
        }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_main_variable_but_not_function(self):
        input = """
        string fname,minit,lname;
        float main;
        void main2() {
            main1();
        }
        boolean[] main1() {
            main2();
            boolean main[10];
            return main;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_declaration_which_is_no_main_function(self):
        """Random declaration which is named main """
        input = """
                int random(int a, float b[], string c) {
                    float d[23];
                    hung(2, d, "helloword");
                    int main;
                    MAIN();
                    return main;
                }
               void MAIN(){
                    float c[23];
                    hung(2, c, "hiworld");
                    if (true) {
                        int a;
                        a = 23;
                        float c;
                        c = 2;
                        string d;
                        d = "homnaydihoc";
                    }
                    else {
                        int ID;
                        ID=ID-ID;
                    }
                    return;
                }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_difference_MAIN_function_but_not_main(self):
        input = """
        int a,b;
        float c[2];
        boolean MAIN(){
            mAIn();
            return true;
        }
        int Main(){
            MAIN();
            return 1;
        }
        float mAIN(){
            Main();
            return 1.1;
        }
        string mAIn(){
            mAIN();
            return "No Entry Point";
        }

                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,474))

    '''Unreachable Function'''
    def test_simple_unreachable_function(self):
        input = """
        void main() {
            boolean locking;
            locking= true;
            return;
        }
        boolean[] locking() {
            boolean main[2];
            main[0]= true;
            main[1]= false;
            return main;
        }
        """
        expect = "Unreachable Function: locking"
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_function_is_not_called_by_main_function(self):
        """Function ppl unreachable """
        input = """
                int assignment3;
                boolean is10;
                boolean MicroC() {
                    is10 = true;
                    return is10;
                }
                int main(){
                    int a, b, c;
                    if (a - 3412 == 230)
                        a = a + 1;
                    do
                    a = a + b;
                    2 == 3;
                    b = 2;
                    while(is10);
                    boolean boo[2];
                    boo[0]= (a == 2) || (b != 3);
                    boo[1]= (b == c) && (a == c);
                    return 3;
                }
                """
        expect = "Unreachable Function: MicroC"
        self.assertTrue(TestChecker.test(input,expect,476))
      
    def test_no_function_call_checkSum_function(self):
        input = '''
        boolean x[2];
        void swap(int a1,int a2) {
            boolean b1,b2,b3;
            {
                boolean b1,b2;
                int a1,a2,a3;
                {
                    boolean b1,b2;
                }
            }
            return;
        }
        boolean checkNum(int num){
            if (num==1)
                return true;
            else{
                swap(num,1);
                return false;
            }
        }
        void main() {
            swap(10, 11);
            return;
        }
        '''
        expect = "Unreachable Function: checkNum"
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_hard_unreachable_function(self):
        input = """
        int a,b;
        float c[2];
        boolean MAIN(){
            return true;
        }
        int Main(){
            MAIN();
            return 1;
        }
        float mAIN(){
            Main();
            return 1.1;
        }
        string mAIn(){
            string st;
            st="ThisIsNotCalled";
            mAIN();
            return st;
        }
        void main(){
            return;
        }

                """
        expect = "Unreachable Function: mAIn"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_unreachable_function_check_is_hidden_by_variable(self):
        input = """
        void test() {
            set();
            return;
        }
        int set(){
            test();
            return 1;
        }
        int check(int a) {
            if (a == 0) return 1;
            int b,c;
            b = 1; c = 10;
            return (a + b) * c * check(a - 1);
        }
        void main() {
            int check;
            check = 2;
            check;
        }
        """
        expect = "Unreachable Function: check"
        self.assertTrue(TestChecker.test(input,expect,479))

    '''Type Miss Match In ArrayCell'''
    def test_E1_in_arrayCell_is_not_arrayType(self):
        input = """
        int swap(){
            int arr[2];
            int t;
            t=arr[0];
            arr[0]= arr[1];
            t[1]= t;
            return t;
        }
        int main(){
            int a,b,c;
            do {
                c=swap();
            } while(a-b == b-a);
            return swap();
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(t),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_E1_in_arrayCell_is_not_arrayTypePointerType(self):
        input = """
        int[] startNum1(int num[]){
            if(num[0]==num[1])
                return num;
            else
                return startNum1(num);
        }
        int startNum2(int x){
            return x;
        }
        void main(){
            int list[2];
            list[0]= startNum1(list)[0];
            list[1]= startNum2(list[0])[0];
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(startNum2),[ArrayCell(Id(list),IntLiteral(0))]),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_E2_in_arrayCell_is_not_intType(self):
        input = """
        void main(){
            int i;
            int arr[10];
            for (i = 0; i < 10; i=i+1){
                arr[i<i+1] = 1;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),BinaryOp(<,Id(i),BinaryOp(+,Id(i),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_type_not_match_in_binary_expr(self):
        input = """
                int[] foo(int n,int r) {
                    int a[5];
                    return a;
                }

                int main() {
                    int a;
                    a = foo + 10;
                    foo(1,1);
                    return 10;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_error_string_is_assigned_boolean(self):
        input = """
        string main(){
            string str;
            do {
                putLn();
                putStringLn(str);
            } while(false);
            return str;
        }
        string getStr(string str){
            str= false;
            return str;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(str),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_OK_intLiteral_add_floatLiteral_return_floatType(self):
        input = """
        float main()
        {
            int i, j;
            int result;
            for(i = 1; i <= 10; i = i + 1)
            {
                for(j = 2; j <= 9; j = j + 1)
                {
                    result = i * j;
                }
            }
            return result+4.5;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_error_negative_unary_stringType(self):
        input = """
                string main()
                {
                    int i, n;
                    string STR;
                    -STR;
                    int S; S=0;
                    for (i = 0; i < n; i = i + 1)
                        S = S + i;
                    return STR;
                }   
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(STR))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_type_miss_match_in_sub_unary_operator(self):
        input = """
        boolean main() {
            int a1,a2,a3;
            a1 = 5;
            if (true)
            {
                a2 = 6;
                float d1,d2;
                d2 = 15.2;
            }
            putInt(a3);
            return -main();
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,CallExpr(Id(main),[]))"
        self.assertTrue(TestChecker.test(input,expect,487))

    '''Type Miss Match In Assignment Expr'''
    def test_error_LHS_in_assignment_op_is_voidType(self):
        input = """
        void main()
        {
            int i, j;
            int result;
            for(i = 1; i <= 10; i = i + 1)
            {
                float fl;
                fl=1.1;
                putFloat(fl)== fl;
            }
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(putFloat),[Id(fl)]),Id(fl))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_error_LHS_in_assignment_op_is_arrayType(self):
        input = """
        float main() {
            int a1,a2,a3[5];
            a1 = 1; a2 = 2;
            a3[0] = a1;
            a3 == 1; 
            a3[2] = 2;
            a3[3] = a3[1] + a3[2];
            return a1+a2-a3[0];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a3),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_error_LHS_in_assignment_op_is_arrayPointerType(self):
        input = """
        int[] startNum1(int num[]){
            if(num[0]==num[1])
                return num;
            else
                return startNum1(num);
        }
        int startNum2(int x){
            return x;
        }
        void main(){
            int list[2];
            list[0]= startNum1(list)[0];
            if(startNum1(list)==list[0])
                return;
            list[1]= startNum2(list[0]);
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(startNum1),[Id(list)]),ArrayCell(Id(list),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_error_not_equal_unary_is_not_boolType(self):
        input = """
                void main()
                {
                    int i, n;
                    int S; S=0;
                    for (i = 0; !n; i = i + 1)
                        S = S + i;
                    return ;
                }   
                """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(n))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_OK_intTyoe_coerce_float_in_assignment_operator(self):
        input = """
        int b,a,c;
        float main() {
            boolean boo;
            float x;
            int y;
            y=10;
            for (b = 1; b < 10; b = b + 1) {
                a = a + 1;
                if (a >= 5) break;
            } 
            for (c = 2; c < 20; c = c + 1) {
                a = getInt();
                if (c % 10 == 0) 
                    continue;
            }
            x=y;
            return y;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    '''Type Miss Match In CallExpr'''
    def test_call_expr_differ_num_of_param(self):
        input = """
        int foo(int x){ return x;}
        int main(){
            int a;
            foo(1,2);
            foo(a);
            return 0;
        }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_call_expr_differ_type_of_parameter(self):
        input = """
        int setInt(int x){ return x;}
        int main(){
            boolean a;
            int x;
            x= setInt(a);
            return x;
        }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(setInt),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_error_use_name_variable_like_function(self):
        input = """
        int x;
        int main(){
            x();
            return 0;
        }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(x),[])"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_floatType_can_not_coerced_to_intType(self):
        input = """
        float sqrt(float num){
            return num;
        }
        float pow(float num, int exp){
            int i;
            for (i = 1; i <= exp; i=i+1)
                num = num * num;
            return num;
        }
        string print(string s){
            return s;
        }
        void main(){
            int i;
            float data[10];
            print("Enter 10 elements: ");
            for(i=0; i < 10; i=i+1)
                {
                    sqrt(data[i]);
                    pow(data[i],data[i+1]);
                }
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(pow),[ArrayCell(Id(data),Id(i)),ArrayCell(Id(data),BinaryOp(+,Id(i),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_error_actual_param_passing_into_formal_para_in_callexpr_is_not_the_same_type(self):
        input = """
                int[] checkArray(int a, float b, int c[]) {
                    int d[3];
                    return d;
                }
               void main(){
                    float a, b, c, x, y, z;
                    a = 9;
                    b = 12;
                    c = 3;
                    int arr[10];
                    checkArray(1,a,checkArray(1,b,arr)[1-3]);
                    x = a - b / 3 + c * 2 - 1;
                    z = a - ( b / (3 + c) * 2) - 1;
                    x= getFloat();
                    putFloat(getFloat());
                    y = a - b / (3 + c) * (2 - 1);
                    putFloat(getFloat());
                    return;
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(checkArray),[IntLiteral(1),Id(a),ArrayCell(CallExpr(Id(checkArray),[IntLiteral(1),Id(b),Id(arr)]),BinaryOp(-,IntLiteral(1),IntLiteral(3)))])"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_LHS_not_value_in_call_expr(self):
        input = """
                int f;
                int main() {
                    int num1,num2, r, result;
                    num1 = 4;
                    num2= 5;
                    pow(num1,num2) = result;
                    return pow(num1-num2,num2+num1);
                }
                int factorial(int n) {
                    for(f = 1; n > 1; n = n - 1)
                        f = f*n;
                    return f;
                }

                int pow(int x,int y) {
                    return factorial(x)/factorial(x*y);
                }
                """
        expect = "Not Left Value: CallExpr(Id(pow),[Id(num1),Id(num2)])"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_call_expr_arrayType_is_not_the_same_element_type(self):
        input = """
        int[] swap(int arr[]){
            int t;
            t=arr[0];
            arr[0]= arr[1];
            arr[1]=t;
            return arr;
        }
        void main() {
            int lst1[10];
            boolean lst2[10];
            if (lst2[0]==true)
                lst1= swap(lst2);
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(swap),[Id(lst2)])"
        self.assertTrue(TestChecker.test(input,expect,499))