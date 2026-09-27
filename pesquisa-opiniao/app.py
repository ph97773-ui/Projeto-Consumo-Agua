"""Pesquisa de opinião sobre atendimento ao cliente."""





def realizar_pesquisa(quantidade=50):
  
    excelentes = 0
  
    ruins = 0
  


    for numero in range(1, quantidade + 1):
      
        print(f"\nEntrevistado {numero} de {quantidade}")
      
        nome = input("Nome: ")
      
        idade = int(input("Idade: "))
      


        while True:
          
            opiniao = input("Opinião (1-Excelente, 2-Bom, 3-Ruim): ")
          
            if opiniao in ("1", "2", "3"):
              
                break
              
            print("Digite apenas 1, 2 ou 3.")
          


        if opiniao == "1":
          
            excelentes += 1
          
        elif opiniao == "3":
          
            ruins += 1
          


    print("\n--- Resultado da pesquisa ---")
  
    print(f"Respostas EXCELENTE: {excelentes}")
  
    print(f"Respostas RUIM: {ruins}")
  
    return excelentes, ruins
  




if __name__ == "__main__":
  
    print("PESQUISA DE OPINIÃO - TUDO WEB")
  
    print("A pesquisa será realizada com 50 entrevistados.")
  
    realizar_pesquisa()
  
























