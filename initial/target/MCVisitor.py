# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#many_decs.
    def visitMany_decs(self, ctx:MCParser.Many_decsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dec.
    def visitDec(self, ctx:MCParser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_dec.
    def visitVar_dec(self, ctx:MCParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_var.
    def visitList_var(self, ctx:MCParser.List_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primtype.
    def visitPrimtype(self, ctx:MCParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_dec.
    def visitFunc_dec(self, ctx:MCParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#types.
    def visitTypes(self, ctx:MCParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#pointertype.
    def visitPointertype(self, ctx:MCParser.PointertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_para.
    def visitList_para(self, ctx:MCParser.List_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_dec.
    def visitPara_dec(self, ctx:MCParser.Para_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#while_stmt.
    def visitWhile_stmt(self, ctx:MCParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_stmt.
    def visitExp_stmt(self, ctx:MCParser.Exp_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#terminated_tok.
    def visitTerminated_tok(self, ctx:MCParser.Terminated_tokContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#element_of_array.
    def visitElement_of_array(self, ctx:MCParser.Element_of_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)



del MCParser