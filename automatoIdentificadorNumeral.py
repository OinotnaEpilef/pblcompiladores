with open ("entrada_exemplo_teste_lexico_meta_1.txt", "r") as example:
    file = example.readlines()
    for line in file:
        finalLine = line.split(' ')
        for word in finalLine:
            lexem = list(word)
            for letter in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                if lexem[0] == letter:
                    state = "initialId"
                    for caracter in lexem:
                        if caracter == letter:
                            state = "id"
                        elif caracter == 1 or caracter == 2 or caracter == 3 or caracter == 4 or caracter == 5 or caracter == 6 or caracter == 7 or caracter == 8 or caracter == 9 or caracter == 0:
                            state = 'id'
                        else:
                            state = 'not id'
                else:
                    print(word, ' não é um identificador')
            for number in '1234567890':
                if lexem[0] == number:
                    isFloat = False
                    state = 'initialNum'
                    for caracter in lexem:
                        if caracter == number:
                            state = 'num'
                        elif caracter == '.' and isFloat == False:
                            state = 'num'
                            isFloat = True
                        elif caracter == '.' and isFloat == True:
                            state = 'not num'
                        else:
                            state = 'not num'
                else:
                    print (word, ' não é um número')
            if state == 'id':
                print(word, ' é um identificador')
            elif state == 'not id':
                print(word, ' é um identificador mal formatado')
            elif state == 'num':
                print(word, ' é um número')
            elif state ==  'not num':
                print(word, 'não é um número')
        print('fim da linha')
    print('fim do arquivo')