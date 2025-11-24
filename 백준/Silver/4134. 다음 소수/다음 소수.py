def isprime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True

num=int(input())
for _ in range(num):
    test= int(input())
    while True:
        if test==0 or test==1:
            print(2)
            break
        if isprime(test):
            print(test)
            break
        else:
            test+=1
# 출처: https://aaaaaaaaaaayowooji.tistory.com/34#google_vignette [Just code it:티스토리]