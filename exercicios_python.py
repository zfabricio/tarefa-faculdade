import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temperaturas = [22, 24, 20, 21, 23, 25, 22]
dias = ['Seg','Ter','Qua','Qui','Sex','Sab','Dom']
plt.figure()
plt.plot(dias, temperaturas, marker='o')
plt.title('Temperatura da Semana')
plt.xlabel('Dia')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.savefig('temperaturas_semana.png') 
plt.close()

x = np.random.rand(50)
y = x * 2 + np.random.normal(0, 0.2, 50)
plt.figure()
plt.scatter(x, y)
plt.title('Scatter Exemplo')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('scatter_exemplo.png')
plt.close()

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array:\n", arr)
print("Média por coluna:", arr.mean(axis=0))
print("Desvio padrão por linha:", arr.std(axis=1))
print("Soma total:", arr.sum())

data = {
    'aluno': ['Ana','Bruno','Carlos','Diana'],
    'vendas': [150, 200, 50, 75],
    'idade': [22, 23, 21, 24]
}
df = pd.DataFrame(data)
print(df.head())
print(df.describe())

filtro = df[df['vendas'] > 100]
print("Filtro (vendas > 100):\n", filtro)

df.to_csv('dados_alunos.csv', index=False)
