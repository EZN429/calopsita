opcaopagamento =str(input("qual é a opção de pagamento"))
if opcaopagamento=="credito":
  print ("por favor insira ou aproxime o cartão de  credito") 
elif opcaopagamento=="debito":
  print ("por favor insira ou aproxim o cartão de debito")
elif opcaopagamento=="pix":
  print ("por favor escaneie o codigo QRcode")
elif opcaopagamento=="dinhero":
   print("pague no caixa e aguarde o troco")
elif opicaopagamento=="cheque":
  print("por favor ponha a sua assinatura")
else:
   print ("pagamento invalido")
