/*
Họ và tên: Trần Hữu Thức
MSSV: 1713454
*/

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}

//PROGRAM STRUCT

program  	: many_decs EOF ;

many_decs	: dec many_decs|dec;

dec 		: var_dec|func_dec;

//Variable declaration:

var_dec	: primtype list_var SM;

list_var: ID (LQ INTLIT RQ)? CM list_var|ID (LQ INTLIT RQ)?;

primtype: INT|FLOAT|BOOLEAN|STRING;

//Function declaration:

func_dec: types ID LB list_para? RB block_stmt;

types: primtype|pointertype|VOID;

pointertype: primtype LQ RQ;

list_para: para_dec CM list_para|para_dec;

para_dec: primtype ID (LQ RQ)?;

// Statement:

block_stmt: LP (var_dec|stmt)* RP; 

stmt: if_stmt|for_stmt|while_stmt|break_stmt|continue_stmt|return_stmt|exp_stmt|block_stmt;

if_stmt: IF LB exp RB stmt (ELSE stmt)?;

while_stmt: DO stmt+ WHILE exp SM;

for_stmt: FOR LB exp SM exp SM exp RB stmt;

break_stmt: BREAK SM;

continue_stmt: CONTINUE SM;

return_stmt: RETURN exp? SM;

exp_stmt: exp SM;


exp : operand
    | exp LQ exp RQ                         //element of array
	| operand LQ exp RQ								// associative: none 
	| <assoc=right> (SUB|NOT)  exp
	| exp (DIV|MUL|MODULE) exp
	| exp (ADD|SUB) exp
	| operand (LSS|LSSEQ|GRR|GRREQ) operand 		// associative: none 
	| operand (EQ|NEQ) operand 						// associative: none 
	| exp AND exp
	| exp OR exp
	| <assoc=right> exp ASN exp
	;
terminated_tok: (INTLIT|FLOATLIT|STRINGLIT|BOOLIT|ID);

func_call: ID LB (exp (CM exp)*)? RB;

element_of_array: (terminated_tok|LB exp RB|func_call) LQ exp RQ;

operand: terminated_tok| element_of_array|func_call| LB exp RB; //phai them subexp o day


//Characters:

WS		: [ \t\f\r\n]+ -> skip; //khac voi Escape Characters duoi

	fragment ESCAPE 	: '\\' [rnfbt"\\]; // mieu ta: \r \\ \b \"  trong python, c++...


COMMENTS: '/*' .*? '*/' ->skip;

COMMENT : '//' ~[\r\n]* ->skip;


// Token Set:

// Keywords: truoc ID

BOOLEAN	: 'boolean';

BREAK	: 'break';

CONTINUE: 'continue';

IF 		: 'if';

ELSE    : 'else';

FOR 	: 'for';

FLOAT	: 'float';

INT		: 'int';

STRING 	: 'string';

RETURN 	: 'return';

VOID 	: 'void';

DO		: 'do';

WHILE 	: 'while';

	fragment TRUE 	: 'true';

	fragment FALSE	: 'false';

// ID phai sau Keyword

ID		: (Letter|'_') (Letter|Digit|'_')*;

	fragment Letter	: [a-zA-Z];

	fragment Digit 	: [0-9];

// Operators:

ADD		: '+';

SUB		: '-';

MUL		: '*';

DIV		: '/';

NOT		: '!';

MODULE	: '%';

OR 		: '||';

AND		: '&&';

NEQ		: '==';

EQ		: '!=';

LSS		: '<';

GRR 	: '>';

LSSEQ	: '<=';

GRREQ	: '>=';

ASN		: '=';

// Seperators:

LB		: '(';

RB		: ')';

LP		: '{';

RP		: '}';

LQ 		: '[';

RQ		: ']';

SM 		: ';';

CM 		: ',';

// Literals:

INTLIT	: Digit+;
//float viet sau intlit vi 123 se nhan intlit truoc
FLOATLIT: Digit* '.'? Digit+ Exponent?
		| Digit+ '.'? Digit* Exponent?
		;

	fragment Exponent: ('e'|'E') '-'? Digit+;

BOOLIT 	: TRUE | FALSE;
// thắc mắc 1: ví dụ với input :  "abc""def" thì lexer cần phải recog ra cái gì???
//thắc mắc 2: nếu ở trên recog ra string1: abc, string2: def thì với input "abc"def" sẽ ra cái gì???
// string lit này k chấp nhận có dấu " trong chuỗi, chỉ chấp nhập dấu \" trong chuỗi.
STRINGLIT	: '"' (~[\b\r\n\f\t"\\] |ESCAPE)* '"'
				{
					temp = str(self.text)
					self.text = temp[1:-1]
				}
				;
// chú ý: ~["]* không bao gồm \", vì thiếu " nên ko tạo được \" => add thêm escaped vô
UNCLOSE_STRING	: '"' (~["]|ESCAPE)*? ([\r\n\f]|EOF)
				{	
					newline = ['\r','\n','\f'] 
					if (self.text[-1] in newline):
						self.text=self.text[1:-1]
					else:
						self.text= self.text[1:]

				}
				;
ILLEGAL_ESCAPE	: '"' (~[\b\r\n\f\t"\\] |ESCAPE)*?'\\' ~[rnfbt"\\] // không cần xác định chuỗi closed rồi mới xác định illegal_escape do unclosed đã được recog ở luật kế trên
				{
					temp = str(self.text)
					self.text = temp[1:]
				}
				;

ERROR_CHAR: .;

