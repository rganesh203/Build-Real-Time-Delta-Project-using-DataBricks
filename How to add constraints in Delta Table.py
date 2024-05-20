# Databricks notebook source
# MAGIC %md
# MAGIC #Not Null and Check Constraints

# COMMAND ----------

# MAGIC %md
# MAGIC ###Not Null

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.student

# COMMAND ----------

sql("drop table if exists deltalake.person")
spark.sql("""CREATE TABLE if not exists deltalake.person 
    (
    ID int NOT NULL,
    Name STRING,
    dept STRING
    ) 
    using DELTA
    partitioned by (dept)
    """)

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalake.person(id, Name, dept) values("hareesh","EEE")

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalake.person(id, Name, dept) values(1,"hareesh","EEE")

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table deltalake.person change column Id drop not null;

# COMMAND ----------

# MAGIC %md
# MAGIC ###Check 

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table deltalake.person add constraint dept_cnt check(dept="EEE");

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalake.person(id, Name, dept) values(2,"Naresh","IT")
