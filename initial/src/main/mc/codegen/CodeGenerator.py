'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
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

    def visitProgram(self, ast, gloenvi):
        #ast: Program
        #gloenvi: Any
        #print 3 lines directives 
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        subBody = SubBody(None, self.env)
        for x in ast.decl:
            subBody = self.visit(x, subBody)
        # generate default constructor
        initFunc = FuncDecl(Id("<init>"), list(), None, Block(list()))
        self.genMETHOD(initFunc, gloenvi, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return gloenvi

    def visitFuncDecl(self, ast, subBody):
        #ast: FuncDecl
        #subBody: frame + list(Symbol)

        # subctxt = subBody
        # if subctxt.frame is not None:
        #     frame = Frame(ast.name.name, ast.returnType)
        #     print(ast.name.name)
        #     self.genMETHOD(ast, subctxt.sym, frame)
        # else:
        #     return SubBody(None, [Symbol(ast.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))] + subctxt.sym)

        frame = Frame(ast.name.name, ast.returnType) #Frame('main', void)
        self.genMETHOD(ast, subBody.sym, frame)
        return SubBody(None, [Symbol(ast.name.name, MType([x.varType for x in ast.param] if ast.name.name not in ['main','<init>'] else list(), ast.returnType), CName(self.className))] + subBody.sym)

        # subctxt = subBody
        # frame = subctxt.frame
        # if frame is not None:
        #     frame = Frame(ast.name.name, ast.returnType)
        #     self.genMETHOD(ast, subctxt.sym, frame)
        # else:
        #     return SubBody(None, [
        #             Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))
        #         ] + subctxt.sym)
    
    def genMETHOD(self, ast,envi, frame):
        #ast: FuncDecl
        #envi: list Symbols
        #frame: Frame

        isInit = ast.returnType is None
        isMain = ast.name.name == "main" 
       
        returnType = VoidType() if isInit else ast.returnType
        methodName = "<init>" if isInit else ast.name.name
        #main: String[] args
        #other: foo(int a,b) => [int, int]
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in ast.param]
    
        mtype = MType(intype, VoidType()) if isMain else MType(intype,returnType) 

        #.method public static? main(...)V
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        localEnvi = envi

        # Generate code for parameter declarations
        if isInit:
            #.var 0 is this LMCClass; from Label0 to Label1
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            #.var 0 is args [Ljava/lang/String; from Label0 to Label1
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        #if localEnvi is None: localEnvi=[]
            # visit parameters and add vardecls to s
        s= SubBody(frame,localEnvi)
        
        for x in ast.param:
            s= self.visit(x,s)
         


        body = ast.body

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

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
     
        if sBody.frame is None: #in global declaration
    #============================drafts
    #neu la global thi dung clinit de new array
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable, ast.varType, False, ""))
            return SubBody(None, [Symbol(ast.variable, ast.varType, CName(self.className))] + sBody.sym)
        else: #in local of function
            index = sBody.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, ast.variable, ast.varType, sBody.frame.getStartLabel(), sBody.frame.getEndLabel(), sBody.frame))
            return SubBody(sBody.frame, [Symbol(ast.variable, ast.varType, Index(index))] + sBody.sym)


    #==================================Statement=====================================

    #generate Return for methods different VoidType and not in main function
    def visitReturn(self, ast: Return, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        retType = frame.returnType

        if (not isinstance(retType, VoidType)) and (frame.name != "main"):
            expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, False))
            # print(frame.currOpStackSize)
            if type(retType) is FloatType and type(expType) is IntType:
                expCode = expCode + self.emit.emitI2F(frame)
            self.emit.printout(expCode)
            self.emit.printout(self.emit.emitRETURN(retType, frame))

        ## self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))
        #return True
        return None
    
    def visitIf(self, ast: If, o: SubBody):
        exprCode, exprType = self.visit(ast.expr, Access(o.frame, o.sym, False, False))
        self.emit.printout(exprCode)
        
        labelTrue = o.frame.getNewLabel()
        labelEnd = o.frame.getNewLabel()
        labelFalse = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFTRUE(labelTrue, o.frame))

        self.emit.printout(self.emit.emitGOTO(labelFalse, o.frame))
        
        self.emit.printout(self.emit.emitLABEL(labelTrue, o.frame))
        
        self.visit(ast.thenStmt,o)

        self.emit.printout(self.emit.emitGOTO(labelEnd, o.frame))
        
        self.emit.printout(self.emit.emitLABEL(labelFalse, o.frame))

        if ast.elseStmt is not None:
            self.visit(ast.elseStmt,o)
        
        self.emit.printout(self.emit.emitLABEL(labelEnd, o.frame))

    def visitDowhile(self, ast:Dowhile, o: SubBody):
        labelStart = o.frame.getNewLabel()
        
        self.emit.printout(self.emit.emitLABEL(labelStart, o.frame))

        o.frame.enterLoop()

        [self.visit(x, o) for x in ast.sl]

        expCode, expType = self.visit(ast.exp, Access(o.frame, o.sym, False, False))

        self.emit.printout(expCode)
        
        self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame)
        
        self.emit.printout(self.emit.emitIFTRUE(labelStart, o.frame))
        
        self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame)
        
        o.frame.exitLoop()
        
    def visitFor(self, ast: For, o: SubBody):
        result=''
        expr1Code, expr1Type = self.visit(ast.expr1, Access(o.frame, o.sym, False, False))
        expr2Code, expr2Type = self.visit(ast.expr2, Access(o.frame, o.sym, False, False))
        result+=expr1Code+expr2Code
        result+=self.emit.emitIFTRUE(labelStart, o.frame)
        labelStart = o.frame.getNewLabel()
        result+=self.emit.emitLABEL(labelStart, o.frame)

        self.visit(ast.loop)



        expr3Code, expr3Type = self.visit(ast.expr3, Access(o.frame, o.sym, False, False))



    def visitBlock(self, ast: Block, o: SubBody):
        [self.visit(x, o) for x in ast.member]

    #==================================Expression=====================================
    # Param:    ast, Access(frame, sym, isLeft, isFirst)
    # Return:   (code, type)


    # def visitId(self, ast: Id, acc: Access):
    #     # Return (name, type, index)

    #     #if acc.isLeft and acc.checkArrayType: return False, None

    #     sym = self.lookup(ast.name, acc.sym, lambda x: x.name)

    #     # recover status of stack in acc.frame
    #     if not acc.isFirst and acc.isLeft: acc.frame.push()
    #     elif not acc.isFirst and not acc.isLeft: acc.frame.pop()

    #     isArrayType = type(sym.mtype) in [ArrayType,ArrayPointerType]:
    #     emitType = StupidUtils.retrieveType(sym.mtype)
    #     if sym.value is None: # not index -> global var - static field
    #         if acc.isLeft and not isArrayType: retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, acc.frame)
    #         else: retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, acc.frame)
    #     else:
    #         if acc.isLeft and not isArrayType: retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, acc.frame)
    #         else: retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, acc.frame)

    #     return retCode, sym.mtype

    #Id is just in local of function

    

    def visitId(self, ast: Id, acc: Access):

        resultCode=""
        sym = self.lookup(ast.name, acc.sym, lambda x: x.name)

        if acc.isFirst:
            if acc.isLeft:
                if isinstance(sym.mtype,(ArrayPointerType,ArrayType)):
                    resultCode+= self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, acc.frame)
        else:
            if acc.isLeft:
                resultCode+= self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, acc.frame)
            else:
                resultCode+= self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, acc.frame)
        return resultCode, sym.mtype

    def visitArrayCell(self, ast: ArrayCell, acc: Access):
       
        arrcode, arrtype = self.visit(ast.arr, acc)
        indexcode, indextype = self.visit(ast.idx, acc)
        if acc.isLeft:
            if acc.isFirst:
                result = arrcode + indexcode, arrtype.eleType
            else:
                result = self.emit.emitASTORE(arrtype.eleType, acc.frame), arrtype.eleType
        elif not acc.isLeft:
            result = arrcode + indexcode + self.emit.emitALOAD(arrtype.eleType, acc.frame), arrtype.eleType
        return result


    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for i, arg in enumerate(ast.param):
            #arg:expr
            paramcode, paramtype = self.visit(arg, Access(frame, nenv, False, False))
            #convert float to int
            #but not yet converting array to array pointer draft
            if type(paramtype) != type(sym.mtype.partype[i]): 
                paramcode+= self.emit.emitI2F(frame)
            in_ = (in_[0] + paramcode, in_[1].append(paramtype))
        
        temp= self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
        if isinstance(o,SubBody):
            self.emit.printout(in_[0])
            self.emit.printout(temp)
        else:
            return in_[0] + temp, sym.mtype.rettype


    def visitBinaryOp(self, ast:BinaryOp, acc:Access):

       # [print(x.name) for x in acc.sym]

        #acc:   #frame: Frame
                #sym: List[Symbol]
                #isLeft: Boolean
                #isFirst: Boolean
        #ast.op:str
        #ast.left:Expr
        #ast.right:Expr
    
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
                result+= selt.emit.emitIREM()
        else: #ast.op is assign op
            lcode, ltype = self.visit(ast.left, Access(acc.frame,acc.sym,True,True))
      
            rcode, rtype = self.visit(ast.right, Access(acc.frame,acc.sym,False,False))
        
            lcode2, ltype2 = self.visit(ast.left, Access(acc.frame,acc.sym,True,False))

            result= lcode+rcode+lcode2
            #just print if this is assign Op:
            self.emit.printout(result)
        return result, ltype

    def visitUnaryOp(self, ast: UnaryOp, acc:Access):
       
        bodycode, bodytype = self.visit(ast.body,acc)
        if ast.op == '-':
            return bodycode + self.emit.emitNEGOP(bodytype, acc.frame)
        if ast.op =='!':
            return bodycode + self.emit.emitNOT(bodytype, acc.frame)
        
    def visitIntLiteral(self, ast, acc):
      
        return self.emit.emitPUSHICONST(ast.value, acc.frame), IntType()
       
    def visitFloatLiteral(self, ast, acc):
   
        return self.emit.emitPUSHFCONST(str(ast.value), acc.frame), FloatType()

    def visitBooleanLiteral(self, ast, acc):
     
        return self.emit.emitPUSHICONST(str(ast.value), acc.frame), BoolType()
    
    def visitStringLiteral(self, ast, acc):
        
        return self.emit.emitPUSHCONST(ast.value,StringType(), acc.frame), StringType()