import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

#2.1 Redeclared Variable/Function/Parameter:
    def test_redec_global_variable (self):
        input="""
        int a;
        void main(){}
        int b,a; //error
        """
        expect= "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_redec_local_variable (self):
        input="""
        int a;
        void main(){
            int b;
            int a;
            float b;//error
        }
        """
        expect= "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,401))


    def test_redec_function (self):
        input="""
        int foo(int i){
            return i;
        }
        void foo(){}//error
        void main(){
            foo();
        }
        """
        expect= "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,402))


    def test_redec_param (self):
        input="""
        void foo(int a, int b, int a){} //error
        void main(){
            foo();
        }
        """
        expect= "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,403))


    def test_redec_mix_param_variable (self):
        input="""
        void foo(int a){
            int a; //error
        }
        void main(){
            foo();
        }
        """
        expect= "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))


    def test_redec_mix_function_variable (self):
        input="""
        void a(){}
        int a;//error
        void main(){
            a();
        }
        """
        expect= "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))


    def test_redec_builtin (self):
        input="""
        void foo(){}
        int a;
        void main(int a){
            foo();
            int foo;
            {
                float a;
            }
            foo=a;
        }
        int putFloat(int k){return 1;} //error
        
        """
        expect= "Redeclared Function: putFloat"
        self.assertTrue(TestChecker.test(input,expect,406))

#2.2 Undeclared Identifier/Function:
    def test_undec_identifier_global (self):
        input="""
        //int a;
        void main(){
            a=1; //error
        }
        """
        expect= "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,407))


    def test_undec_identifier_local (self):
        input="""
        void main(){
            int a,b,c;
            a=k; //error
        }
        """
        expect= "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,408))


    def test_undec_fucntion (self):
        input="""
        void main(){
            foo(); //error
        }
        """
        expect= "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,409))


    def test_undec_valid (self):
        input="""
        int foo1(){ return 1;}
        int main(){
            int foo2;
            return foo1();
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,410))

#2.3 Type Mismatch In Statement:
    def test_mismatch_if_constant_expr (self):
        input="""
        void main(){
            if(1+2){} //error
        }
        """
        expect= "Type Mismatch In Statement: If(BinaryOp(+,IntLiteral(1),IntLiteral(2)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,411))


    def test_mismatch_if_id_expr (self):
        input="""
        void main(){
            int a;
            a=1;
            if(a+2*a){} //error
        }
        """
        expect= "Type Mismatch In Statement: If(BinaryOp(+,Id(a),BinaryOp(*,IntLiteral(2),Id(a))),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,412))


    def test_mismatch_if_valid (self):
        input="""
        void main(){
            boolean b;
            b=true;
            int a[10];
            if(b == true &&false || (a[1]!=2) ){}
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,413))


    def test_mismatch_expr1_of_for (self):
        input="""
        void main(){
            for (
            true; //error
            true;
            5
            ){} 
        }
        """
        expect= "Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);IntLiteral(5);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,414))


    def test_mismatch_expr2_of_for (self):
        input="""
        void main(){
            int i;
            for (
                i=1;
                5; //error
                i=i+2
                ){} 
        }
        """
        expect= "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));IntLiteral(5);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(2)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,415))


    def test_mismatch_expr3_of_for (self):
        input="""
        void main(){
            int i;
            for (
                i=1;
                5; 
                3.5 //error
                ){} 
        }
        """
        expect= "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));IntLiteral(5);FloatLiteral(3.5);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,416))


    def test_mismatch_for_valid (self):
        input="""
        void main(){
            int a;
            for (a=1;a<=5;a=a+1){
                a=a-1;
            }
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,417))


    def test_mismatch_dowhile (self):
        input="""
        void main(){
            int a;
            a=1;
            do
                a=a+1;
            while (a); //error 
        }
        """
        expect= "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,418))


    def test_mismatch_dowhile_valid (self):
        input="""
        void main(){
            int a;
            a=4;
            do
                a=a+1;
            while (a==100); 
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,419))


    def test_mismatch_return_void (self):
        input="""
        void main(){
            return 1; //error
        }
        """
        expect= "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,420))


    def test_mismatch_return_not_void (self):
        input="""
        int main(){
            return; //error
        }
        """
        expect= "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,421))


    def test_mismatch_return_not_miss_type_prim (self):
        input="""
        float main(){
            return true; //error
        }
        """
        expect= "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,422))


    def test_mismatch_return_not_miss_type_array (self):
        input="""
        int[] main(){
            float a[10];
            return a; //error
        }
        """
        expect= "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,423))


    def test_mismatch_return_valid (self):
        input="""
        float main(){
            int a[10];
            return 1 + a[3];
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,424))

#2.4 Type Mismatch In Expression:
    def test_mismatch_array_id (self):
        input="""
        void main(){
            int _int_a;
            _int_a =5;
            _int_a[10]=1; //error
        }
        """
        expect= "Type Mismatch In Expression: ArrayCell(Id(_int_a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,425))


    def test_mismatch_array_index (self):
        input="""
        void main(){
            int arr[10];
            arr[2+2.5]=1; //error
        }
        """
        expect= "Type Mismatch In Expression: ArrayCell(Id(arr),BinaryOp(+,IntLiteral(2),FloatLiteral(2.5)))"
        self.assertTrue(TestChecker.test(input,expect,426))


    def test_mismatch_array_arr_pointer_type_valid (self):
        input="""
        float[] foo(){
            float a[10];
            return a;
        }
        void main(){
            foo()[2]=4;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,427))


    def test_mismatch_array_arr_type_valid (self):
        input="""
        void main(int a[]){
            a[2]=4;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,428))


    def test_mismatch_binary_boolean (self):
        input="""
        boolean main(){
            boolean a,b;
            a= true;
            b= false;
            b= a + b; //error, not plus Op on boolean type
            return b; 
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,429))


    def test_mismatch_binary_bool_valid (self):
        input="""
        boolean main(){
            boolean a,b;
            a= true;
            b= false;
            b = a == ( !b != a && a) || b; 
            return b; 
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,430))


    def test_mismatch_binary_void (self):
        input="""
        void main(){
            int a;
            a= main() +1; //error
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(main),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,431))


    def test_mismatch_binary_int (self):
        input="""
        void main(){
            int a;
            a=1;
            a= a && a;//error not && Op on int type
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,432))


    def test_mismatch_binary_int_not_same_type (self):
        input="""
        void main(){
            int a;
            a=1;
            float b;
            b=1.5;
            boolean k;
            k = a == b; //error, must the same type int
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,433))


    def test_mismatch_binary_int_return_bool_valid (self):
        input="""
        boolean main(){
            int a;
            a= 1;
            return (a < a) ||  (a<= a) || (a> a) || (a>= a) == (a != a); 
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,434))


    def test_mismatch_binary_int_with_negation_op_valid (self):
        input="""
        int main(){
            int a;
            a=1;
            return a + a - -a +(a=5); //Ok, The last operator (=) will result a value of type int when both operands are in type int.
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,435))


    def test_mismatch_binary_float_with_equal_Op (self):
        input="""
        void main(){
            float a;
            a=1;
            boolean b;
            b = a==a; //error, no Equal Op on float type
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,436))


    def test_mismatch_binary_float_with_assign_valid (self):
        input="""
        float main(){
            float a;
            return a=5; //OK, The assign operator = which results in a value of type float if the left hand side operand is in type float
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,437))


    def test_mismatch_binary_float_with_Op_valid (self):
        input="""
        float main(){
            float a;
            a=1.5;
            boolean b;
            b= (a<a) ||(a<=a) ||(a> a) || (a>=a);
            return a +a -a *a / -a;  
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,438))


    def test_mismatch_binary_string (self):
        input="""
        boolean main(){
            string a;
            a="hihihi";
            return  a == "hihihi"; //error, no == Op on string type
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(==,Id(a),StringLiteral(hihihi))"
        self.assertTrue(TestChecker.test(input,expect,439))


    def test_test_mismatch_assignment (self):
        input="""
        void main(){
            int a;
            a= 1.5; // error
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(1.5))"
        self.assertTrue(TestChecker.test(input,expect,440))


    def test_test_mismatch_func_call_mis_number_param (self):
        input="""
        void foo(int a, int b){}
        void main(){
            foo(1); //error
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,441))


    def test_test_mismatch_func_call_valid (self):
        input="""
        void foo(float a, int b[]){}
        void main(){
            int k[10];
            foo(1,k);
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,442))


    def test_test_mismatch_func_call_mis_element_type (self):
        input="""
        void foo(int a[]){}
        void main(){
            float a[10];
            foo(a);//error
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,443))

#2.5 Function not return:
    def test_func_not_return_simple (self):
        input="""
        int main(){}//error
        """
        expect= "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,444))


    def test_func_not_return_in_for_loop (self):
        input="""
        int main(){ //error
            int i;
            for(i=1;i<5;i=i+1){
                return i;
            }
        }
        """
        expect= "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,445))


    def test_func_not_return_in_if (self):
        input="""
        int main(){ //error
            int i;
            i=1;
            if (i==5) return;
            else 
                if (true) i=i+1;
                else return;
        }
        """
        expect= "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,446))


    def test_func_not_return_in_if_valid (self):
        input="""
        int main(){ 
            int i;
            i=1;
            if (i==5) return 1;
            else 
                if (true) return 1;
                else return 1;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,447))


    def test_func_not_return_in_dowhile_valid (self):
        input="""
        int main(){
            do 
                return 1;
            while(false);
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,448))


    def test_func_not_return_complex_valid (self):
        input="""
        int main(boolean k){
            if(k){
                for(1;true;2) return 1;
                if (!k)
                    do 
                        return 1;
                    while (k);
                else 
                    {{{
                        return 1;
                    }}}
            }
            else
            {{{
                if (!k && k) return 1;
                else return 1;
            }}}
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,449))

#2.6 Break/Continue not in loop:
    def test_break_not_in_loop_for_simple (self):
        input="""
        void main(){
            break; //error
        }
        """
        expect= "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,450))


    def test_break_not_in_loop_for_valid (self):
        input="""
        void main(){
            int i;
            for(i=1;i<=5;i=i+1){
                break;
            }
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,451))


    def test_break_not_in_loop_indirectly_for_valid (self):
        input="""
        void main(){
            int i;
            for (i=1;i==5;i=i+1){
                if (true) break;
                else if(false) {
                    {
                        {
                            break;
                        }
                    }
                }
            }

        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,452))


    def test_break_not_in_loop_dowhile_valid (self):
        input="""
        void main(){
            do 
                break;
            while(false);

        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,453))


    def test_break_not_in_loop_dowhile_indirectly_valid (self):
        input="""
        void main(){
            do 
                if (true) 
                {
                    do
                        if(true) break;
                    while (true);
                }
            while(false);

        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,454))


    def test_continue_not_in_loop_for (self):
        input="""
        void main(){
            int i;
            continue; //error
            for (i=0; i<=5;i=i+1){
                int k;
            }
        }
        """
        expect= "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))


    def test_continue_not_in_loop_dowhlie (self):
        input="""
        void main(){
            int i;
            continue; //error
            do
            //something
            i=3;
            while (true);
        }
        """
        expect= "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,456))

#2.7 No Entry Point:
    def test_no_entry_point_simple (self):
        input="""
        void foo(){} 
        //error

        """
        expect= "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,457))


    def test_no_entry_point_with_main_variable (self):
        input="""
        int main;
        void foo(){}
        //error
        """
        expect= "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,458))


    def test_no_entry_point_with_Main (self):
        input="""
        void Main(){}
        //error
        """
        expect= "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,459))


    def test_no_entry_point_valid (self):
        input="""
        float main(int a, string b, float c, string d[]){
            return c;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,460))

#2.8 Unreachable function:
    def test_unreachable_func_simple (self):
        input="""
        void foo(){}
        void main(){}
        """
        expect= "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,461))


    def test_unreachable_func_with_variable_with_the_same_name (self):
        input="""
        void foo(){} 
        void main(){
            int foo;
            foo =5;
        }
        //error
        """
        expect= "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,462))


    def test_unreachable_func_valid (self):
        input="""
        void foo1(){}
        void foo2(){
            foo1();
        }
        void main(){
            foo2();
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,463))

#2.9 Not left value
    def test_not_left_value_simple (self):
        input="""
        void main(){
            1=5; //error
        }

        """
        expect= "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,464))


    def test_not_left_value_func_call (self):
        input="""
        int foo(){return 1;}
        void main(){
            foo()=5; //error
        }
        """
        expect= "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,465))


    def test_not_left_value_bool_literal (self):
        input="""
        void main(){
            true=1+2; //error
        }
        """
        expect= "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,466))


    def test_not_left_value_variable_valid (self):
        input="""
        void main(){
            int a;
            a=6+5/4+5*2;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,467))


    def test_not_left_value_index_expr_valid (self):
        input="""
        void main(){
            float a[10];
            a[5]= 5.5/2+5/2 + 4*3 -4;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,468))
        

    def test_not_left_value_func_arr_pointer_expr_valid (self):
        input="""
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            foo()[3]=4+5/3;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,469))

#2.10 Unreachable statement:
    def test_unreachable_stmt_return (self):
        input="""
        void foo(){
            return;
            int a;
            a=1; //error
        }
        void main(){
            foo();
        }
        """
        expect= "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,470))


    def test_unreachable_stmt_return_in_if (self):
        input="""
        void foo(){}
        void main(){
            if (true){
                return;
                foo();//error
            }
        }
        """
        expect= "Unreachable Statement: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,471))


    def test_unreachable_stmt_return_in_if_else (self):
        input="""
        void main(){
            if (true) return;
            else return;
            int k;
            k=5;//error
        }

        """
        expect= "Unreachable Statement: BinaryOp(=,Id(k),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,472))


    def test_unreachable_stmt_loop_break (self):
        input="""
        void main(){
            int i;
            for (i=1;i<=5;i=i+1){
                break;
                i=5; //error
            }
        }
        """
        expect= "Unreachable Statement: BinaryOp(=,Id(i),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,473))


    def test_unreachable_stmt_loop_mix_break_continue (self):
        input="""
        void main(){
            int i;
            for (i=1;i<=5;i=i+1){
                if(true)
                    break;
                else 
                    continue;
                i=5; //error
            }
        }
        """
        expect= "Unreachable Statement: BinaryOp(=,Id(i),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,474))


    def test_unreachable_stmt_loop_mix_return_continue (self):
        input="""
        void main(int a){
            do
                if (false){
                    a=1;
                    continue;
                }
                else return;
                a=1000; //error
            while(false);
        }
        """
        expect= "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(1000))"
        self.assertTrue(TestChecker.test(input,expect,475))


    def test_unreachable_stmt_loop_valid (self):
        input="""
        void main(){
            int i;
            for (i=10;i<0;i=i+1){
                i=4;
            }
            if(false) 
                i=5;
            do
                i=6;
            while(false);
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,476))


    def test_unreachable_stmt_loop_declare_valid (self):
        input="""
        void main(){
            int i;
            do
            return;
            while(true);
            int k;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,477))

#2.11 Index out of range:

    def test_index_out_of_range_simple (self):
        input="""
        void main(){
            int a[10];
            a[10]=5; //eror
        }
        """
        expect= "Index Out Of Range: ArrayCell(Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,478))


    def test_index_out_of_range_negation_index (self):
        input="""
        void main(){
            float a[10];
            a[-1]=5; //error
        }
        """
        expect= "Index Out Of Range: ArrayCell(Id(a),UnaryOp(-,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,479))


    def test_index_out_of_range_valid (self):
        input="""
        void main(){
            float a[10];
            a[19/2]=5; 
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,480))


    def test_index_out_of_range_arr_pointer_type_valid (self):
        input="""
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            foo()[15]=1;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,481))


    def test_index_out_of_range_variable_valid (self):
        input="""
        void main(){
            int a[5],i;
            i=100;
            a[i]=10;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_index_out_of_range_constant_complex_expr_valid (self):
        input="""
        void main(){
            int a[10],i;
            i=5;
            a[1+3/2 --2 +9*2/3-1]=1;
            a[i/5*7]=1;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,483))


    def test_index_out_of_range_function_index_valid (self):
        input="""
        int foo(){
            return 3000;
        }
        void main(){
            float a[10];
            a[foo()]=1;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,484))

#2.12 Uninitialized Variable:
    def test_uninitialized_variable_simple (self):
        input="""
        int main(){
            int i;
            return i; //error
        }
        """
        expect= "Uninitialized Variable: i"
        self.assertTrue(TestChecker.test(input,expect,485))


    def test_uninitialized_variable_param_valid (self):
        input="""
        int main(int i,int k){
            i=5;
            return k;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,486))


    def test_uninitialized_variable_global_valid (self):
        input="""
        int i;
        int main(){
            return i;
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,487))


    def test_uninitialized_variable_valid (self):
        input="""
        int main(){
            int k;
            if (true) k=5;
            return 1; 
        }
        
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,488))


    def test_uninitialized_variable_in_if_else_valid (self):
        input="""
        int main(){
            int k;
            if (true) k=5;
            else k=6;
            return k; 
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,489))


    def test_uninitialized_variable_global_local_nested_variable_in_loop (self):
        input="""
        int k;
        int main(){
            int i;
            i = k;                  //OK
            for(i=0;i<10;i=i+1){
                int k;
                return k;           //error
            }
        }
        """
        expect= "Uninitialized Variable: k"
        self.assertTrue(TestChecker.test(input,expect,490))

#some special test cases
    def test_mismmatch_expr (self):
        input="""
        void foo1(){}
        void main(){
            foo1=5; //error
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(=,Id(foo1),IntLiteral(5))"

        self.assertTrue(TestChecker.test(input,expect,491))


    def test_mismatch_index_expr (self):
        input="""
        void main(){
            int a[10];
            a[5.0/2] =10; //error
        }
        """
        expect= "Type Mismatch In Expression: ArrayCell(Id(a),BinaryOp(/,FloatLiteral(5.0),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,492))


    def test_uninitialized_variable_in_block_valid (self):
        input="""
        void main() {
            int a,b;
            for (1;true;2){
                {a=4;}
                b=a+1; // OK, not uninitialized error
                break;
            }
            
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,493))


    def test_type_mismatch_with_declare_variable_same_name_function (self):
        input="""
        int[] foo(int a) {
            int b[10];
            return b;
        }
        void main() {
            int a; 
            foo(5);         //OK
            int foo;        //declare variable same nam function foo
            a = foo(1)[2];  //error
            return;
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,494))


    def test_unreachable_stmt_in_other_scope (self):
        input="""
        void main(){
                    foo();
                    return;
                }
                int foo(){
                    int i;
                    {
                        return 1;
                    }
                    {
                        i=1;// unreachable stmt
                    }
                }
        """
        expect= "Unreachable Statement: Block([BinaryOp(=,Id(i),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,495))


    def test_unreachable_func  (self):
        input="""
        void foo(){
            return;
        }
        void main(){
            foo; //OK
        }
        """
        expect= "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,496))


    def test_complex_valid (self):
        input="""
        float foo(){
            return 1.e-10;
        }
        float[] arr(){
            float a[10];
            return a;
        }
        void main(){
            float a;
            a=3000;
            arr()[5]=foo()+a/1.0;
            int i;
            if ((i=3) == 4)
                return;
            if (a>=3000) 
                return;
            for (i=0;i<10;i=i+1){
                arr()[i] = foo()+i;
            }
        }

        
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,497))


    def test_complex_with_built_in_valid (self):
        input="""

        int main(int args[]){
            
            int i,len,arr[100];
            //get length of array
            len = getInt();
            //enter array
            for (i=0;i<len;i=i+1){
                arr[i]=getInt();
            }
            //print array
            for (i=0;i<len;i=i+1){
                putFloat(arr[i]);   
            }
            return 1;
            
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,498))


    def test_standard_program_sort_array_valid (self):
        input="""
        int arr[100];
        int[] sort(int array[]){
            int i,j,len;
            len =100;
            for (i=0;i<len;i=i+1){
                for (j=i;j<len;j=j+1)
                    if (array[i] > array[j]) 
                        {
                            int temp;
                            temp=array[i];
                            array[i] =array[j];
                            array[j]=temp;
                        }
            }
            return array;
        }

        int random(int i){
            return i*9/5+2-3*4/5%6;
        }
        void main(){
            int i,len;
            len = getInt();
            for (i=0; i<len; i=i+1)
                arr[i]=random(i);
            if ((len=5) == 5)
                return;
            //print sorted array
            for (i=0;i<len;i=i+1)
                putInt(sort(arr)[i]);
        }
        """
        expect= ""
        self.assertTrue(TestChecker.test(input,expect,499))

