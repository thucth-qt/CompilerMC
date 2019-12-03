import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_unreachable_statement_normal_return_check_if(self):
        input = """
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
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(d2),FloatLiteral(2500.0)),BinaryOp(=,Id(a1),BinaryOp(+,Id(a1),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,3000))
