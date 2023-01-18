def func2(arg5, arg6):
    var34 = var9(arg6, arg5)
    var39 = func8(arg6, arg5)
    var43 = func9(var34, var39)
    var44 = var34 | (var34 ^ arg5) - -1756965019
    var45 = var44 ^ var39
    var46 = (var34 - arg5) | var43 ^ var34
    var47 = var34 | var46
    var48 = var46 + 249264413
    var49 = ((-567 + var47) | var45) ^ -1492464189
    var50 = var47 - (899 ^ var45) | -432499775
    var51 = ((-266 + var49) + var46) ^ var34
    var52 = var51 ^ var43
    var53 = var45 ^ var34 & var46 & var51
    var54 = var46 - var48 + var52
    var55 = var39 & var53 | var39
    var56 = (var45 | var44 + var50) | var51
    var57 = var49 + 197 | var54 & var51
    var58 = (var34 | arg5) + var47 ^ arg6
    result = (var53 ^ (var52 ^ var39) + (var47 & (var55 - var49) - arg6 ^ var43 + var58) ^ var58 & var46) - var54
    return result
def func8(arg35, arg36):
    var37 = 0
    for var38 in xrange(29):
        var37 += arg36 ^ 8 + arg36
    return var37
def func5(arg10, arg11):
    var16 = func6(arg10, arg11)
    def func7(arg17, arg18):
        var19 = (arg18 - -692017079 - (arg11 | (arg10 - arg17) - -682) & arg17 ^ arg18 + arg17) + -1732347285
        var20 = var16 & 302357977
        var21 = (((var19 | 1074184599 | (arg18 ^ 1757859286) ^ -309) ^ 1730808176 + var16 & -625) - var20) ^ arg17 ^ (arg18 - ((-1567857151 | var16) | 495)) & ((-403959781 & (arg18 & (var20 | arg11) - var16) - arg18) + arg18 - 687)
        result = (var19 | (-89 | var20 ^ arg10 + var16 | arg10) | (arg18 | arg17)) & var21
        return result
    var22 = func7(arg10, arg11)
    var23 = -66595313 | var22
    var24 = 1297836215 | (761 ^ var22) ^ arg10
    var25 = arg10 ^ var16 - arg10 ^ arg10
    var26 = var22 ^ var25
    var27 = (var16 & 411) - 178
    var28 = var22 | var16 & 123
    var29 = var26 ^ ((var23 - var27) - var28)
    var30 = var26 | 897
    var31 = -674 + 176
    var32 = var16 | arg11
    var33 = ((var27 + var28) | var30) ^ 1316519049
    result = var22 + var32 | ((-781 - ((var26 | (var32 ^ var31)) - var29)) - var27 - var16)
    return result
def func6(arg12, arg13):
    var14 = 0
    for var15 in xrange(47):
        var14 += (arg13 + var15) | var15
    return var14
def func4():
    closure = [2]
    def func3(arg7, arg8):
        closure[0] += func5(arg7, arg8)
        return closure[0]
    func = func3
    return func
var9 = func4()
def func1(arg1, arg2):
    var3 = 1315298825 & -1031061574
    var4 = (((((arg1 & var3 ^ (((arg2 & arg2 - ((arg1 + ((arg2 | var3) | (arg2 - -651039155))) & 234 ^ var3) & arg2 + arg1) | 794903845) ^ arg1)) | var3) + arg1) + var3) | var3) ^ arg2 ^ -919 ^ 552698391
    result = arg2 + arg2 ^ var4 ^ arg2 | ((var3 ^ arg1 | (((445 ^ var4) & arg1) + arg1)) & arg2) ^ arg2
    return result
def func9(arg40, arg41):
    def func10(acc, rest):
        var42 = acc | 7
        if acc == 0:
            return var42
        else:
            result = func10(acc - 1, var42)
            return result
    result = func10(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 5'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 59'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
