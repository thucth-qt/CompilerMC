#MSSV: 1713454

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import *

class ASTGeneration(MCVisitor):#tra ve kieu AST
    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        #danh cho vardecl
        # varDecListList=[self.visit(x) for x in ctx.dec()];
        # varDecList= reduce(lambda x,y:x+y,varDecListList)        # return Program(varDeclList)
        #danh cho funcdecl
        DecListList= [self.visit(x) for x in ctx.dec()]
        DecList= reduce(lambda x,y:x+y,DecListList) if DecListList else []
        return Program(DecList)


    # Visit a parse tree produced by MCParser#dec.
    def visitDec(self, ctx:MCParser.DecContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MCParser#var_dec.
    # return a list of pairs of variabe and type
    # int a,b; --> (a,IntType) (b,IntType)
    def visitVar_dec(self, ctx:MCParser.Var_decContext):
        varList=[]
        for varWalker in ctx.var():
            varTemp=self.visit(varWalker)
            typeTemp=self.visit(ctx.primtype())
            if list==type(varTemp):#if varTemp.INTLIT():
                variable=varTemp[0].getText()
                varType=ArrayType(varTemp[1],typeTemp)
            else:
                variable=varTemp.getText()
                varType=typeTemp
            varList.append(VarDecl(variable,varType))
        return varList


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        if ctx.INTLIT():
            return [ctx.ID(),ctx.INTLIT()]
        else:
            return ctx.ID()


    # Visit a parse tree produced by MCParser#primtype.
    def visitPrimtype(self, ctx:MCParser.PrimtypeContext):
        if ctx.INT(): return IntType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.BOOLEAN():return BoolType()
        elif ctx.STRING():return StringType()


    # Visit a parse tree produced by MCParser#func_dec.
    def visitFunc_dec(self, ctx:MCParser.Func_decContext):
        returnType = self.visit(ctx.types())
        name=Id(ctx.ID().getText())
        param=self.visit(ctx.list_para()) if ctx.list_para() else []
        body=self.visit(ctx.block_stmt())
        return [FuncDecl(name,param,returnType,body)]


    # Visit a parse tree produced by MCParser#types.
    def visitTypes(self, ctx:MCParser.TypesContext):
        if ctx.primtype(): return self.visit(ctx.primtype())
        elif ctx.pointertype():return self.visit(ctx.pointertype())
        else: return VoidType()


    # Visit a parse tree produced by MCParser#pointertype.
    def visitPointertype(self, ctx:MCParser.PointertypeContext):

        return ArrayPointerType(self.visit(ctx.primtype()))


    # Visit a parse tree produced by MCParser#list_para.
    def visitList_para(self, ctx:MCParser.List_paraContext):
        #return self.visitChildren(ctx)
        return [self.visit(x) for x in ctx.para_dec()]


    # Visit a parse tree produced by MCParser#para_dec.
    def visitPara_dec(self, ctx:MCParser.Para_decContext):
        if ctx.LQ(): varType=ArrayPointerType(self.visit(ctx.primtype()))
        else: varType=self.visit(ctx.primtype())
        variable=ctx.ID().getText()
        return VarDecl(variable,varType)


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        
        if not ctx.block_member(): return Block([])
        #each visitBlock_member() return a list
        #each a stmt is a list --> stmtList is a list of lists
        #stmt: int a,b; --> [VarDecl(a,IntType),VarDecl(b,IntType)]
        #stmt: if a==b then x=1; -->[........] 
        stmtList = [self.visit(x) for x in ctx.block_member()]
        #stmts: a list of prime stmt
        #stmts: [VarDecl(a,IntType),VarDecl(b,IntType),If(..),...]
        stmts= reduce(lambda x,y:x+y,stmtList) 
        return Block(stmts)

    # Visit a parse tree produced by MCParser#block_member.
    def visitBlock_member(self, ctx:MCParser.Block_memberContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return [self.visit(ctx.getChild(0))] # must convert to list like var_dec


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):

        expr= self.visit(ctx.exp())
        #because ctx.stmt(1) is a list, so need a index [0]
        thenStmt=self.visit(ctx.stmt(0))[0] 
        if ctx.stmt(1):
            elseStmt= self.visit(ctx.stmt(1)) [0]
            return If(expr,thenStmt,elseStmt)
        else:
            return If(expr,thenStmt)

    # Visit a parse tree produced by MCParser#while_stmt.
    def visitWhile_stmt(self, ctx:MCParser.While_stmtContext):

        listStmt = reduce(lambda x,y:x+y,[self.visit(z) for z in ctx.stmt()])
        Expr= self.visit(ctx.exp())
        return Dowhile(listStmt,Expr)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        expr1=self.visit(ctx.exp(0))
        expr2=self.visit(ctx.exp(1))
        expr3=self.visit(ctx.exp(2))
        loop=self.visit(ctx.stmt())[0]
        return For(expr1,expr2,expr3,loop)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return()

    # Visit a parse tree produced by MCParser#exp_stmt.
    def visitExp_stmt(self, ctx:MCParser.Exp_stmtContext):
        return self.visit(ctx.exp())


        # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return BinaryOp(ctx.ASN().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp())) if ctx.ASN() else self.visit(ctx.exp1())


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2())) if ctx.OR() else self.visit(ctx.exp2())


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3())) if ctx.AND() else self.visit(ctx.exp3())


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1))) if ctx.exp4(1) else self.visit(ctx.exp4(0))


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1))) if ctx.exp5(1) else self.visit(ctx.exp5(0))


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6())) if ctx.exp5() else self.visit(ctx.exp6())


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7())) if ctx.exp6() else self.visit(ctx.exp7())


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp7())) if ctx.exp7() else self.visit(ctx.exp8())


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp())) if ctx.exp() else self.visit(ctx.exp9())


    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        return self.visit(ctx.exp()) if ctx.exp() else self.visit(ctx.operand())

    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT(): return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT(): return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLIT(): return BooleanLiteral(ctx.BOOLIT().getText()=="true")
        elif not ctx.LB(): return Id(ctx.ID().getText())
        elif ctx.LB(): return CallExpr(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.exp()] if ctx.exp() else [])
