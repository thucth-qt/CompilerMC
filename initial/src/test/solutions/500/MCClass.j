.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_1
	iastore
	aload_1
	iconst_1
	iconst_1
	aload_1
	iconst_0
	iaload
	iadd
	iastore
	aload_1
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 8
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
