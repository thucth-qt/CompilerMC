import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

	def test_1(self):	
		self.assertTrue(TestLexer.checkLexeme( " //hello this is single-line comment" ,"<EOF>",1))

	def test_2(self):	
		self.assertTrue(TestLexer.checkLexeme( " /*this is\n multi-line comment*/  " ,"<EOF>",2))

	def test_3(self):	
		self.assertTrue(TestLexer.checkLexeme( " /* this is \n multi-line comment and  // a single-line comment inside */  " ,"<EOF>",3))

	def test_4(self):	
		self.assertTrue(TestLexer.checkLexeme( " //this is single-line comment, and /* a multi-line comment inside */  " ,"<EOF>",4))

	def test_5(self):	
		self.assertTrue(TestLexer.checkLexeme( " identifier  " ,"identifier,<EOF>",5))

	def test_6(self):	
		self.assertTrue(TestLexer.checkLexeme( " identifier123 " ,"identifier123,<EOF>",6))

	def test_7(self):	
		self.assertTrue(TestLexer.checkLexeme( " IdenTiFier123abc " ,"IdenTiFier123abc,<EOF>",7))

	def test_8(self):	
		self.assertTrue(TestLexer.checkLexeme( " _Id__123ab " ,"_Id__123ab,<EOF>",8))

	def test_9(self):	
		self.assertTrue(TestLexer.checkLexeme( " _123 " ,"_123,<EOF>",9))

	def test_10(self):	
		self.assertTrue(TestLexer.checkLexeme( " 123abc_ID " ,"123,abc_ID,<EOF>",10))

	def test_11(self):	
		self.assertTrue(TestLexer.checkLexeme( " boolean Id " ,"boolean,Id,<EOF>",11))

	def test_12(self):	
		self.assertTrue(TestLexer.checkLexeme( " __else_id 123while " ,"__else_id,123,while,<EOF>",12))

	def test_13(self):	
		self.assertTrue(TestLexer.checkLexeme( " a+b " ,"a,+,b,<EOF>",13))

	def test_14(self):	
		self.assertTrue(TestLexer.checkLexeme( " a_*b/d<=43*a " ,"a_,*,b,/,d,<=,43,*,a,<EOF>",14))

	def test_15(self):	
		self.assertTrue(TestLexer.checkLexeme( " a<==b " ,"a,<=,=,b,<EOF>",15))

	def test_16(self):	
		self.assertTrue(TestLexer.checkLexeme( " a;b " ,"a,;,b,<EOF>",16))

	def test_17(self):	
		self.assertTrue(TestLexer.checkLexeme( " [1,)};]  " ,"[,1,,,),},;,],<EOF>",17))

	def test_18(self):	
		self.assertTrue(TestLexer.checkLexeme( " something' " ,"something,Error Token '",18))

	def test_19(self):	
		self.assertTrue(TestLexer.checkLexeme( " 123456789 " ,"123456789,<EOF>",19))

	def test_20(self):	
		self.assertTrue(TestLexer.checkLexeme( " -123456789 " ,"-,123456789,<EOF>",20))

	def test_21(self):	
		self.assertTrue(TestLexer.checkLexeme( " 1. " ,"1.,<EOF>",21))

	def test_22(self):	
		self.assertTrue(TestLexer.checkLexeme( " .1 " ,".1,<EOF>",22))

	def test_23(self):	
		self.assertTrue(TestLexer.checkLexeme( " 1.1 " ,"1.1,<EOF>",23))

	def test_24(self):	
		self.assertTrue(TestLexer.checkLexeme( " 1e1 " ,"1e1,<EOF>",24))

	def test_25(self):	
		self.assertTrue(TestLexer.checkLexeme( " 1e " ,"1,e,<EOF>",25))

	def test_26(self):	
		self.assertTrue(TestLexer.checkLexeme( " 0e5 " ,"0e5,<EOF>",26))

	def test_27(self):	
		self.assertTrue(TestLexer.checkLexeme( " 000.0e-1 " ,"000.0e-1,<EOF>",27))

	def test_28(self):	
		self.assertTrue(TestLexer.checkLexeme( " 1.2E9 " ,"1.2E9,<EOF>",28))

	def test_29(self):	
		self.assertTrue(TestLexer.checkLexeme( " 128e-42 " ,"128e-42,<EOF>",29))

	def test_30(self):	
		self.assertTrue(TestLexer.checkLexeme( " true 123false " ,"true,123,false,<EOF>",30))

	def test_31(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "this is a legal string" """ ,"this is a legal string,<EOF>",31))

	def test_32(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "unclosed string """ ,"Unclosed String: unclosed string ",32))

	def test_33(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "unclosed string\n with newline character" """ ,"Unclosed String: unclosed string",33))

	def test_34(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "illegal escape\\x string" """ ,"Illegal Escape In String: illegal escape\\x",34))

	def test_35(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "string accept legal escape charater\\n \\b" """ ,"string accept legal escape charater\\n \\b,<EOF>",35))

	def test_36(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "string1""string2" """ ,"string1,string2,<EOF>",36))

	def test_37(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "string and \\\\ comment" """ ,"string and \\\\ comment,<EOF>",37))

	def test_38(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "string"" """ ,"string,Unclosed String:  ",38))

	def test_39(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "hello \\ " """ ,"Illegal Escape In String: hello \\ ",39))

	def test_40(self):	
		self.assertTrue(TestLexer.checkLexeme(""" "hello" """"" " ""","""hello,<EOF>""",40))

	def test_41(self):	
		self.assertTrue(TestLexer.checkLexeme(""" "" " """,""",Unclosed String:  """,41))

	def test_42(self):	
		self.assertTrue(TestLexer.checkLexeme(r""""hello lexer \t \b \n \""  asdf """,r"""hello lexer \t \b \n \",asdf,<EOF>""",42))

	def test_43(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "hello""""""" "hello " ""","hello,hello ,<EOF>",43))

	def test_44(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"Backspace  \b"
"Formfeed   \f"
"Return     \r"
"Newline    \n"
"Tab        \t"
"Double quote       \""
"Backslash  \\ "
			""",

			r"""Backspace  \b,Formfeed   \f,Return     \r,Newline    \n,Tab        \t,Double quote       \",Backslash  \\ ,<EOF>""",
			44
		))

	def test_45(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"Newline
	multiple lines
"           
			""",

			r"""Unclosed String: Newline""",
			45
		))

	def test_46(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
" Hi Hi \c \d "
			""",

			"Illegal Escape In String:  Hi Hi \c",
			46
		))

	def test_47(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"abc - xyz"
"abc \yyz"
			""",

			"abc - xyz,Illegal Escape In String: abc \y",
			47
		))

	def test_48(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int float string void true false boolean if else for do while break continue return  
			""",
			"int,float,string,void,true,false,boolean,if,else,for,do,while,break,continue,return,<EOF>",
			48
		))
	def test_49(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "hello"""""" "hello " ""","hello ,hello,Unclosed String:  ",49))

	def test_50(self):	
		self.assertTrue(TestLexer.checkLexeme( r""" "hello "hi " """ ,"hello ,hi,Unclosed String:  ",50))

	def test_51(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "a\nb" """ ,"Unclosed String: a",51))

	def test_52(self):	
		self.assertTrue(TestLexer.checkLexeme( """ "space at the end of sentences """ ,"Unclosed String: space at the end of sentences ",52))

	def test_53(self):	
		self.assertTrue(TestLexer.checkLexeme(
			""" 
			"a""b""c"
			""",
			"a,b,c,<EOF>",
			53
		))

	def test_54(self):
		self.assertTrue(TestLexer.checkLexeme(
			""" 
			"a""b""c"
			""",
			"a,b,c,<EOF>",
			54
		))

	def test_55(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
		(foo)(3)
			""",
			r"""(,foo,),(,3,),<EOF>""",
			55
		))
	def test_56(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int fibonacci (int n)  
{
	if (n==0)
		return 0;
	if (n == 1)   
		return 1;
	else  
		return fibonacci(n-1)+fibonacci(n-2);
}  
			""",
			r"""int,fibonacci,(,int,n,),{,if,(,n,==,0,),return,0,;,if,(,n,==,1,),return,1,;,else,return,fibonacci,(,n,-,1,),+,fibonacci,(,n,-,2,),;,},<EOF>""",
			56
		))

	def test_57(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int main()
{
	printf("\n\n\t\tLexer - Best place to practice\n\n\n");
	int num;
	printf("\nHello world!\nWelcome to Lexer: Best place to practice\n");
	printf("\n\n\t\t\tCoding is Fun !\n\n\n");
	return 0;
}
			""",
			r"""int,main,(,),{,printf,(,\n\n\t\tLexer - Best place to practice\n\n\n,),;,int,num,;,printf,(,\nHello world!\nWelcome to Lexer: Best place to practice\n,),;,printf,(,\n\n\t\t\tCoding is Fun !\n\n\n,),;,return,0,;,},<EOF>""",
			57
		))

	def test_58(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
for (i = 0; i < 10; i = i + 1) {
  if (i == 4)
	continue;
  print("%d\n", i);
}
			""",
			r"""for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,if,(,i,==,4,),continue,;,print,(,%d\n,,,i,),;,},<EOF>""",
			58
		))

	def test_59(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int time = 22;
if (time < 10)
	print("Good morning.");
if (time < 20) {
	print("Good day.");
else
	print("Good evening.");
// Outputs "Good evening."
			""",

			r"int,time,=,22,;,if,(,time,<,10,),print,(,Good morning.,),;,if,(,time,<,20,),{,print,(,Good day.,),;,else,print,(,Good evening.,),;,<EOF>",
			59
		))

	def test_60(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int i = 0;
do
  print("\n");
  i++;
while (i < 5);
			""",

			r"int,i,=,0,;,do,print,(,\n,),;,i,+,+,;,while,(,i,<,5,),;,<EOF>",
			60
		)) 

	def test_61(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int main()
{
  int x;
 
  printf("Input an integer\n");
  scanf("%d", &x); // %d is used for an integer
 
  printf("The integer is: %d\n", x);
 
  return 0;
}
			"""
		, r"int,main,(,),{,int,x,;,printf,(,Input an integer\n,),;,scanf,(,%d,,,Error Token &"
		, 61
		))

	def test_62(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int plusFuncInt(int x, int y) {
  return x + y;
}

double plusFuncDouble(double x, double y) {
  return x + y;
}
			""",

			r"int,plusFuncInt,(,int,x,,,int,y,),{,return,x,+,y,;,},double,plusFuncDouble,(,double,x,,,double,y,),{,return,x,+,y,;,},<EOF>",
			62
		))

	def test_63(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int sum(int num1, int num2){
   int num3 = num1+num2;
   return num3;
}
			""",

			r"int,sum,(,int,num1,,,int,num2,),{,int,num3,=,num1,+,num2,;,return,num3,;,},<EOF>",
			63
		))


	def test_64(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
float a, b, c;
boolean x, y, z;
int g, h, y;
float nty();
int x, y, z;
int q, w;
string a; 
	/*
		=======================================
		Comment here
		=======================================
	*/
""",

			r"float,a,,,b,,,c,;,boolean,x,,,y,,,z,;,int,g,,,h,,,y,;,float,nty,(,),;,int,x,,,y,,,z,;,int,q,,,w,;,string,a,;,<EOF>",
			64
		))
	def test_65(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"abc\mabc"
			""",

			r"""Illegal Escape In String: abc\m""",
			65
		))

	def test_66(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
s = "string          '
"a = 4
g = 9
			""",

			r"""s,=,Unclosed String: string          '""",
			66
		))

	def test_67(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"\"abc
			""",

			r"""Unclosed String: \"abc""",
			67
		))

	def test_68(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
00001.1101010101000
0e-432
000000001e-542400
000313121.e00031321132
			""",

			"00001.1101010101000,0e-432,000000001e-542400,000313121.e00031321132,<EOF>",
			68
		))

	def test_69(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
1234 00003132234 00002132123
			""",

			"1234,00003132234,00002132123,<EOF>",
			69
		))

	def test_70(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
abc#
			""",

			"abc,Error Token #",
			70
		))

	def test_71(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
$a = 5
			""",

			"Error Token $",
			71
		))

	def test_72(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
a = a & 1
			""",

			"a,=,a,Error Token &",
			72
		))

	def test_73(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
!== != & ^ % $ # ... \
			""",

			"!=,=,!=,Error Token &",
			73
		))

	def test_74(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
int float string void true false boolean if else for do while break continue return  
			""",
			"int,float,string,void,true,false,boolean,if,else,for,do,while,break,continue,return,<EOF>",
			74
		))

	def test_75(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"abc - xyz"
"abc \yyz"
			""",

			"abc - xyz,Illegal Escape In String: abc \y",
			75
		))

	def test_76(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"abc - xyz"
"abc \ xyz"
			""",

			"abc - xyz,Illegal Escape In String: abc \ ",
			76
		))

	def test_77(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
" Hi Hi \s\d\\f "
			""",

			"Illegal Escape In String:  Hi Hi \s",
			77
		)) 

	def test_78(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
" Hi Hi \c \d "
			""",

			"Illegal Escape In String:  Hi Hi \c",
			78
		))

	def test_79(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
Illegal"\a"
""",

			r"""Illegal,Illegal Escape In String: \a""",
			79
		))

	def test_80(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"Newline
	multiple lines
"           
			""",

			r"""Unclosed String: Newline""",
			80
		))

	def test_81(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
"Backspace  \b"
"Formfeed   \f"
"Return     \r"
"Newline    \n"
"Tab        \t"
"Double quote       \""
"Backslash  \\ "
			""",

			r"""Backspace  \b,Formfeed   \f,Return     \r,Newline    \n,Tab        \t,Double quote       \",Backslash  \\ ,<EOF>""",
			81
		))

	def test_82(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
" hello lexer \t \b \n \""     asdf 
""",

			r""" hello lexer \t \b \n \",asdf,<EOF>""",
			82
		))

	def test_83(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
" abc \n xyz "
" abc \\n xyz "
""",

			r""" abc \n xyz , abc \\n xyz ,<EOF>""",
			83
		))

	def test_84(self):	
		self.assertTrue(TestLexer.checkLexeme(
			""" 
" hello lexer
			""",

			"Unclosed String:  hello lexer",
			84
		))

	def test_85(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
e-12 e12 1e 12e 12.05e .05e ee e01 .
""",

			"e,-,12,e12,1,e,12,e,12.05,e,.05,e,ee,e01,Error Token .",
			85
		)) 

	def test_86(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
""
12 32.43 43.E12 4e-1 true "false" false "012" 1.32 1. .0
"String"
			""",

			",12,32.43,43.E12,4e-1,true,false,false,012,1.32,1.,.0,String,<EOF>",
			86
		))

	def test_87(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
""
"String"
" "
"?"
"-"
"#"
"Mulitiple Characters"
			""",

			",String, ,?,-,#,Mulitiple Characters,<EOF>",
			87
		))

	def test_88(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
			""",

			"1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
			88
		))

	def test_89(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
true false
			""",

			"true,false,<EOF>",
			89
		))  

	def test_90(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
0 1 2 3 4 123 123456789 001 0x123
			""",

			"0,1,2,3,4,123,123456789,001,0,x123,<EOF>",
			90
		))

	def test_91(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
// inline comment \b \t
	is multiple lines
// inline comment
""",

			"is,multiple,lines,<EOF>",
			91
		))

	def test_92(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
/* This is a block comment */
// This is a line comment
/* Comment with multiple lines
	Hello comments
*/
/*
	Comment multiple lines
*/
/* nest comments
	// inline comment 
// inline comment
*/
			""",

			"<EOF>",
			92
		))

	def test_93(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
/* Comment with multiple lines
	Hello comments
	This is block comment
*/
			""",

			"<EOF>",
			93
		))

	def test_94(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
123abc 123_abc 00000123_123abc
			""",

			"123,abc,123,_abc,00000123,_123abc,<EOF>",
			94
		))
	def test_95(self):
		self.assertTrue(TestLexer.checkLexeme(
			r"""
// inline comment  
// This is inline comment
			""",
			"<EOF>",
			95
		))
	def test_96(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
id-1 id&1  
			""",
			"id,-,1,id,Error Token &",
			96
		))

	def test_97(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
_ _abc _123 _abc123 _abc_123 _123_abc
__ ____ ____123____
abc ABC aBC Abc _ABC __ABc __123ABc
hdad_adsajdk_hf__T_
			""",

			"a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,hdad_adsajdk_hf__T_,<EOF>",
			97
		))

	def test_98(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
id boolean_id float_id int_id string_id void_id 
			""",
			"id,boolean_id,float_id,int_id,string_id,void_id,<EOF>",
			98
		))

	def test_99(self):	
		self.assertTrue(TestLexer.checkLexeme(
			r"""
id ID _id 89id 89ID 89_id
			""",
			"id,ID,_id,89,id,89,ID,89,_id,<EOF>",
			99
		))

	def test_100(self):	
		self.assertTrue(TestLexer.checkLexeme( r"""
void testLexer(){
	string x;
	x = "this is a string";//for check string;
	x=a*c-(3-z)/0+"this is a string";
}
			""" ,"void,testLexer,(,),{,string,x,;,x,=,this is a string,;,x,=,a,*,c,-,(,3,-,z,),/,0,+,this is a string,;,},<EOF>",100))
	