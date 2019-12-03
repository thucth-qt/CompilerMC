import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

		def test_101(self):
			input = r"""   
			int i;
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,101))
		def test_102(self):
			input = r"""   
			float i;
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,102))
		def test_103(self):
			input = r"""   
			string i;
			float abc;
			boolean array[1];

			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,103))
		def test_104(self):
			input = r"""   
			float a,c,b,d;
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,104))
		def test_105(self):
			input = r"""   
			string a,d[12],e[98];
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,105))
		def test_106(self):
			input = r"""   
			int main(){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,106))
		def test_107(self):
			input = r"""   
			float main(int x){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,107))
		def test_108(self):
			input = r"""   
			void foo(int i){
			int k;
			}

			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,108))
		def test_109(self):
			input = r"""   
			boolean hello(int foo[]){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,109))
		def test_110(self):
			input = r"""   
			string chuoi(int x){
			//statement
			x=chuoi[-1];
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,110))
		def test_111(self):
			input = r"""   
			void foo(float j[],int i){
			print(i);
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,111))
		def test_112(self):
			input = r"""   
			int main(){
			return k;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,112))
		def test_113(self):
			input = r"""   
			int main(){
			//this single-line comment 
			return k;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,113))
		def test_114(self):
			input = r"""   
			int main(){
			//this single-line comment /* a multi-line commment inside*/ 
			return k;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,114))
		def test_115(self):
			input = r"""   
			int main(){
			/* a multi-line commment 
			here
			ok	
			*/ 
			return k;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,115))
		def test_116(self):
			input = r"""   
			int main(){
			/* a multi-line commment 
			here // there is a single-line comment
			ok	
			*/ 
			return something;	
			}		
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,116))
		def test_117(self):
			input = r"""   
			int main(){
			// comment 1 // comment neseted // something
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,117))
		def test_118(self):
			input = r"""   
			void main(){
			/* hehee //cmt1 //cmt2 */
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,118))
		def test_119(self):
			input = r"""   
			void main(){
			5 + 4;
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,119))
		def test_120(self):
			input = r"""   
			boolean a[2];
			string a;
			boolean b[3],x;
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,120))
		def test_121(self):
			input = r"""   
			int x;
			int foo(){
			x=x+1;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,121))
		def test_122(self):
			input = r"""   
			boolean b;
			boolean foo(boolean k){
			k=b;
			return k==b;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,122))
		def test_123(self):
			input = r"""   
			void hello(){
			return hello(2);
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,123))
		def test_124(self):
			input = r"""   
			int main(){
			continue;
			return blackbi;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,124))
		def test_125(self):
			input = r"""   
			int main(){
			break;
			return blackbi;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,125))
		def test_126(self):
			input = r"""   
			
			void foo(){
			float x;
			x=1.23;
			int y;
			y=1e-3;
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,126))
		def test_127(self):
			input = r"""   
			
			void foo(){
			int k;
			k=foo[1];
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,127))
		def test_128(self):
			input = r"""   
			
			int foo(){
			string k;
			k="abd\n";
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,128))
		def test_129(self):
			input = r"""   
			int foo(){
			string k;
			k="abd\n,,,,,,,,,,";
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,129))
		def test_130(self):
			input = r"""   
			
			int foo(){
			string k;
			k="abd\n,,,,,,,,,,";//comnent
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,130))
		def test_131(self):
			input = r"""   
			void _func(){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,131))
		def test_132(self):
			input = r"""   
			float number;
			boolean check;
			int arr[4],num,brr[5];
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,132))
		def test_133(self):
			input = r"""   
			float number;
			float FUNC(float x){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,133))
		def test_134(self):
			input = r"""   
			
			int print(int k){
			int a;
			return a;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,134))
		def test_135(self):
			input = r"""   
			int data_1;
			void main(){
			foo(2);
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,135))
		def test_136(self):
			input = r"""   
			int print_sth(){
			x=1000.2e-10;
			return 1;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,136))
		def test_137(self):
			input = r"""   
			
			int _foo(int str[], float x){
				return -1;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,137))
		def test_138(self):
			input = r"""   
			int foo(){
			for(i=0;i<=8;i=i+1)
				data=data+1;
			return data;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,138))
		def test_139(self):
			input = r"""   
			
			int main(){
			for (i=1;i<0;i=i-2){

			x=2;
			}
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,139))
		def test_140(self):
			input = r"""   
			void main() { if(i>1) a; } 
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,140))
		def test_141(self):
			input = r"""   
			
			void main() { if(i>1) a=5; else {} } 
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,141))
		def test_142(self):
			input = r"""   
			
			void main() { if(!true) a=5; else {}}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,142))
		def test_143(self):
			input = r"""   
			void main() { if(!false +2) a=5; else {}}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,143))
		def test_144(self):
			input = r"""   
			
			void main() { if(5) a=5; else 3+2=f;}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,144))
		def test_145(self):
			input = r"""   
			void main(string k[]) { if(((true))) foo(0); else return 5;}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,145))
		def test_146(self):
			input = r"""   
			void main(string k[]) { if(!((true))) foo(0); else return 5;}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,146))
		def test_147(self):
			input = r"""   
			void main(string k[]) { if(!((true) * false)) foo(0)=a[7]; else return true;}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,147))
		def test_148(self):
			input = r"""  
			int main(){ 
			if(true) for (i=1;i<0;i=i-2){x=2;} else break;
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,148))
		def test_149(self):
			input = r"""   
			int main(){
			for (ID=200;i>0;i=i-1) if (5!=6) print("hello");
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,149))
		def test_150(self):
			input = r"""   
			
			int main(){
			for (ID=0;ID1>0;HELLO=9-1) if (1000==6) continue;
			}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,150))
		def test_151(self):
			input = r"""   
			int main(){
			break;
    		continue;
}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,151))
		def test_152(self):
			input = r"""   
			int main(){
    		a+b == c+d == e+f;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,152))
		def test_153(self):
			input = r"""   
			int main(){
		    a+b = c +d = e+-f;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,153))
		def test_154(self):
			input = r"""   
			
			int main(){
}
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,154))
		def test_155(self):
			input = r"""   
			int main(){
			__(__,__,__);
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,155))
		def test_156(self):
			input = r"""   
			int main(){
			__*__(_*_/*+_--_);
			}
			
			"""
			expect = "Error on line 3 col 13: *"
			self.assertTrue(TestParser.checkParser(input,expect,156))
		def test_157(self):
			input = r"""   
			int main(){
			_=_/a_/b_/__;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,157))
		def test_158(self):
			input = r"""   
			int main(){
			do{__(_);}{1+2;}{9+_;} while true;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,158))
		def test_159(self):
			input = r"""   
			
			int 1.e2(){
			1.e2+.1e2;
			}
			"""
			expect = "Error on line 3 col 7: 1.e2"
			self.assertTrue(TestParser.checkParser(input,expect,159))
		def test_160(self):
			input = r"""   
			int main(){
			int successful;
			successful = int;
			}
			
			"""
			expect = "Error on line 4 col 16: int"
			self.assertTrue(TestParser.checkParser(input,expect,160))
		def test_161(self):
			input = r"""   
			int main(){
			int Void;
			Void();
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,161))
		def test_162(self):
			input = r"""   
			int main(){
			int successful;
			successful = int;
			}
			
			"""
			expect = "Error on line 4 col 16: int"
			self.assertTrue(TestParser.checkParser(input,expect,162))
		def test_163(self):
			input = r"""   
			int Void(){
			int void;
			}
			
			"""
			expect = "Error on line 3 col 7: void"
			self.assertTrue(TestParser.checkParser(input,expect,163))
		def test_164(self):
			input = r"""   
			
			int main(){
			int "a";
			}
			"""
			expect = "Error on line 4 col 7: a"
			self.assertTrue(TestParser.checkParser(input,expect,164))
		def test_165(self):
			input = r"""   
			int main(){
			    if (main()){
			        main();
			    	}
			    else ((main()));
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,165))
		def test_166(self):
			input = r"""   
			int main(){
			class A(){
			    
			}
			}
			
			"""
			expect = "Error on line 3 col 9: A"
			self.assertTrue(TestParser.checkParser(input,expect,166))
		def test_167(self):
			input = r"""   
			int main(){
			class A(){
			    static int main(){}
			}
			}
			
			"""
			expect = "Error on line 3 col 9: A"
			self.assertTrue(TestParser.checkParser(input,expect,167))
		def test_168(self):
			input = r"""   
			float number;
            boolean check;
            float FLOAT_FUNC(int a){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,168))
		def test_169(self):
			input = r"""   
			float arr[10],number;
            boolean list[2],check;
            float test(int a, boolean list[], float brr[]){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,169))
		def test_170(self):
			input = r"""   
			int Date;
        	int PRINT(int a){
	            Date=9;
	            int i;
	            for(i=0;i<8;i=i+1)
	                Date=Date+1;
	            return 1;
	        }
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,170))
		def test_171(self):
			input = r"""   
			int PRINT(int a){
            Date=9;
            int i;
            for(i=0;i<8;i=i+1)
                Date=Date+1;
            return 1;
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,171))
		def test_172(self):
			input = r"""   
			void PRINT(int a){
            Date=9;
            int i;
            i=10;
            if(i>8)
                Date=Date+3;
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,172))
		def test_173(self):
			input = r"""   
			int date[31],month[12];
	        int Year(int month[], int date[]){}
	        boolean PRINT(int a){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,173))
		def test_174(self):
			input = r"""   
			boolean a;
	        boolean a[2];
	        string a;
	        boolean b[3];
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,174))
		def test_175(self):
			input = r"""   
			
			boolean abc__bc-ab(int c){

        	}
			"""
			expect = "Error on line 3 col 18: -"
			self.assertTrue(TestParser.checkParser(input,expect,175))
		def test_176(self):
			input = r"""   
	      	int abc(){}
	        boolean abc(){}
	        float[] abc(){}
	        void print(){}
	        int[] abc(){}
	        string low2up(){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,176))
		def test_177(self):
			input = r"""   
			
			
			"""
			expect = "Error on line 4 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,177))
		def test_178(self):
			input = r"""   
			int main(string arg[]){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,178))
		def test_179(self):
			input = r"""   
			void goo ( float x [ ] ) {
			    float y[ 10 ] ;
			    int z[ 10 ] ;
			    foo( x ) ;
			    foo( y ) ;
			    foo( z ) ;
			    return;
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,179))
		def test_180(self):
			input = r"""   
			boolean swap(int a, int b)
			{ 
			    int tmp;
			    tmp = a;
			    a = b;
			    b = tmp;
			    printf(a, b);
			    return true;
			}
			int main(){
			    int a,b;
			    boolean result;
			    result = swap(a,b);
			    print(result);
			}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,180))
		def test_181(self):
			input = r"""   
	        int a(int abc){}
        	float a(int a[]){}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,181))
		def test_182(self):
			input = r"""   
	        int float2int(float a){}
	        int a(int a[], int b, float c[], string d){}
	        float b(){}
	        int c(string c[], int a, int b){}
				
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,182))
		def test_183(self):
			input = r"""   
			int main(){}
	        int main()
				
			"""
			expect = "Error on line 5 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,183))
		def test_184(self):
			input = r"""   
	        int a;
	        float b;
	        boolean c;
	        string d
			
			"""
			expect = "Error on line 7 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,184))
		def test_185(self):
			input = r"""   
		    int a;
	        float b;
	        boolean c[];
				
			"""
			expect = "Error on line 4 col 19: ]"
			self.assertTrue(TestParser.checkParser(input,expect,185))
		def test_186(self):
			input = r"""   
			int a = b;
			
			"""
			expect = "Error on line 2 col 9: ="
			self.assertTrue(TestParser.checkParser(input,expect,186))
		def test_187(self):
			input = r"""   
			void foo(int a, float b[]){
            int c[3];
            if(a>0) foo(a-1,b);
            return ;
			
			"""
			expect = "Error on line 7 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,187))
		def test_188(self):
			input = r"""   
			string c(){
            s = a +b + c * d;
            d = a && b;
            e = !a;
			
			"""
			expect = "Error on line 7 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,188))
		def test_189(self):
			input = r"""   
			void foo(){
            if(false) return;
            else return 2;
			
			"""
			expect = "Error on line 6 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,189))
		def test_190(self):
			input = r"""   
			int[] foo(int b[]){
            int a[1];
            if (true) return a;
            else return b;
			
			"""
			expect = "Error on line 7 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,190))
		def test_191(self):
			input = r"""   
			int main(){
            if(a>c)
                if (!c) c+x;
                else d+s;
            else true;
			
			"""
			expect = "Error on line 8 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,191))
		def test_192(self):
			input = r"""   
			int foo(int  c[]){
            if (a==c)
                if (d=f)
                    if(lv=2) c=d;
                    else c = a[cc+9];
                else "disdsi/"/4;
            else sdji=7/3;
			
			"""
			expect = "Error on line 10 col 3: <EOF>"
			self.assertTrue(TestParser.checkParser(input,expect,192))
		def test_193(self):
			input = r"""   
			int main(){
            	foo(2)[3+x] = a[b[2]] + 3;
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,193))
		def test_194(self):
			input = r"""   
			string c(){
            	3[3+x] = true[b[2]] +3;
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,194))
		def test_195(self):
			input = r"""   
			int main(){
            	do a=c; d=5; do i=i+3;c+d; while c!=9; while a;
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,195))
		def test_196(self):
			input = r"""   
			int main(){
	            do{
	                a=c;
	                d=b;
	            }
	            {
	                a=a+4;
	                b>4;
	            }
	            while a!=b;
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,196))
		def test_197(self):
			input = r"""   
			int main(){
	            do{
	                a=c;
	                d=b;
	            }
	            {
	            }
	            while (a!=b);
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,197))
		def test_198(self):
			input = r"""   
			int main(){
            	for (true;(a);1) do {a=c;b=d;}{} while a;
        	}
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,198))
		def test_199(self):
			input = r"""   
			int main(){
            	for (true;(a);1) ;
        	}
			
			"""
			expect = "Error on line 3 col 30: ;"
			self.assertTrue(TestParser.checkParser(input,expect,199))
		def test_200(self):
			input = r"""   
	        int main(){
	            int ab;
	            {
	                {
	                    {
	                        {
	                            break;
	                        }
	                        break;
	                    }
	                    break;
	                }
	                break;
	            }
	        }
			
			"""
			expect = "successful"
			self.assertTrue(TestParser.checkParser(input,expect,200))