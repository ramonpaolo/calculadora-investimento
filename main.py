import json, locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

feeYear = 13.25 / 100
feeMonth = feeYear / 12

feeDay = feeMonth / 29

print('\n')

initialMoney = float(input('Quantidade de dinheiro investido: R$').replace('.', '').replace(',', ''))
quantityMounth = int(input('Quantidade de meses para simular: '))

firstAvenue = initialMoney * feeDay

lastMoneySavings = initialMoney + firstAvenue

allAvenuesDaily = [
  {
      'avenue': locale.currency(firstAvenue, grouping=True, symbol=False),
      'day': 1,
      'total_avenue': locale.currency(lastMoneySavings, grouping=True, symbol=False),
      'currency': 'BRL',
      'symbol': 'R$',
      'month': 1
  },
]

for x in range(2, 22 * quantityMounth, 1):
  avenue = lastMoneySavings * feeDay

  lastMoneySavings = lastMoneySavings + avenue 

  allAvenuesDaily.append({
      'avenue': locale.currency(avenue, grouping=True, symbol=False),
      'day': x,
      'total_avenue': locale.currency(lastMoneySavings, grouping=True, symbol=False),
      'currency': 'BRL',
      'symbol': 'R$',
      'month': (x / 22).__floor__() + 1
  })

with open('avenue.json', 'w') as file:
    json.dump(allAvenuesDaily, file, indent=2)

print('\n')

print('Juros anual: {:.2f}%'.format(feeYear * 100))
print('Juros mensal: {:.2f}%'.format(feeMonth * 100))
print('Juros diário: {:.3f}%'.format(feeDay * 100))

print('\n')

print(f'Primeiro dia de ganho: R${allAvenuesDaily[0]["avenue"]}')
print(f'Último dia de ganho: R${allAvenuesDaily[-1]["avenue"]}')

print('\n')
