import lexer

SourceCode = open('SourceCode.txt', 'r')
SourceCode = SourceCode.read()
print(SourceCode)

text = SourceCode
result, error = lexer.run('SourceCode.txt', text)

if error:
    print(error.as_string())
else:
    print(result)
