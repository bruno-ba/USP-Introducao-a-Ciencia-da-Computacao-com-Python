MASSAS_ATOMICAS = {'H': 1, 'P': 31, 'O': 16, 'Ca': 40, 'C': 12, 'N': 14, 'Na': 23, 'Cl': 35.5}


if __name__ == '__main__':

   U_ALUMINIO = 27
   U_OXIGENIO = 16

   massa_aluminio_equacao = 2 * U_ALUMINIO
   massa_oxigenio_equacao = 3/2 * U_OXIGENIO * 2

   fator_aluminio_oxigenio = massa_oxigenio_equacao /massa_aluminio_equacao
   var_aluminio = 2.5
   print(f'massa  do alumínio na equação: {massa_aluminio_equacao}')
   print(f'massa  do oxigênio na equação: {massa_oxigenio_equacao}')
   print(f'para {var_aluminio} g de Alumíno, precisará de {fator_aluminio_oxigenio * var_aluminio:.2f} g de Oxigênio')

print('*****************************************************')





def calcular_massas(multiplicador = 1, **kwargs):
   soma_massas = 0
   for k, v in kwargs.items():
      soma_massas += MASSAS_ATOMICAS.get(k, 0) * v

   return soma_massas * multiplicador


massa_acido_fosforico = calcular_massas(2, H=3, P=1, O=4)

massa_reagente_acido_fosforico = calcular_massas(2, H=3, P=1, O=4)
massa_reagente_oxido_calcio = calcular_massas(3, Ca=1, O=1)
massa_reagentes = massa_reagente_acido_fosforico + massa_reagente_oxido_calcio
massa_produto_fosfato_calcio = calcular_massas(Ca=3, P=2, O=8)
massa_produto_agua = calcular_massas(3, H=2, O=1)
massa_produtos = massa_produto_fosfato_calcio + massa_produto_agua

print("\nReagentes:")
print(f'Massa do ácido fosfórico (H3PO4): {massa_reagente_acido_fosforico:.2f}')
print(f'Massa do óxido de cálcio (CaO): {massa_reagente_oxido_calcio:.2f}')
print(f'Massa dos reagentes : {massa_reagentes:.2f}')

print("\nProdutos:")
print(f'Massa do fosfato de cálcio : {massa_produto_fosfato_calcio:.2f}')
print(f'Massa do água : {massa_produto_agua:.2f}')
print(f'Massa dos produtos : {massa_produtos:.2f}')

print("\nEquação Química")
if massa_produtos != massa_reagentes:
   print('Erro de balanceamento!')
else:
   print('Equação Balanceada')

print('*' * 100)
massa_ureia =calcular_massas(C=1, O=1) + calcular_massas(2, N=1, H=2)
massa_amonia = calcular_massas(2, N=1, H=3)
print(f"Massa da ureia: {massa_ureia}")
print(f"Massa da amônia: {massa_amonia}")
print('*' * 100)

reagente_HCl = calcular_massas(H=1, Cl=1)
reagente_NaOH = calcular_massas(Na=1, O=1, H=1)
produto_NaCl = calcular_massas(Na=1, Cl=1)
produto_H2O = calcular_massas(H=2, O=1)

mr = reagente_HCl + reagente_NaOH
mp = produto_NaCl + produto_H2O

print('Massas dos Reagentes:')
print(f"Massa do HCl: {reagente_HCl}")
print(f"Massa do NaOH: {reagente_NaOH}")
print(f"Massa dos reagentes: {mr}")
print('\nMassas dos Produtos:')
print(f"Massa do NaCl: {produto_NaCl}")
print(f"Massa do H2O: {produto_H2O}")
print(f"Massa dos produtos: {mp}")

print("\nEquação Química")
if mr != mp:
   print('Erro de balanceamento!')
else:
   print('Equação Balanceada')

print( calcular_massas(Ca=1) + calcular_massas(2, Cl=1, O=3))