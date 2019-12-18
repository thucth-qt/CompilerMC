.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is i I from Label0 to Label1
Label0:
.var 1 is j I from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label2:
.var 2 is j I from Label2 to Label3
	bipush 6
	istore_2
	iload_2
	invokestatic io/putInt(I)V
Label3:
	iload_1
	invokestatic io/putInt(I)V
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 3
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
