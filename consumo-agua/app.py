"""Classificador de consumo de água para imóveis."""





def ler_tipo_imovel():
  
    tipos_validos = {"comercial", "casa", "apartamento"}
  


    while True:
      
        tipo = input("Digite o tipo de imóvel (comercial, casa ou apartamento): " ).strip().lower()
      
        if tipo in tipos_validos:
          
            return tipo
          
        print("Tipo inválido. Escolha comercial, casa ou apartamento.")
      




def ler_consumo():
  
    while True:
      
        entrada = input("Digite o consumo mensal de água em m³: " ).strip().replace(",", ".")
      
        try:
          
            consumo = float(entrada)
          
            if consumo < 0:
              
                raise ValueError
              
            return consumo
          
        except ValueError:
          
            print("Consumo inválido. Digite um número decimal igual ou maior que zero.")
          




def classificar_consumo(tipo, consumo):
  
    """Retorna a mensagem correspondente às regras de negócio."""
  
    if tipo == "comercial":
      
        return "Tarifa comercial aplicada – consulte o plano corporativo."
      


    if tipo == "apartamento" and consumo < 10:
      
        return "Consumo econômico – excelente controle de água!"
      


    if (tipo == "apartamento" and consumo <= 25) or (
      
        tipo == "casa" and consumo <= 25
      
    ):
      
        return "Consumo moderado – dentro do padrão residencial."
      


    return "Consumo excessivo – adote medidas de economia e verifique vazamentos."
  




def main():
  
    print("\n=== Classificador de Consumo de Água ===")
  
    tipo = ler_tipo_imovel()
  
    consumo = ler_consumo()
  
    resultado = classificar_consumo(tipo, consumo)
  


    print(f"\nTipo de imóvel: {tipo}")
  
    print(f"Consumo mensal: {consumo:.2f} m³")
  
    print(f"Alerta educativo: {resultado}")
  




if __name__ == "__main__":
  
    main()
  






































