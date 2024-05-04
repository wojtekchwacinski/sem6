import random
import sympy
def trywialny(n=10, t=10, k=100, s=90):

    #rozbijanie sekretu
    zbior = []

    while len(zbior) != n - 1:
        x = random.randint(0, k-1)
        if x not in zbior:
            zbior.append(x) 

    s_n = (s - sum(zbior))%k

    zbior.append(s_n)

    #odzyskiwanie sekretu

    sekret = sum(zbior)% k

    print(f"Sekret: {sekret}")




def shamir(s=38099, t=5, n=8):
    prime = sympy.randprime(3000, 6000)
    
    a_list = []
    for i in range(t-1):
        a = random.randint(1, prime - 1)  
        a_list.append(a)
    s_list = []
    print(f"Wylosowana liczba pierwsza: {prime}")
    print(f"Wylosowane liczby do wielomianu: {a_list}")
    
    for j in range(1, n+1):
        suma = 0
        for k in range(len(a_list)):
            suma += a_list[k] * pow(j, k+1, prime)
        #print(suma)
        s_j = (s + suma)
        l = [j, s_j]

        s_list.append(l)
   

    print(f"Uzyskane udziały: {s_list}")

    # Odzyskiwanie sekretu
    t_udzialow = random.sample(s_list, k=t)
    print(t_udzialow)
    secret = 0

    for t_i in t_udzialow:
        x_i, y_i = t_i
        #print(x_i, y_i)
        numerator, denominator = 1, 1
        
        for t_j in t_udzialow:
            if t_i != t_j:
                x_j, y_j = t_j
                numerator *= -x_j
                denominator *= (x_i-x_j)
                
        secret += y_i * (numerator / denominator)
    secret = sympy.Mod(secret, prime)
    print("Odzyskany sekret:", secret)









if __name__ == "__main__":
    trywialny()
    shamir()
