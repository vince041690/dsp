name= input ('Enter your name:')
math= input ('Type your math grade:')
sci= input ('Type your Science grade:')
eng= input ('Type your English grade:')
ave= (float(math)+float(sci)+float(eng))/3
print ('Math:',math +' Science:',sci +' English:',eng +' Your average is:', ave)
if ave>=75:
    print('Congratulations',name +', You passed:',ave)
elif ave<=74:
    print('Better luck next time',name + ', You failed:',ave)