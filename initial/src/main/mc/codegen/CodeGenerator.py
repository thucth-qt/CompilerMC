'''
 *  1713454
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def initialEnv(self):
        return [Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putLn", MType([], VoidType()), CName(self.libName))]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String directry to folder containing MCClass.j of current testcase

        gloenv = self.initialEnv()
        gc = CodeGenVisitor(ast, gloenv, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname =cname
    
    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j") #accept input that file MCClass.j

#==================================Declaration===================================
    '''
    this section is to visit Declaration for generating drectives:

        .source MCClass.java
        .class public MCClass
        .super java.lang.Object
        .method public static foo(I)I

    '''
    def visitProgram(self, ast, gloenvi):
        '''
        *print lines of directives 
        1. visit all vardecls in global and set static field
        2. visit funcdecls
        '''
        gloenvi=self.env
        
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        #in global: frame = None
        subBody = SubBody(None,gloenvi )

       
        #visit Declarations:
        '''
        1. visit all var declarations in global
        2. add func declarations in global to env (for calling inter functions)
        3. visit all all func declarations
        '''
        for x in filter(lambda x: isinstance(x,VarDecl), ast.decl):
            subBody = self.visit(x, subBody)
        for x in filter(lambda x: isinstance(x,FuncDecl), ast.decl):
            subBody.sym = [Symbol(x.name.name, MType([y.varType for y in x.param],x.returnType),CName(self.className))]+subBody.sym
        for x in filter(lambda x: isinstance(x,FuncDecl), ast.decl):
            subBody = self.visit(x, subBody)

        # generate default constructor
        initConstructor = FuncDecl(Id("<init>"), list(), None, Block(list()))
        initClass = FuncDecl(Id("<clinit>"), list(), None, Block(list()))
        self.genMETHOD(initConstructor, subBody.sym, Frame("<init>", VoidType))
        self.genMETHOD(initClass, subBody.sym, Frame("<clinit>", VoidType))

        self.emit.emitEPILOG()
        return gloenvi

    def visitFuncDecl(self, ast, subBody):
        
        frame = Frame(ast.name.name, ast.returnType) #Frame('main', void)
        subBody.sym=[Symbol(ast.name.name, MType([x.varType for x in ast.param] if ast.name.name not in ['main','<init>'] else list(), ast.returnType), CName(self.className))] + subBody.sym
        self.genMETHOD(ast, subBody.sym, frame)
        return subBody
    
    def genMETHOD(self, ast,envi, frame):
     
        #ast: FuncDecl
        #envi: list Symbols
        #frame: Frame

        isInit = ast.name.name == "<init>"
        isClinit = ast.name.name == "<clinit>"
        isMain = ast.name.name == "main" 
       
        returnType = VoidType() if isInit or isClinit else ast.returnType
        methodName = ast.name.name
        #main: String[] args
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in ast.param]
    
        mtype = MType(intype, VoidType()) if isMain else MType(intype,returnType) 

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        localEnvi = envi
        # Generate code for parameter declarations
        if isInit:
            #.var 0 is this LMCClass; from Label0 to Label1
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isClinit:
            #in isClinit, there is not declaration, just initialize
            pass
        if isMain:
            #.var 0 is args [Ljava/lang/String; from Label0 to Label1
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        s= SubBody(frame,localEnvi)
        
        for x in ast.param:
            s= self.visit(x,s)
         
        body = ast.body

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        if isClinit:
            '''
            bipush 10
            newarray int
            putstatic MCClass.a [I
	
            '''
            globalArrVar = filter(lambda x:(isinstance(x.value, CName) and isinstance(x.mtype, ArrayType)),envi )
            for ast_i in globalArrVar:
                self.emit.printout(self.emit.emitClinitForArrayGlobal(ast_i.value.value+"."+ ast_i.name, ast_i.mtype,frame ))
        for x in body.member:
            if isinstance(x,VarDecl):
                s= self.visit(x,s)
            else:
                self.visit(x,s)

          
        # [self.visit(x, s) for x in body.member]
        # [print(x.name) for x in s]
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # Generate Return for only VoidType or Return in Main function must be convert into VoidType:
  
        if (type(returnType) is VoidType) or (frame.name == "main"):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitVarDecl(self, ast, sBody):
        #in global declaration
        if sBody.frame is None: 
            #============================drafts
            #neu la global thi dung clinit de new array
            tem=self.emit.emitATTRIBUTE(ast.variable, ast.varType, False, "")
            self.emit.printout(tem)
            return SubBody(None, [Symbol(ast.variable, ast.varType, CName(self.className))] + sBody.sym)
        else: #in local of function
            index = sBody.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, ast.variable, ast.varType, sBody.frame.getStartLabel(), sBody.frame.getEndLabel(), sBody.frame))
            return SubBody(sBody.frame, [Symbol(ast.variable, ast.varType, Index(index))] + sBody.sym)

#==================================Statement=====================================
    '''
    this section is to visit Statement:
        - Return nothing
        - printout rigth when visit
    '''

    def visitReturn(self, ast: Return, o: SubBody):
        '''generate Return for methods different VoidType and not in main function'''

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        retType = frame.returnType

        if (not isinstance(retType, VoidType)) and (frame.name != "main"):
            expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, False))
            if type(retType) is FloatType and type(expType) is IntType:
                expCode = expCode + self.emit.emitI2F(frame)
            self.emit.printout(expCode)
            self.emit.printout(self.emit.emitRETURN(retType, frame))
        return True #isReturn , for check isReturn later
    def visitIf(self, ast: If, o: SubBody):
        '''
            1. visit expr
            2. if true go to label 1
            3. do elseStmt
            4. go to label 2
            5.Label 1
            6. do thenStmt
            7.Label 2
            8.label end

        '''
        exprCode, exprType = self.visit(ast.expr, Access(o.frame, o.sym, False, False))
        self.emit.printout(exprCode)
        
        labelTrue = o.frame.getNewLabel()
        labelEnd = o.frame.getNewLabel()
        #labelFalse = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFTRUE(labelTrue, o.frame))

        # self.emit.printout(self.emit.emitGOTO(labelFalse, o.frame))
        isReturnElse=False
        if ast.elseStmt is not None:
            if self.visit(ast.elseStmt,o) is True: isReturnElse = True

        if not isReturnElse:
            self.emit.printout(self.emit.emitGOTO(labelEnd, o.frame))

        self.emit.printout(self.emit.emitLABEL(labelTrue, o.frame))
        
        isReturnThen=False
        if self.visit(ast.thenStmt,o) is True:
            isReturnThen=True
        
        self.emit.printout(self.emit.emitLABEL(labelEnd, o.frame))
        return isReturnThen and isReturnElse
    def visitDowhile(self, ast:Dowhile, o: SubBody):
        '''
        1. Label Start
        2. visit list stmt
        3. Label Continue
        4. visit Expr
        5. if True go to Label Start
        6. Label Break
        
        '''
        labelStart = o.frame.getNewLabel()
        
        o.frame.enterLoop()

        self.emit.printout(self.emit.emitLABEL(labelStart, o.frame))

        [self.visit(x, o) for x in ast.sl]

        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))

        expCode, expType = self.visit(ast.exp, Access(o.frame, o.sym, False, False))

        self.emit.printout(expCode)
        
        self.emit.printout(self.emit.emitIFTRUE(labelStart, o.frame))
        
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        
        o.frame.exitLoop()
        
    def visitFor(self, ast: For, o: SubBody):
        '''
        1.visit expr 1 (like visit a stmt: visit(ast, SubBody) because this is assign op)
        2.Label condition
        3.visit expr 2 (like visit a expr: visit(ast, Access)) 
        4.if True goto Label True
        5.go to Label Break (the same purpose with Label End)
        6.Label True
        7.visit Stmt
        8.Label Continue
        9.visit expr3 (like visit a stmt: visit(ast, SubBody))
        10. go to Label condition
        11. Label Break

        '''
        labelTrue  = o.frame.getNewLabel()
        labelCondition = o.frame.getNewLabel()
        o.frame.enterLoop()
        labelBreak = o.frame.getBreakLabel()
        labelContinue = o.frame.getContinueLabel()
        isReturn=False
        self.visit(ast.expr1,o)
        self.emit.printout(self.emit.emitLABEL(labelCondition, o.frame))
        expr2Code, expr2Type = self.visit(ast.expr2, Access(o.frame, o.sym, False, False))
        self.emit.printout(expr2Code)
        self.emit.printout(self.emit.emitIFTRUE(labelTrue, o.frame))
        self.emit.printout(self.emit.emitGOTO(labelBreak, o.frame))
        self.emit.printout(self.emit.emitLABEL(labelTrue, o.frame))
        if self.visit(ast.loop, o) is True:
            isReturn = True
        self.emit.printout(self.emit.emitLABEL(labelContinue, o.frame))
        if not isReturn:
            self.visit(ast.expr3, o)
            self.emit.printout(self.emit.emitGOTO(labelCondition, o.frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak, o.frame))

        o.frame.exitLoop()
        return isReturn

    def visitBreak(self, ast: Break, o: SubBody):
        '''
        when enter the loop, we call frame.enterLoop to create BreakLabel
        and then we placed it in some place
        '''
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
    
    def visitContinue(self, ast: Continue, o:SubBody):
        '''
        when enter the loop, we call frame.enterLoop to create ContinueLabel
        and then we placed it in some place
        '''
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame))

    def visitBlock(self, ast: Block, o: SubBody):
        '''
        remember to pop variable declared in scope
        '''
        frame=o.frame
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        #count the number of vardecl to pop it out of sym after exit scope
        count=0
        isReturn=False
        for x in ast.member:
            if isinstance(x,VarDecl):
                o= self.visit(x,o)
                count+=1
            else:
                if self.visit(x,o) is True:
                    isReturn=True
        o.sym = o.sym[count:]
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        frame.exitScope()
        return isReturn

#==================================Expression====================================
    '''
    *Param:     ast, Access(frame, sym, isLeft, isFirst)
    *Return:    code, type
    *Note:      the first command in each method  "isinstance(acc,SubBody): return" say that 
                if expr which called as a statement should do nothing (except assign expression, and call)
    '''

    def visitId(self, ast: Id, acc):
        '''
        *every varible is visited two times
        *array, field of class in left : first: load reference,  second: store value
        *simple variable  and array, field of class in right :  first: do nothing,     second: store value
        '''

        if isinstance(acc,SubBody): return
        resultCode=""
        sym = self.lookup(ast.name, acc.sym, lambda x: x.name)
        isGlobal =isinstance(sym.value,CName)
        if acc.isLeft: #left
            if acc.isFirst:#first
                if isinstance(sym.mtype,(ArrayPointerType,ArrayType)):
                    if isGlobal :
                        resultCode+= self.emit.emitGETSTATIC(sym.value.value+"." + ast.name, sym.mtype,acc.frame)
                    else:
                        resultCode+= self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, acc.frame)
            
            else: #second
                if isGlobal:
                    #name = Class name + "." +field name 
                    resultCode+= self.emit.emitPUTSTATIC(sym.value.value+"." + ast.name, sym.mtype, acc.frame)
                else:
                    resultCode+= self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, acc.frame)

        else: #right
            if acc.isFirst: #left
                pass
            else:#second
                if  isGlobal:
                    resultCode+= self.emit.emitGETSTATIC(sym.value.value+"." + ast.name, sym.mtype, acc.frame)
                else:
                    resultCode+= self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, acc.frame)
        return resultCode, sym.mtype
    
    def visitArrayCell(self, ast: ArrayCell, acc):
        '''
        *in LSH and in second time access: store (aload)
        *in RHS: load value (<type>astore)
        '''
        if isinstance(acc,SubBody): return
        
        if acc.isLeft: #LHS
            '''
            *if a[10] is LHS example: a[10]=3000;
                1. aload , iconst (first time)
                2. iconst 3000 (don't care)
                3. iastore      (second time)
            '''
            
            if acc.isFirst:
                # aload , iconst
                arrcode1, arrtype1 = self.visit(ast.arr, acc)
                indexcode,indextype = self.visit(ast.idx, Access(acc.frame, acc.sym,False, False ))
                result = arrcode1+ indexcode 
            else:
                arrcode1, arrtype1 = self.visit(ast.arr, Access(acc.frame, acc.sym,True, True ))
                 # iastore
                result = self.emit.emitASTORE(arrtype1.eleType, acc.frame)


        else :#RHS
            '''
            *if a[10] is RHS example: i = a[10];
                1. aload <index of a> (second time)
                2. iconst 10            (second time)
                3. iaload               (second time)
                4. istore <dont care>
            '''
            
            if acc.isFirst:
                result=""
            else:
                arrcode1, arrtype1 = self.visit(ast.arr, acc)
                indexcode, indextype = self.visit(ast.idx, acc)
                result= arrcode1 + indexcode + self.emit.emitALOAD(arrtype1.eleType, acc.frame)

        #print(" left ",acc.isLeft , ";     first ", acc.isFirst," :\n ",result)
        return result, arrtype1.eleType

    def visitCallExpr(self, ast: CallExpr, o):
        '''
        *input o: subBody or Access
        *subBody when Call is a statement => print code JVM
        *Access when Call is a expression => return code JVM for caller
        '''

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for i, arg in enumerate(ast.param):
            #arg:expr
            #in RHS just visit in 2nd time
            paramcode, paramtype = self.visit(arg, Access(frame, nenv, False, False))

            #convert float to int
            if isinstance(paramtype,IntType) and isinstance(sym.mtype.partype[i],FloatType): 
                paramcode+= self.emit.emitI2F(frame)
 
            in_ = (in_[0] + paramcode, in_[1]+[paramtype])

        
        temp= self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
        if isinstance(o,SubBody):
            self.emit.printout(in_[0])
            self.emit.printout(temp)
        else:
            return in_[0] + temp, sym.mtype.rettype

    def visitBinaryOp(self, ast:BinaryOp, acc):
        '''
        divide into two type of Operation
        1. Assign: can be statement or expression
        2. Others: just be expression
        '''
        # Not assign Op
        if ast.op != '=':
            lcode, ltype = self.visit(ast.left, acc)
            #print("binOp left: "+ str(acc.frame.currOpStackSize))
            rcode, rtype = self.visit(ast.right, acc)
            #print("binOp right: "+ str(acc.frame.currOpStackSize))

            result=lcode
            #coercions type
            if isinstance(ltype,IntType) and isinstance(rtype,FloatType):
                ltype=rtype=FloatType()
                result+=self.emit.emitI2F(acc.frame)
                result+=rcode
            elif isinstance(ltype,FloatType) and isinstance(rtype,IntType):
                ltype=rtype=FloatType()
                result+=rcode
                result+=self.emit.emitI2F(acc.frame)
            else:
                result+=rcode
            
            #generate code for Op
            if ast.op in [ '<', '<=', '>', '>=', '==', '!=' ]: 
                result+= self.emit.emitREOP(ast.op,ltype,acc.frame)
            elif ast.op == '||': 
                result+= self.emit.emitOROP(acc.frame)
            elif ast.op == '&&': 
                result += self.emit.emitANDOP(acc.frame)
            elif ast.op in ['+','-']:
                result+= self.emit.emitADDOP(ast.op,ltype,acc.frame)
            elif ast.op in ['*','/']:
                result+= self.emit.emitMULOP(ast.op,ltype,acc.frame)
            elif ast.op == '%':
                result+= self.emit.emitMOD(acc.frame)
            #print(ast,result)
            return result, ltype
            
        else: #ast.op is assign op
            lcode, ltype = self.visit(ast.left, Access(acc.frame,acc.sym,True,True))

            rcode, rtype = self.visit(ast.right, Access(acc.frame,acc.sym,False,False))
         
            lcode2, ltype2 = self.visit(ast.left, Access(acc.frame,acc.sym,True,False))

            if isinstance(ltype,FloatType) and isinstance(rtype,IntType):
                result= lcode+rcode+self.emit.emitI2F(acc.frame)+lcode2
            else:
                result= lcode+rcode+lcode2

            #just print if this is assign Op:
            if isinstance(acc,SubBody): #statement
                self.emit.printout(result)
            else: #expression => a=4 return 5 => need load a to Op stack
                rcode2, rtype2 = self.visit(ast.left, Access(acc.frame,acc.sym,False,False))
                return result + rcode2, ltype

    def visitUnaryOp(self, ast: UnaryOp, acc):
        '''
        too easy to describe
        '''
        if isinstance(acc,SubBody): return

        bodycode, bodytype = self.visit(ast.body,acc)
        if ast.op == '-':
            return bodycode + self.emit.emitNEGOP(bodytype, acc.frame), bodytype
        if ast.op =='!':
            return bodycode + self.emit.emitNOT(bodytype, acc.frame), bodytype
        
    def visitIntLiteral(self, ast, acc):
        if isinstance(acc,SubBody): return
        return self.emit.emitPUSHICONST(ast.value, acc.frame), IntType()

       
    def visitFloatLiteral(self, ast, acc):
        if isinstance(acc,SubBody): return
        return self.emit.emitPUSHFCONST(str(ast.value), acc.frame), FloatType()

    def visitBooleanLiteral(self, ast, acc):
        if isinstance(acc,SubBody): return
        return self.emit.emitPUSHICONST(str(ast.value), acc.frame), BoolType()
   
    
    def visitStringLiteral(self, ast, acc):
        if isinstance(acc,SubBody): return
        return self.emit.emitPUSHCONST(ast.value,StringType(), acc.frame), StringType()
