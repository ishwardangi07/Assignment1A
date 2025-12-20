#Assignment-1A

print("Program to find the equation of best fit line of three data points")

try:
    x, y = map (int,input("Enter first data point (x,y): ").split(','))
    x1, y1 = map (int,input("Enter second data point (x,y): ").split(','))
    x2, y2 = map (int,input("Enter third data point (x,y): ").split(','))
except ValueError:
    print("Error! Please use format: x,y (e.g., 1,2)")
    exit()

learning_rate = 0.01
target = 0.001
count = 0
N=3

m = 0
c = 0


error1=m*x+c-y
error2=m*x1+c-y1
error3=m*x2+c-y2

cost= (1/(2*N))  *((error1**2)+(error2**2)+(error3**2))

while cost > target and count < 1000: #program repea untill it reach target and prevent the infinite loop
    dm= (1/N)*(error1*x+error2*x1+error3*x2)   #partial derivative of m =(1/N)* sume of (error*x)
    dc= (1/N)*(error1+error2+error3)

    m= m-learning_rate*dm
    c=c-learning_rate*dc

    error1=m*x+c-y
    error2=m*x1+c-y1
    error3=m*x2+c-y2


    cost= (1/(2*N))*((error1**2)+(error2**2)+(error3**2))
    count=count+1

print(f"The equation for the best fit line for given data points is y={m:.3f}x+{c:.3f} with cost function of {cost}")
 
    