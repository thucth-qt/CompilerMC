"""
* MSSV: 1713454
"""
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import*
from copy import deepcopy


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'MType(['+','.join(str(x) for x in self.partype )+ '],'+str(self.rettype)+')'
class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol("'+self.name+'",'+str(self.mtype) +', '+str(self.value) +')'
@dataclass  # automatically init
#contain some utils for general purposes
class CheckUtils:
    @staticmethod
    def checkRedeclared(self, id: str, kind: Kind, env: list):
        if id in env:
            raise Redeclared(kind, id)
        else:
            return False
    #function check if two objects are of same class
    #mode = 0: 1 direction (int -> float: true)
    #mode = 1: 2 direction (int ->float : false)
    @staticmethod
    def checkCompatible(src,dest,mode=0):
        if mode ==1:
            if type(src) is type(dest):
                if isinstance(src,(ArrayType,ArrayPointerType)):
                    return type(src.eleType) is type(dest.eleType)
                else: return True
            else: return False
        elif mode ==0:
            if type(src) is type(dest):
                if isinstance(src,(ArrayType,ArrayPointerType)):
                    return type(src.eleType) is type(dest.eleType)
                else: return True
            elif isinstance(src,IntType) and isinstance(dest,FloatType):
                return True
            elif isinstance(src,ArrayType) and isinstance(dest,ArrayPointerType):
                return type(src.eleType) is type(dest.eleType)
            else: return False
        else: 
            raise Exception("error in CheckCompatible()")
    
    @staticmethod
    #this method is to visit stmt
    def visitElement(checker,ast,envi,info):
        
        # CheckUtils.Print(envi)
        # print("ast: "+str(ast))
        isTerminal=[False,False] #isreturn , isBreak/continue
        if ast is None: return isTerminal
        if isinstance(ast,Block):
            envi.append([("block",info)])
            isTerminal=checker.visit(ast,envi)
            envi.pop()
        else:
            isTerminal=checker.visit(ast,envi)
        return isTerminal
 
    @staticmethod
    def isInLoop(envi):
        for x in envi[2:][::-1]:
            if x[0][0] in ("for","while"): return True
        return False

defaultValue=0
class StaticChecker(BaseVisitor, Utils):

    #Initial global_evi with built-in functions of MC Parser
    built_in = [[
        ("outermost",),
        Symbol("getInt", MType([], IntType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType()))
    ]]

    def __init__(self, ast):
        self.ast = ast
        self.unreachableFunc=[]

    def check(self):
        return self.visit(self.ast, StaticChecker.built_in)
    #return an entire global_envi
    def visitProgram(self, ast:Program, builtIn):
        #copy built-in into global_envi
        global_envi=deepcopy(builtIn)

        #create global_envi first:
        for x in ast.decl:
            if isinstance(x,VarDecl): #vardecl
                if self.lookup(x.variable, global_envi[0][1:], lambda x: x.name) is not None:
                    raise Redeclared(Variable(),x.variable)
                else:
                    global_envi[0].append(Symbol(x.variable,x.varType,defaultValue))
                
            else: #funcdecl

                if self.lookup(x.name.name,global_envi[0][1:],lambda x: x.name) is not None:
                    raise Redeclared(Function(),x.name.name)
                else:
                    paramType=[y.varType for y in x.param]
                    global_envi[0].append(Symbol(x.name.name,MType(paramType,x.returnType)))
                    if x.name.name!="main":
                        self.unreachableFunc.append(x.name.name)

        #check entry point:
        mainFunc=self.lookup("main",global_envi[0][1:],lambda x:x.name) 
        if mainFunc is None:
            raise NoEntryPoint()
        elif not isinstance(mainFunc.mtype,MType):
            raise NoEntryPoint()


        #visit every FuncDecl: 
        for x in ast.decl:
            if isinstance(x,FuncDecl):
                self.visit(x, global_envi)
        #check unreachable functon:
        if len(self.unreachableFunc)>0:
            raise UnreachableFunction(self.unreachableFunc[0])

       
        
    def visitFuncDecl(self, ast:FuncDecl, envi):

        #add local envi
        paramType=[y.varType for y in ast.param]
        # add symbol of current function for checking Return stmt, like: [global envi] [current function is visiting,local envi] ...
        envi.append([Symbol(ast.name.name,MType(paramType,ast.returnType))]) 
        #check parameters

        for x in ast.param:
            if self.lookup(x.variable, envi[-1][1:], lambda y: y.name) is not None:
                raise Redeclared(Parameter(),x.variable)
            else:
                envi[-1].append(Symbol(x.variable,x.varType,defaultValue))

        isReturn=False
        if self.visit(ast.body,envi)[0] is True: isReturn=True # <isReturn>, <isBreak/Continue>
        envi.pop()
        if not isinstance(ast.returnType,VoidType) and not isReturn: raise FunctionNotReturn(ast.name.name)

    def visitVarDecl(self, ast:VarDecl, envi):
        #here we just visit vardecl in function
        if self.lookup(ast.variable, envi[-1][1:], lambda x: x.name) is not None:
            raise Redeclared(Variable(),ast.variable)
        else:
            envi[-1].append(Symbol(ast.variable,ast.varType))

    def visitDowhile(self, ast, envi):
        isTerminal = [False,False] # <isReturn>, <isBreak/Continue>
  
        envi.append([["while"]])
        for x in ast.sl:
            if True in isTerminal:
                raise UnreachableStatement(x)
            checkTerminal=CheckUtils.visitElement(self,x,envi,"while")
            if type(checkTerminal)==list:
                if checkTerminal[0] is True: isTerminal[0]=True
                if True in checkTerminal : isTerminal[1]=True # 1 return 2 break -> [false,true] để có thể terminal cho vòng lặp, mạnh(return) + yếu(break/continue) -> yếu (break/continue)
        envi.pop()
        exprType=self.visit(ast.exp,envi)
        if not isinstance(exprType[0],BoolType): raise TypeMismatchInStatement(ast)
        return isTerminal
    #envi[1] is element contains current function visited
    def visitReturn(self, ast:Return, envi):
        FuncRetType= envi[1][0].mtype.rettype
        #case: ast.expr = None
        if ast.expr is None:
            if not isinstance(FuncRetType, VoidType):
                raise TypeMismatchInStatement(ast)
        else: 
        #case: ast.expr != None
            ExpType = self.visit(ast.expr,envi)

            if not CheckUtils.checkCompatible(ExpType[0],FuncRetType):
                raise TypeMismatchInStatement(ast)
        #has Return stmt
        return [True,False]       
    
    def visitContinue(self, ast, envi):
        for x in envi[2:][::-1]:
            if x[0][0] in ("for","while"):  return [False,True]  
        raise ContinueNotInLoop()

    def visitBreak(self, ast, envi):

        for x in envi[2:][::-1]:
            if x[0][0] in ("for","while"):  return [False,True]  
        raise BreakNotInLoop()

    def visitFor(self, ast:For, envi):
        envi.append([["for"]])
        expr1Type=self.visit(ast.expr1,envi)
        if not isinstance(expr1Type[0],IntType): raise TypeMismatchInStatement(ast)
        expr2Type=self.visit(ast.expr2,envi)
        if not isinstance(expr2Type[0],BoolType): raise TypeMismatchInStatement(ast)
        expr3Type=self.visit(ast.expr3,envi)
        if not isinstance(expr3Type[0],IntType): raise TypeMismatchInStatement(ast)
        Temp=CheckUtils.visitElement(self,ast.loop,envi,"for")
        mixEnvi=reduce(lambda  x,y:x+y[1:], envi,[])
        for x in envi[-1][0][1:]:# delete value initialized in for 
            y=self.lookup(x,mixEnvi[::-1],lambda z:z.name)
            if y is not None:
                y.value=None
        envi.pop()
        if type(Temp) is list:
            return [False,Temp[1]] # return in For loop is ignored

    def visitIf(self, ast:If, envi):
        envi.append([["if"]])
        #check expr
        exprType=self.visit(ast.expr,envi)
        if not isinstance(exprType[0],BoolType): 
            raise TypeMismatchInStatement(ast)
        #visit thenStmt and elseStmt
        envi.append([["then"]])
        isTerminal1= CheckUtils.visitElement(self,ast.thenStmt,envi,"then")
        envi.pop()
        envi.append([["else"]])
        isTerminal2= CheckUtils.visitElement(self,ast.elseStmt,envi,"else")   
        envi.pop()
        isTerminal=[False,False]
        isTerminal[0]=isTerminal1[0] and isTerminal2[0]
        isTerminal[1] = (isTerminal1[0] or isTerminal1[1]) and(isTerminal2[0] or isTerminal2[1]) 

        mixEnvi=reduce(lambda  x,y:x+y[1:], envi,[])
        for x in envi[-1][0][1:]:# delete value initialized in for 
            y=self.lookup(x,mixEnvi[::-1],lambda z:z.name)
            if y is not None:
                y.value=None
        envi.pop()
        return isTerminal

    def visitBlock(self, ast, envi):
        isTerminal =[False,False]
        if CheckUtils.isInLoop(envi):
            for x in ast.member:
                if (True in isTerminal) and isinstance(x,AST.Stmt): raise UnreachableStatement(x)
                checkTerminal=CheckUtils.visitElement(self,x,envi,"block")
                if type(checkTerminal)==list:
                    #if checkTerminal[0] or checkTerminal[1] is True: isTerminal[1] =True
                    isTerminal[1] = True in checkTerminal
                    isTerminal[0] = False #DO NOT CONSIDER VALUE OF EXPRESSION IN LOOP, SO  RETURN IN LOOP IS IGNORED

        else:

            for x in ast.member:
                if isTerminal[0] and isinstance(x,AST.Stmt): raise UnreachableStatement(x)
                checkTerminal=CheckUtils.visitElement(self,x,envi,"block")
                if type(checkTerminal)==list:
                    if checkTerminal[0] is True: isTerminal[0] =True
        return isTerminal
# literal: abstract


    def visitBooleanLiteral(self, ast, c):
        return BoolType(), True, ast.value

    def visitStringLiteral(self, ast, c):
        return StringType(), True, ast.value

    def visitFloatLiteral(self, ast, c):
        return FloatType(), True,ast.value

    def visitIntLiteral(self, ast, c):
        return IntType(), True, ast.value

    def visitCallExpr(self, ast:CallExpr, envi):

    #check undeclared function, except envi[1] is current dupplicated function 
        mixEnvi= reduce(lambda x,y:x+y[1:],envi,[])
        CallExprSymbol=self.lookup(ast.method.name,mixEnvi[::-1],lambda x:x.name )
        
        if CallExprSymbol is None:
            raise Undeclared(Function(),ast.method.name)
        if not isinstance(CallExprSymbol.mtype,MType): #avoid lookup return a variable
            raise TypeMismatchInExpression(ast)
    #mark this funciton that called (delete this function name in unreachable func list)
        if (CallExprSymbol.name in self.unreachableFunc) and (CallExprSymbol.name!= envi[1][0].name): #just delete 1 time
            self.unreachableFunc.remove(CallExprSymbol.name)

    #check mismatch parameter 
        if not isinstance(CallExprSymbol.mtype,MType) or len(ast.param) != len(CallExprSymbol.mtype.partype):
            raise TypeMismatchInExpression(ast)
        for i in range(len(ast.param)):
            thisParaType=self.visit(ast.param[i],envi)
            if not CheckUtils.checkCompatible(thisParaType[0],CallExprSymbol.mtype.partype[i]): 
                raise TypeMismatchInExpression(ast)

    #return type for later checking
        return CallExprSymbol.mtype.rettype, False, None #<type> <isConstant>

    def visitUnaryOp(self, ast:UnaryOp, envi):
    #check inside UnaryOp    
    #return Type for later check 
   
        bodyType=self.visit(ast.body,envi) #<type> <isConstant> <value>
        expression=ast.op+str(bodyType[2])
        try:
            result=eval(expression)
        except:
            result = None
        if ast.op =='!' and isinstance(bodyType[0],BoolType):
            return BoolType(), bodyType[1],result
        if ast.op =='-' and isinstance(bodyType[0],(IntType,FloatType)):
            return bodyType[0],bodyType[1],result
        raise TypeMismatchInExpression(ast)

    def visitBinaryOp(self, ast:BinaryOp, envi):

        assignOp =['=']
        boolOp=['==', '!=', '!', '&&', '||']
        intOp1=['+', '-', '*', '/', '%']
        intOp2=[ '<', '<=', '>', '>=', '==', '!=' ]
        floatOp1=[ '+', '-', '*', '/']
        floatOp2=['<', '<=', '>' , '>=' ]
       
        
        right=self.visit(ast.right,envi)
        # initialize for variable: in for / dowhile / if (not else) not consider initialized
        if ast.op in assignOp:
            mixEnvi= reduce(lambda x,y:x+y[1:],envi,[])
            if isinstance(ast.left,Id): # i =5+6, consider array cell A[10] there is only 1 value eg, A[10]= {x} 
                idLHS=self.lookup(ast.left.name,mixEnvi[::-1],lambda x:x.name)
                if idLHS is not None:
                    if idLHS.value is None:
                        idLHS.value=defaultValue
                        for x in list(range(2,len(envi)))[::-1]:
                            if envi[x][0][0] in ("for", "while"):
                                envi[x][0].append(idLHS.name)
                            elif envi[x][0][0] =="if":
                                if len(envi)>x+1:
                                    if envi[x+1][0][0]=="then":
                                        envi[x][0].append(idLHS.name)
                    else:
                         for x in list(range(2,len(envi)))[::-1]:
                            if envi[x][0][0] =="if":
                                if len(envi)>x+1:
                                    if envi[x+1][0][0] =="else" and (idLHS.name in envi[x][0]):
                                        envi[x][0].remove(idLHS.name)

        left=self.visit(ast.left,envi)

        isConstant= left[1] and right[1]
        expression= str(left[2])+ast.op+str(right[2])

        try:
            result=eval(expression);
        except :
            result=None

       
    #check assign Op
        if ast.op in assignOp:
    
            #check not left value:
            if not isinstance(ast.left,(Id,ArrayCell)):
                raise NotLeftValue(ast.left) 
            #LHS is not void type, array type, array pointer type
            if isinstance(left[0],(VoidType,ArrayType,ArrayPointerType)):
                raise TypeMismatchInExpression(ast)

            if CheckUtils.checkCompatible(right[0],left[0]):
                return left[0],isConstant, result          
    
    #check other Ops:
        #check bool exp:
        if isinstance(left[0],BoolType) and isinstance(right[0],BoolType):
            if ast.op  in boolOp:
                return BoolType(), isConstant, result
    
        #check int exp:
        if isinstance(left[0],IntType) and isinstance(right[0],IntType):
            if ast.op in intOp1:
                if ast.op=='/' and type(eval(str(left[2]))) is int and type(eval(str(right[2]))) :
                    expression= str(left[2])+"//"+str(right[2])
                try:
                    result=eval(expression);
                except :
                    result=None
                return IntType(), isConstant, result
            if ast.op in intOp2:
                return BoolType(), isConstant, result

        #check float exp:
        if isinstance(left[0],(IntType,FloatType)) and isinstance(right[0],(IntType,FloatType)):
            if isinstance(left[0],FloatType) or isinstance(right[0],FloatType):
                if ast.op in floatOp1:
                    return FloatType(), isConstant, result
                if ast.op in floatOp2:
                    return BoolType(), isConstant, result

        #check string exp: in "check assign Op" on the top
        raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast:ArrayCell, envi):
       
    # arrayCell: a[i] or foo(..)[i] support i is integer exp, a is name of variable of ArrType|ArrPorterType, foo(): return type of ArrayPointerType
    #check mismatch inside of ArrayCell
        arrType=self.visit(ast.arr,envi)
        idxType=self.visit(ast.idx,envi)

        if not isinstance(arrType[0],(ArrayType,ArrayPointerType)):
            raise TypeMismatchInExpression(ast)
        if not isinstance(idxType[0],IntType):
            raise TypeMismatchInExpression(ast)

    #get value of index expression
        valueIndexExpr = idxType[2]
        isConstant = idxType[1]   
    #return Type for later checking mismatch in Expr
        mixEnvi= reduce(lambda x,y:x+y[1:],envi,[])
        # a[i]: with a is ArrayType or ArrayPointerType
        if isinstance(ast.arr,Id):
            arraySymbol=self.lookup(ast.arr.name,mixEnvi[::-1],lambda x:x.name)
            if arraySymbol is None:
                raise Undeclared(Identifier(),ast.arr.name)

            #check index out of range, just with arraytype (arraytype just in vardecl)
            if isConstant and type(arraySymbol.mtype) is ArrayType : # index expr is constants
                if valueIndexExpr not in range(int(str(arraySymbol.mtype.dimen))): #cast type since arraySymbol.mtype.dimen is a TerminalNode???
                    raise IndexOutOfRange(ast) 
            return arraySymbol.mtype.eleType,False , arraySymbol.value
        #foo(..)[i]
        else:
            arraySymbol=self.lookup(ast.arr.method.name,mixEnvi[::-1],lambda x:x.name)
            if arraySymbol is None:
                raise Undeclared(Function(),ast.arr.method)
            if not isinstance(arraySymbol.mtype,MType): #case foo is a variable (int foo;)
                raise TypeMismatchInExpression(ast.arr)
            return arraySymbol.mtype.rettype.eleType, False, arraySymbol.value
            
    def visitId(self, ast, envi):
        mixEnvi= reduce(lambda x,y:x+y[1:],envi,[])
        idSymbol=self.lookup(ast.name,mixEnvi[::-1],lambda x:x.name)

        if idSymbol is None:
            raise Undeclared(Identifier(),ast.name)
      
        if not isinstance(idSymbol.mtype,(MType,ArrayType,ArrayPointerType)) and idSymbol.value is None:
            raise UninitializedVariable(ast.name)
        return idSymbol.mtype, False, idSymbol.value #<type> <isConstant> <value>
