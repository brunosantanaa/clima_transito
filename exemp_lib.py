
# coding: utf-8

# # BaltarTec - Testes e Exemplos
# 
# Utilizaremos este notebook para testar e simular aplicações dos métodos desenvolvidos por nós. Descrever ao máximo as etapadas dos testes para que todos possam acompanhar o processo de criação.

# # Classes:
# 
# ## data
# 
# #### Argumentos
# 
# - **latitude**: Latitude do local a ser analizado
# - **longitude**: Latitude do local a ser analizado
# 
# ## Métodos:
# - [wazeScraping](#wazeScraping)
# - [clima](#clima)

# In[1]:


from baltar_met import data

#Cria o objeto dt a partir da classe data
dt = data(-8.055312, -34.897963)


# ## wazeScraping
# 
# ### Retorna
# - **severity**: Número de pontos congestionados por nível de congestionamento [1..4]

# In[2]:


#Armazena o número de pontos congestionados
trafic_severity = dt.wazeScraping()
#Imprime na tela
for i in range(0, len(trafic_severity)):
    print("Grau {0} ->  {1} data points".format(i+1, trafic_severity[i]))


# ## clima
# 
# ### Retorna
# 
# - dict{main, name, visibility, cod, weather, sys, dt, wind, coord, clouds, base, id}
# 
# ### Descrição:
# 
# - **'main'**: dict{'pressure', 'temp_max', 'temp', 'temp_min', 'humidity'} 
# - **'name'**: str
# - **'visibitility'**: int
# - **'cod'**: int (webcode)
# - **'weather'**: array(dict{'icon', 'description', 'id', 'main'})
# - **'sys'**: dict{'message', 'sunrise', 'sunset', 'country', 'type', 'id'}
# - **'dt'**: longInt
# - **'wind'**: dict{'speed', 'deg'}
# - **'coord'**: dict{'lon', 'lat'}
# - **'clouds'**: dict{'all'}
# - **'base'**: str
# - **'id'**: longInt

# In[3]:


#Exemplo de utilização:

#Armazena resposta do método
weather_location = dt.clima()
#Recupera a temperatura em Celsius
temperatura = weather_location['main']['temp']
print('Temperatura: {0} C'.format(temperatura))
#Recupera as condições climáticas
condicao = weather_location['weather'][0]['main']
descricao = weather_location['weather'][0]['description']
print('Condição Climática: '+condicao+ ' ('+descricao+')')

