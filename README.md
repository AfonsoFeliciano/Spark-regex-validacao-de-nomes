# Aplicação de regex para validação de nomes em spark

Realização de regex no dataframe abaixo, transformando-o de: 

| nome  |
| ------------- |
| Maria Jose  | 
| Joaozinho |
|Jorge |
|1121as00 |
|Funcionario |
|SAHJSHS_asj@_ |
|SHAJSHGDU154 |
|**** |

Para: 

| nome  | nome_validado
| ------------- | -------------
| Maria Jose  | Maria Jose
| Joaozinho | Joaozinho
|Jorge | Jorge
|1121as00 |
|Funcionario |
|SAHJSHS_asj@_ |
|SHAJSHGDU154 |
|**** |


Para isso, foi utilizada a expressão em um código spark: 

```
^(?=.{1,40}$)[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$
```

