# Generated from F:/assignment2/initial/src/main/mc/parser\MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0184\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\6\2o\n\2\r\2\16\2p\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4|\n\4\f\4\16\4\177\13")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u008a\n\5\f")
        buf.write("\5\16\5\u008d\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\5\25\u00e7\n\25\3")
        buf.write("\25\3\25\3\25\7\25\u00ec\n\25\f\25\16\25\u00ef\13\25\3")
        buf.write("\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.")
        buf.write("\3/\6/\u012a\n/\r/\16/\u012b\3\60\7\60\u012f\n\60\f\60")
        buf.write("\16\60\u0132\13\60\3\60\5\60\u0135\n\60\3\60\6\60\u0138")
        buf.write("\n\60\r\60\16\60\u0139\3\60\5\60\u013d\n\60\3\60\6\60")
        buf.write("\u0140\n\60\r\60\16\60\u0141\3\60\5\60\u0145\n\60\3\60")
        buf.write("\7\60\u0148\n\60\f\60\16\60\u014b\13\60\3\60\5\60\u014e")
        buf.write("\n\60\5\60\u0150\n\60\3\61\3\61\5\61\u0154\n\61\3\61\6")
        buf.write("\61\u0157\n\61\r\61\16\61\u0158\3\62\3\62\5\62\u015d\n")
        buf.write("\62\3\63\3\63\3\63\7\63\u0162\n\63\f\63\16\63\u0165\13")
        buf.write("\63\3\63\3\63\3\63\3\64\3\64\3\64\7\64\u016d\n\64\f\64")
        buf.write("\16\64\u0170\13\64\3\64\5\64\u0173\n\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\7\65\u017a\n\65\f\65\16\65\u017d\13\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\5}\u016e\u017b\2\67\3\3\5\2")
        buf.write("\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16")
        buf.write("\35\17\37\20!\21#\22%\2\'\2)\23+\2-\2/\24\61\25\63\26")
        buf.write("\65\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%")
        buf.write("S&U\'W(Y)[*]+_,a\2c-e.g/i\60k\61\3\2\13\5\2\13\f\16\17")
        buf.write("\"\"\t\2$$^^ddhhppttvv\4\2\f\f\17\17\4\2C\\c|\3\2\62;")
        buf.write("\4\2GGgg\6\2\n\f\16\17$$^^\3\2$$\4\3\f\f\16\17\2\u0197")
        buf.write("\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2)\3\2\2\2\2/")
        buf.write("\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3")
        buf.write("\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A")
        buf.write("\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2")
        buf.write("K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2")
        buf.write("\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2")
        buf.write("\2\2_\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2")
        buf.write("\2\2\2k\3\2\2\2\3n\3\2\2\2\5t\3\2\2\2\7w\3\2\2\2\t\u0085")
        buf.write("\3\2\2\2\13\u0090\3\2\2\2\r\u0098\3\2\2\2\17\u009e\3\2")
        buf.write("\2\2\21\u00a7\3\2\2\2\23\u00aa\3\2\2\2\25\u00af\3\2\2")
        buf.write("\2\27\u00b3\3\2\2\2\31\u00b9\3\2\2\2\33\u00bd\3\2\2\2")
        buf.write("\35\u00c4\3\2\2\2\37\u00cb\3\2\2\2!\u00d0\3\2\2\2#\u00d3")
        buf.write("\3\2\2\2%\u00d9\3\2\2\2\'\u00de\3\2\2\2)\u00e6\3\2\2\2")
        buf.write("+\u00f0\3\2\2\2-\u00f2\3\2\2\2/\u00f4\3\2\2\2\61\u00f6")
        buf.write("\3\2\2\2\63\u00f8\3\2\2\2\65\u00fa\3\2\2\2\67\u00fc\3")
        buf.write("\2\2\29\u00fe\3\2\2\2;\u0100\3\2\2\2=\u0103\3\2\2\2?\u0106")
        buf.write("\3\2\2\2A\u0109\3\2\2\2C\u010c\3\2\2\2E\u010e\3\2\2\2")
        buf.write("G\u0110\3\2\2\2I\u0113\3\2\2\2K\u0116\3\2\2\2M\u0118\3")
        buf.write("\2\2\2O\u011a\3\2\2\2Q\u011c\3\2\2\2S\u011e\3\2\2\2U\u0120")
        buf.write("\3\2\2\2W\u0122\3\2\2\2Y\u0124\3\2\2\2[\u0126\3\2\2\2")
        buf.write("]\u0129\3\2\2\2_\u014f\3\2\2\2a\u0151\3\2\2\2c\u015c\3")
        buf.write("\2\2\2e\u015e\3\2\2\2g\u0169\3\2\2\2i\u0176\3\2\2\2k\u0182")
        buf.write("\3\2\2\2mo\t\2\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2")
        buf.write("\2\2qr\3\2\2\2rs\b\2\2\2s\4\3\2\2\2tu\7^\2\2uv\t\3\2\2")
        buf.write("v\6\3\2\2\2wx\7\61\2\2xy\7,\2\2y}\3\2\2\2z|\13\2\2\2{")
        buf.write("z\3\2\2\2|\177\3\2\2\2}~\3\2\2\2}{\3\2\2\2~\u0080\3\2")
        buf.write("\2\2\177}\3\2\2\2\u0080\u0081\7,\2\2\u0081\u0082\7\61")
        buf.write("\2\2\u0082\u0083\3\2\2\2\u0083\u0084\b\4\2\2\u0084\b\3")
        buf.write("\2\2\2\u0085\u0086\7\61\2\2\u0086\u0087\7\61\2\2\u0087")
        buf.write("\u008b\3\2\2\2\u0088\u008a\n\4\2\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f")
        buf.write("\b\5\2\2\u008f\n\3\2\2\2\u0090\u0091\7d\2\2\u0091\u0092")
        buf.write("\7q\2\2\u0092\u0093\7q\2\2\u0093\u0094\7n\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097\7p\2\2\u0097\f")
        buf.write("\3\2\2\2\u0098\u0099\7d\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7c\2\2\u009c\u009d\7m\2\2\u009d\16")
        buf.write("\3\2\2\2\u009e\u009f\7e\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1")
        buf.write("\7p\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4")
        buf.write("\7p\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7g\2\2\u00a6\20")
        buf.write("\3\2\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7h\2\2\u00a9\22")
        buf.write("\3\2\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad")
        buf.write("\7u\2\2\u00ad\u00ae\7g\2\2\u00ae\24\3\2\2\2\u00af\u00b0")
        buf.write("\7h\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7t\2\2\u00b2\26")
        buf.write("\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\30")
        buf.write("\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\32\3\2\2\2\u00bd\u00be\7u\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7i\2\2\u00c3\34\3\2\2\2\u00c4\u00c5")
        buf.write("\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7w\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7p\2\2\u00ca\36")
        buf.write("\3\2\2\2\u00cb\u00cc\7x\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7k\2\2\u00ce\u00cf\7f\2\2\u00cf \3\2\2\2\u00d0\u00d1")
        buf.write("\7f\2\2\u00d1\u00d2\7q\2\2\u00d2\"\3\2\2\2\u00d3\u00d4")
        buf.write("\7y\2\2\u00d4\u00d5\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7n\2\2\u00d7\u00d8\7g\2\2\u00d8$\3\2\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd&\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3(\3\2\2\2\u00e4\u00e7\5+\26\2\u00e5\u00e7")
        buf.write("\7a\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7")
        buf.write("\u00ed\3\2\2\2\u00e8\u00ec\5+\26\2\u00e9\u00ec\5-\27\2")
        buf.write("\u00ea\u00ec\7a\2\2\u00eb\u00e8\3\2\2\2\u00eb\u00e9\3")
        buf.write("\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb")
        buf.write("\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee*\3\2\2\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00f0\u00f1\t\5\2\2\u00f1,\3\2\2\2\u00f2\u00f3")
        buf.write("\t\6\2\2\u00f3.\3\2\2\2\u00f4\u00f5\7-\2\2\u00f5\60\3")
        buf.write("\2\2\2\u00f6\u00f7\7/\2\2\u00f7\62\3\2\2\2\u00f8\u00f9")
        buf.write("\7,\2\2\u00f9\64\3\2\2\2\u00fa\u00fb\7\61\2\2\u00fb\66")
        buf.write("\3\2\2\2\u00fc\u00fd\7#\2\2\u00fd8\3\2\2\2\u00fe\u00ff")
        buf.write("\7\'\2\2\u00ff:\3\2\2\2\u0100\u0101\7~\2\2\u0101\u0102")
        buf.write("\7~\2\2\u0102<\3\2\2\2\u0103\u0104\7(\2\2\u0104\u0105")
        buf.write("\7(\2\2\u0105>\3\2\2\2\u0106\u0107\7?\2\2\u0107\u0108")
        buf.write("\7?\2\2\u0108@\3\2\2\2\u0109\u010a\7#\2\2\u010a\u010b")
        buf.write("\7?\2\2\u010bB\3\2\2\2\u010c\u010d\7>\2\2\u010dD\3\2\2")
        buf.write("\2\u010e\u010f\7@\2\2\u010fF\3\2\2\2\u0110\u0111\7>\2")
        buf.write("\2\u0111\u0112\7?\2\2\u0112H\3\2\2\2\u0113\u0114\7@\2")
        buf.write("\2\u0114\u0115\7?\2\2\u0115J\3\2\2\2\u0116\u0117\7?\2")
        buf.write("\2\u0117L\3\2\2\2\u0118\u0119\7*\2\2\u0119N\3\2\2\2\u011a")
        buf.write("\u011b\7+\2\2\u011bP\3\2\2\2\u011c\u011d\7}\2\2\u011d")
        buf.write("R\3\2\2\2\u011e\u011f\7\177\2\2\u011fT\3\2\2\2\u0120\u0121")
        buf.write("\7]\2\2\u0121V\3\2\2\2\u0122\u0123\7_\2\2\u0123X\3\2\2")
        buf.write("\2\u0124\u0125\7=\2\2\u0125Z\3\2\2\2\u0126\u0127\7.\2")
        buf.write("\2\u0127\\\3\2\2\2\u0128\u012a\5-\27\2\u0129\u0128\3\2")
        buf.write("\2\2\u012a\u012b\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c^\3\2\2\2\u012d\u012f\5-\27\2\u012e\u012d")
        buf.write("\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2")
        buf.write("\u0133\u0135\7\60\2\2\u0134\u0133\3\2\2\2\u0134\u0135")
        buf.write("\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u0138\5-\27\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u013d\5")
        buf.write("a\61\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u0150")
        buf.write("\3\2\2\2\u013e\u0140\5-\27\2\u013f\u013e\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\u0144\3\2\2\2\u0143\u0145\7\60\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0149\3\2\2\2\u0146")
        buf.write("\u0148\5-\27\2\u0147\u0146\3\2\2\2\u0148\u014b\3\2\2\2")
        buf.write("\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014d\3")
        buf.write("\2\2\2\u014b\u0149\3\2\2\2\u014c\u014e\5a\61\2\u014d\u014c")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f")
        buf.write("\u0130\3\2\2\2\u014f\u013f\3\2\2\2\u0150`\3\2\2\2\u0151")
        buf.write("\u0153\t\7\2\2\u0152\u0154\7/\2\2\u0153\u0152\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0157\5")
        buf.write("-\27\2\u0156\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159b\3\2\2\2\u015a\u015d")
        buf.write("\5%\23\2\u015b\u015d\5\'\24\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015dd\3\2\2\2\u015e\u0163\7$\2\2\u015f")
        buf.write("\u0162\n\b\2\2\u0160\u0162\5\5\3\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0166\u0167\7$\2\2\u0167\u0168\b\63\3\2\u0168")
        buf.write("f\3\2\2\2\u0169\u016e\7$\2\2\u016a\u016d\n\t\2\2\u016b")
        buf.write("\u016d\5\5\3\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2")
        buf.write("\u016d\u0170\3\2\2\2\u016e\u016f\3\2\2\2\u016e\u016c\3")
        buf.write("\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173")
        buf.write("\t\n\2\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\b\64\4\2\u0175h\3\2\2\2\u0176\u017b\7$\2\2\u0177")
        buf.write("\u017a\n\b\2\2\u0178\u017a\5\5\3\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017b\u0179\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u017f\7^\2\2\u017f\u0180\n\3\2\2\u0180")
        buf.write("\u0181\b\65\5\2\u0181j\3\2\2\2\u0182\u0183\13\2\2\2\u0183")
        buf.write("l\3\2\2\2\35\2p}\u008b\u00e6\u00eb\u00ed\u012b\u0130\u0134")
        buf.write("\u0139\u013c\u0141\u0144\u0149\u014d\u014f\u0153\u0158")
        buf.write("\u015c\u0161\u0163\u016c\u016e\u0172\u0179\u017b\6\b\2")
        buf.write("\2\3\63\2\3\64\3\3\65\4")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENTS = 2
    COMMENT = 3
    BOOLEAN = 4
    BREAK = 5
    CONTINUE = 6
    IF = 7
    ELSE = 8
    FOR = 9
    FLOAT = 10
    INT = 11
    STRING = 12
    RETURN = 13
    VOID = 14
    DO = 15
    WHILE = 16
    ID = 17
    ADD = 18
    SUB = 19
    MUL = 20
    DIV = 21
    NOT = 22
    MODULE = 23
    OR = 24
    AND = 25
    NEQ = 26
    EQ = 27
    LSS = 28
    GRR = 29
    LSSEQ = 30
    GRREQ = 31
    ASN = 32
    LB = 33
    RB = 34
    LP = 35
    RP = 36
    LQ = 37
    RQ = 38
    SM = 39
    CM = 40
    INTLIT = 41
    FLOATLIT = 42
    BOOLIT = 43
    STRINGLIT = 44
    UNCLOSE_STRING = 45
    ILLEGAL_ESCAPE = 46
    ERROR_CHAR = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'float'", "'int'", "'string'", "'return'", "'void'", "'do'", 
            "'while'", "'+'", "'-'", "'*'", "'/'", "'!'", "'%'", "'||'", 
            "'&&'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENTS", "COMMENT", "BOOLEAN", "BREAK", "CONTINUE", 
            "IF", "ELSE", "FOR", "FLOAT", "INT", "STRING", "RETURN", "VOID", 
            "DO", "WHILE", "ID", "ADD", "SUB", "MUL", "DIV", "NOT", "MODULE", 
            "OR", "AND", "NEQ", "EQ", "LSS", "GRR", "LSSEQ", "GRREQ", "ASN", 
            "LB", "RB", "LP", "RP", "LQ", "RQ", "SM", "CM", "INTLIT", "FLOATLIT", 
            "BOOLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "WS", "ESCAPE", "COMMENTS", "COMMENT", "BOOLEAN", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "FOR", "FLOAT", "INT", "STRING", 
                  "RETURN", "VOID", "DO", "WHILE", "TRUE", "FALSE", "ID", 
                  "Letter", "Digit", "ADD", "SUB", "MUL", "DIV", "NOT", 
                  "MODULE", "OR", "AND", "NEQ", "EQ", "LSS", "GRR", "LSSEQ", 
                  "GRREQ", "ASN", "LB", "RB", "LP", "RP", "LQ", "RQ", "SM", 
                  "CM", "INTLIT", "FLOATLIT", "Exponent", "BOOLIT", "STRINGLIT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.STRINGLIT_action 
            actions[50] = self.UNCLOSE_STRING_action 
            actions[51] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            					temp = str(self.text)
            					self.text = temp[1:-1]
            				
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            	
            					newline = ['\r','\n','\f'] 
            					if (self.text[-1] in newline):
            						self.text=self.text[1:-1]
            					else:
            						self.text= self.text[1:]

            				
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            					temp = str(self.text)
            					self.text = temp[1:]
            				
     


