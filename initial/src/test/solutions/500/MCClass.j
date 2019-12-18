.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is i I from Label0 to Label1
Label0:
.var 1 is j I from Label0 to Label1
	iconst_1
	ifgt Label2
	goto Label4
Label2:
	bipush 100
	invokestatic io/putInt(I)V
	goto Label3
Label4:
	sipush 200
	invokestatic io/putInt(I)V
Label3:
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MCClass/foo(I)I
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
