# Programa para classificar o consumo de água



print("=== Consumo de Água ===")



tipo = input("Digite o tipo de imóvel (comercial, casa ou apartamento): " ).strip().lower()

consumo = float(input("Digite o consumo mensal de água em m³: " ).replace(",", "."))



if tipo == "comercial":
  
    mensagem = "Tarifa comercial aplicada – consulte o plano corporativo."
  
elif tipo == "apartamento" and consumo < 10:
  
    mensagem = "Consumo econômico – excelente controle de água!"
  
elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
  
    mensagem = "Consumo moderado – dentro do padrão residencial."
  
else:
  
    mensagem = "Consumo excessivo – adote medidas de economia e verifique vazamentos."
  


print("\nResultado:")

print(mensagem)









