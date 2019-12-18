.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass.a I
	getstatic MCClass.a I
	invokestatic io/putIntLn(I)V
Label2:
.var 1 is a I from Label2 to Label3
	iconst_2
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label3:
	getstatic MCClass.a I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
