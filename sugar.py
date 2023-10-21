print("***************************SPECIFIC ROATION OF SUGAR SOLUTION***************************")
print()
print()
n=int(input("Enter number of readings taken for each solution(sugar and water): "))
water=[]
ssugar=[]
print()
for i in range(0,n):
    print("Enter reading of",i+1,"th angle for water solution")
    w=float(input())
    water.append(w)
print()
for i in range(0,n):
    print("Enter reading of",i+1,"th angle for sugar solution")
    s=float(input())
    ssugar.append(s)

sum=0
for i in range(0,n):
    sum+=(ssugar[i]-water[i])

avg=sum/n

L=float(input("Enter the length of the tube IN DECIMETERS: "))    #was 2dm in my case
C=float(input("Enter concentration of sugar solution IN GRAM PER CC: ")) #was 0.2 in my case
S=(avg)/(L*C)
print("The value of specific rotation for sugar solution is: ",S)