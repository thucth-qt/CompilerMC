# Generated from F:/assignment2/initial/src/main/mc/parser\MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete listener for a parse tree produced by MCParser.
class MCListener(ParseTreeListener):

    # Enter a parse tree produced by MCParser#program.
    def enterProgram(self, ctx:MCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MCParser#program.
    def exitProgram(self, ctx:MCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MCParser#dec.
    def enterDec(self, ctx:MCParser.DecContext):
        pass

    # Exit a parse tree produced by MCParser#dec.
    def exitDec(self, ctx:MCParser.DecContext):
        pass


    # Enter a parse tree produced by MCParser#var_dec.
    def enterVar_dec(self, ctx:MCParser.Var_decContext):
        pass

    # Exit a parse tree produced by MCParser#var_dec.
    def exitVar_dec(self, ctx:MCParser.Var_decContext):
        pass


    # Enter a parse tree produced by MCParser#var.
    def enterVar(self, ctx:MCParser.VarContext):
        pass

    # Exit a parse tree produced by MCParser#var.
    def exitVar(self, ctx:MCParser.VarContext):
        pass


    # Enter a parse tree produced by MCParser#primtype.
    def enterPrimtype(self, ctx:MCParser.PrimtypeContext):
        pass

    # Exit a parse tree produced by MCParser#primtype.
    def exitPrimtype(self, ctx:MCParser.PrimtypeContext):
        pass


    # Enter a parse tree produced by MCParser#func_dec.
    def enterFunc_dec(self, ctx:MCParser.Func_decContext):
        pass

    # Exit a parse tree produced by MCParser#func_dec.
    def exitFunc_dec(self, ctx:MCParser.Func_decContext):
        pass


    # Enter a parse tree produced by MCParser#types.
    def enterTypes(self, ctx:MCParser.TypesContext):
        pass

    # Exit a parse tree produced by MCParser#types.
    def exitTypes(self, ctx:MCParser.TypesContext):
        pass


    # Enter a parse tree produced by MCParser#pointertype.
    def enterPointertype(self, ctx:MCParser.PointertypeContext):
        pass

    # Exit a parse tree produced by MCParser#pointertype.
    def exitPointertype(self, ctx:MCParser.PointertypeContext):
        pass


    # Enter a parse tree produced by MCParser#list_para.
    def enterList_para(self, ctx:MCParser.List_paraContext):
        pass

    # Exit a parse tree produced by MCParser#list_para.
    def exitList_para(self, ctx:MCParser.List_paraContext):
        pass


    # Enter a parse tree produced by MCParser#para_dec.
    def enterPara_dec(self, ctx:MCParser.Para_decContext):
        pass

    # Exit a parse tree produced by MCParser#para_dec.
    def exitPara_dec(self, ctx:MCParser.Para_decContext):
        pass


    # Enter a parse tree produced by MCParser#block_stmt.
    def enterBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#block_stmt.
    def exitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#block_member.
    def enterBlock_member(self, ctx:MCParser.Block_memberContext):
        pass

    # Exit a parse tree produced by MCParser#block_member.
    def exitBlock_member(self, ctx:MCParser.Block_memberContext):
        pass


    # Enter a parse tree produced by MCParser#stmt.
    def enterStmt(self, ctx:MCParser.StmtContext):
        pass

    # Exit a parse tree produced by MCParser#stmt.
    def exitStmt(self, ctx:MCParser.StmtContext):
        pass


    # Enter a parse tree produced by MCParser#if_stmt.
    def enterIf_stmt(self, ctx:MCParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#if_stmt.
    def exitIf_stmt(self, ctx:MCParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#while_stmt.
    def enterWhile_stmt(self, ctx:MCParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#while_stmt.
    def exitWhile_stmt(self, ctx:MCParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#for_stmt.
    def enterFor_stmt(self, ctx:MCParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#for_stmt.
    def exitFor_stmt(self, ctx:MCParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#break_stmt.
    def enterBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#break_stmt.
    def exitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#continue_stmt.
    def enterContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#continue_stmt.
    def exitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#return_stmt.
    def enterReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#return_stmt.
    def exitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#exp_stmt.
    def enterExp_stmt(self, ctx:MCParser.Exp_stmtContext):
        pass

    # Exit a parse tree produced by MCParser#exp_stmt.
    def exitExp_stmt(self, ctx:MCParser.Exp_stmtContext):
        pass


    # Enter a parse tree produced by MCParser#exp.
    def enterExp(self, ctx:MCParser.ExpContext):
        pass

    # Exit a parse tree produced by MCParser#exp.
    def exitExp(self, ctx:MCParser.ExpContext):
        pass


    # Enter a parse tree produced by MCParser#exp1.
    def enterExp1(self, ctx:MCParser.Exp1Context):
        pass

    # Exit a parse tree produced by MCParser#exp1.
    def exitExp1(self, ctx:MCParser.Exp1Context):
        pass


    # Enter a parse tree produced by MCParser#exp2.
    def enterExp2(self, ctx:MCParser.Exp2Context):
        pass

    # Exit a parse tree produced by MCParser#exp2.
    def exitExp2(self, ctx:MCParser.Exp2Context):
        pass


    # Enter a parse tree produced by MCParser#exp3.
    def enterExp3(self, ctx:MCParser.Exp3Context):
        pass

    # Exit a parse tree produced by MCParser#exp3.
    def exitExp3(self, ctx:MCParser.Exp3Context):
        pass


    # Enter a parse tree produced by MCParser#exp4.
    def enterExp4(self, ctx:MCParser.Exp4Context):
        pass

    # Exit a parse tree produced by MCParser#exp4.
    def exitExp4(self, ctx:MCParser.Exp4Context):
        pass


    # Enter a parse tree produced by MCParser#exp5.
    def enterExp5(self, ctx:MCParser.Exp5Context):
        pass

    # Exit a parse tree produced by MCParser#exp5.
    def exitExp5(self, ctx:MCParser.Exp5Context):
        pass


    # Enter a parse tree produced by MCParser#exp6.
    def enterExp6(self, ctx:MCParser.Exp6Context):
        pass

    # Exit a parse tree produced by MCParser#exp6.
    def exitExp6(self, ctx:MCParser.Exp6Context):
        pass


    # Enter a parse tree produced by MCParser#exp7.
    def enterExp7(self, ctx:MCParser.Exp7Context):
        pass

    # Exit a parse tree produced by MCParser#exp7.
    def exitExp7(self, ctx:MCParser.Exp7Context):
        pass


    # Enter a parse tree produced by MCParser#exp8.
    def enterExp8(self, ctx:MCParser.Exp8Context):
        pass

    # Exit a parse tree produced by MCParser#exp8.
    def exitExp8(self, ctx:MCParser.Exp8Context):
        pass


    # Enter a parse tree produced by MCParser#exp9.
    def enterExp9(self, ctx:MCParser.Exp9Context):
        pass

    # Exit a parse tree produced by MCParser#exp9.
    def exitExp9(self, ctx:MCParser.Exp9Context):
        pass


    # Enter a parse tree produced by MCParser#operand.
    def enterOperand(self, ctx:MCParser.OperandContext):
        pass

    # Exit a parse tree produced by MCParser#operand.
    def exitOperand(self, ctx:MCParser.OperandContext):
        pass


