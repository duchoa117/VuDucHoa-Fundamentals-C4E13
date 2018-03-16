b = int(input('How many B bacterias are there? '))
time = int(input('How much time in minutes will we wait? '))
print('After',time, 'minutes, we would have',b*(2**(1/2*time))//1,'bacterias.')
