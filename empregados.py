def cadastrar():
    arquivo = open('empregado.txt', 'w')
    
    num_emps = int(input("Quantos empregados? "))

    for n in range(1, num_emps + 1):
        nome = input(('Nome: '))
        id_emp = input('ID: ')
        dept = input('Departamento: ')
        arquivo.write(nome + "\n")
        arquivo.write(id_emp + "\n")
        arquivo.write(dept + "\n \n")

    arquivo.close()

def consultar():
    arquivo = open('empregado.txt', 'r')
    nome = arquivo.readline()
    while nome != '':
        id_emp = arquivo.readline()
        dept = arquivo.readline()

        nome = nome.rstrip('\n')
        id_emp = id_emp.rstrip('\n')
        dept = dept.rstrip('\n')

        print("Nome: ", nome)
        print("ID: ", id_emp)
        print("Dept: ",dept)

        nome = arquivo.readline()
    arquivo.close()        
def main():   
    cadastrar()

main()
