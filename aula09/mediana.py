def mediana(lst):
    if (len(lst)%2)!=0:
        m1=int((len(lst)-1)/2)
        print("O valor mediano é: ",lst[m1])
    else:
        m1=int(len(lst)/2)
        m2=int((len(lst)/2)-1)
        print("Os valores medianos são: ",lst[m1]," e ",lst[m2])








def main():
    lst =[]
    x=1
    while True:
        print("Se pretender acabar a lista insira o valor 00!")
        x=input("Insira o número que pretende adicionar á lista!\n")
        if x=="00":
            break
        else:
            lst.append(x)
            print (lst)
            print("")
    if len(lst)==0:
        print("Por favor insira valores á lista!")
    else:
        mediana(lst)

main()