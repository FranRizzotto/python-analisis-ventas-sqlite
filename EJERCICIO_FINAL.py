import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
#OBTENIENDO LOS 10 PRODUCTOS MAS RENTABLES
conn=sqlite3.connect("northwind.db")
query='''SELECT ProductName,SUM(price*quantity)as Revenue 
FROM OrderDetails as od 
join products p on p.ProductID=od.ProductID
group by od.ProductID
order by revenue DESC
limit 10
'''
top_products=pd.read_sql_query(query,conn)#hace todo automaticamente, la consulta, y el armado.query es la consulta y con esto la ejecutamos

#para verlo con graficas----------

top_products.plot(x="ProductName",y="Revenue", kind="bar",figsize=(10,5),legend=False)
#esto basicamente es para armar el grafico , donde kind es el tipo, lo definimos con barras, y figsize el tamaño.
plt.title("10 productos rentables")
plt.xlabel("Productos")
plt.ylabel("revenue")
plt.xticks(rotation=90)# le dice que los nombres los rote 90 grados.
plt.show()
#si vemos al ejecutar el codigo, tiene los nombres para el eje x y el eje y, y tamb rotados 90 º 

#OBTENIENDO LOS 10 EMPLEADOS MAS EFECTIVOS
#|| "" || a esto se le llama concatenar
#count cuenta filas,asi que le damos * para que nos cuente todas las filas
query2='''
SELECT FirstName || " " || LastName as Employee , COUNT(*) as total
FROM Orders o
JOIN Employees e
ON e.EmployeeID=o.EmployeeID
group by o.EmployeeID
order by total desc
limit 10
'''
top_employees=pd.read_sql_query(query2,conn)
top_employees.plot(x="Employee",y="total",kind="bar",figsize=(10,5),legend=False)#en x e y se le pasan los as del select

plt.title("10 empleados mas efectivos")
plt.xlabel("empleados")
plt.ylabel("total vendido")
plt.xticks(rotation=45)
plt.show()
