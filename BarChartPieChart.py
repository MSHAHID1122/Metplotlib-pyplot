import matplotlib.pyplot as plt 

departments =["CS","IT","ME","CIV"]
students= [220,150,200,210]

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.bar(departments,students,color=["green","blue","yellow","red"])
plt.xlabel('departments')
plt.ylabel('students')
plt.subplot(1,2,2)

plt.pie(students,labels=departments,autopct='%1.1f%%',colors=["green","blue","yellow","red"])
plt.tight_layout()
plt.show()