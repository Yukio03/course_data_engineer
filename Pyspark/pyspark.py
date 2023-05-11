#!/usr/bin/env python
# coding: utf-8

# In[170]:


from pyspark.sql import *
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType, DateType

spark = SparkSession.builder.appName("Python Spark SQL basic example").config("spark.driver.bindAddress","localhost").config("spark.ui.port","4040").getOrCreate()


# In[224]:


from datetime import datetime
from pyspark.sql.functions import from_unixtime, when, col, udf, size


# In[246]:


schema = StructType(fields=[
    StructField("id", IntegerType()),
    StructField("timestamp", IntegerType()),
    StructField("type", StringType()),
    StructField("page_id", IntegerType()),
    StructField("tag", StringType()),
    StructField("sign", BooleanType())
])

data = [
    (12345, 1667127426, "click", 101, "Sport", False),
    (12341, 1667921868, "click", 102, "Politics", False),
    (12341, 1667622974, "move", 102, "Politics", False),
    (12345, 1667629145, "scroll", 101, "Sport", False),
    (12342, 1667327123, "click", 102, "Politics", False),
    (12342, 1667627345, "scroll", 102, "Politics", True),
    (12342, 1667627567, "visit", 103, "Medicine", True),
    (12347, 1667620765, "click", 102, "Politics", False),
    (12347, 1667690869, "click", 103, "Medicine", False),
    (12342, 1667027868, "click", 102, "Politics", True),
    (12343, 1667699425, "scroll", 101, "Sport", True),
    (12343, 1667259425, "click", 103, "Medicine", True)
     
]

df = spark.createDataFrame(data=data, schema=schema)
df.show()


# In[247]:


df.groupBy("id").count().orderBy("count", ascending=False).show() 
# Вывести топ-5 самых активных посетителей сайта


# In[248]:


users_sign = df.filter(df["sign"] == "True").select("id").distinct() 
count_sign = users_sign.count()
total_count = df.select("id").distinct().count()
print((count_sign / total_count)*100, "%", sep="")
# Посчитать процент посетителей, у которых есть ЛК


# In[249]:


df.filter(df["type"] == "click").select("page_id").groupBy("page_id").count().orderBy("count", ascending=False).show()
# Вывести топ-5 страниц сайта по показателю общего кол-ва кликов на данной странице


# In[251]:


def convert_time(time):
    if time[0] == '0':
        time = int(time[-1])
        if time > 0 and time <= 4:
            return "0-4"
        elif time > 4 and time <= 8:
            return "4-8"
        elif time > 8 and time <= 10:
            return "8-12"
    elif time[0] != '0':
        time = int(time)
        if time >= 10 and time <= 12:
            return "8-12"
        elif time > 12 and time <= 16:
            return "12-16"
        elif time > 16 and time <= 20:
            return "16-20"
        elif time > 20 and time <= 24:
            return "20-24"


# In[252]:


# Функция для перевода часов в промежутки как в задании 0-4, 4-8
func = udf(convert_time, StringType())


# In[253]:


row = df.select(from_unixtime('timestamp')[12:12][1:2].alias('ts'))


# In[254]:


df = df.withColumn("hour", from_unixtime('timestamp')[12:12][1:2])


# In[255]:


df = df.withColumn("ts", func("hour"))
df = df.drop("hour")
df.show()
# Добавьте столбец к фрейму данных со значением временного диапазона в рамках суток с размером окна – 4 часа(0-4, 4-8, 8-12 и т.д.)


# In[256]:


df.groupBy("ts").count().orderBy("count", ascending=False).show(1)
# Выведите временной промежуток на основе предыдущего задания, в течение которого было больше всего активностей на сайте.


# In[257]:


schema_users = StructType(fields=[
    StructField("id", IntegerType()),
    StructField("user_id", IntegerType()),
    StructField("name", StringType()),
    StructField("date_birth", DateType()),
    StructField("date_create", DateType())
])

data_users = [
    (1, 12343, "Иванов Иван Иванович", datetime(1990, 10, 10), datetime(2022, 12, 12)),
    (2, 12342, "Петров Петр Петрович", datetime(1995, 8, 10), datetime(2022, 12, 13)),
    (3, 12345, "Андреев Андрей Андреевич", datetime(1999, 5, 2), datetime(2022, 12, 14))
]

users = spark.createDataFrame(data=data_users, schema=schema_users)
users.show()
# Создайте второй фрейм данных, который будет содержать информацию о ЛК посетителя сайта со следующим списком атрибутов


# In[264]:


cond = [users.user_id == df.id, df.tag == "Sport", df.type == "scroll"]
surname = users.join(df, cond, "inner").select(users.name)
surname.show()
# Вывести фамилии посетителей, которые читали хотя бы одну новость про спорт.

