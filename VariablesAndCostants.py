import Constant


var = "Codekul"
varInt = 10
varFloat = 10.2
varBool = True

# var = 30

print(var)

var1 = None
print(type(var1))

var = var + '- The Gurukul for Coders!'
print(var)

string = ''''Codekul' - "The gurukul for Coders!"'''

string = '''This
    is
        multiline
            String'''

string = ('Value: %d'%varInt)
string = ('Value1: {}\nValue2: {}'.format(varFloat, varInt))

print(string)

Constant.MY_CONST = 200
print(Constant.MY_CONST)