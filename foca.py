def jogar():


  print("*********************************") 
  print("Bem vindo ao jogo da foca!")
  print("*********************************")

  palavra_secreta = "Banana"
  letras_acertadas = ["_","_","_","_","_","_"]

  acertou = False
  enforcou = False

  print(letras_acertadas) 
  # for chances in range (1,6):
  #   print("Você deve acertar a palavra secreta!!!")
  while (not acertou and not enforcou):
    
    chute = input("Qual letra?: ")
    # chute = chute.strip()
    
    index = 0
    for letra in palavra_secreta:
      if chute.upper() == letra.upper():
        letras_acertadas [index] = letra
      index = index + 1
      
    print(letras_acertadas)

    if "".join(letras_acertadas) == palavra_secreta:
      print("Você acertou e a palavra é","".join(letras_acertadas))
      acertou = True
      

    print("Jogando...")  
      
print("Fim do jogo")
   


    

  






if (__name__ == "__main__"):
  jogar()