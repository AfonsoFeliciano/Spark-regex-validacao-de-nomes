# Databricks notebook source
from pyspark.sql.functions import col, regexp_extract, col
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

# COMMAND ----------

#Definição dos valores
data =  [("Maria Jose",), ('Joaozinho',), ('Jorge',), ('1121as00',),('/Funcionario',), ('SAHJSHS_asj@_',), ('SHAJSHGDU154',), ('****',)]

#Criação do dataframe
df = spark.createDataFrame(data, ["nome"])

#Exibição
df.display()

# COMMAND ----------

#Criação e exibição do regex
regex = "^(?=.{1,40}$)[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$"
print(regex)

# COMMAND ----------

#Utilização do regex
df = df.withColumn('nome_validado', regexp_extract(col('nome'), regex, 0))
df.display()
