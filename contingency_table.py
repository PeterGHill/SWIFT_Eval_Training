def contingency_table(forecast,obs):#12.07.2019

   a=[]
   b=[]
   c=[]
   d=[]
   for l in range(len(forecast)):
       
       if obs[l]==1 and forecast[l]==1:
            a.append(1)
       elif obs[l]==0 and forecast[l]==1:
            b.append(1)
       elif obs[l]==1 and forecast[l]==0:
            c.append(1)
       elif obs[l]=0 and forecast[l]==0:
            d.append(1)
            

   
   
   return a,b,c,d
   

def hr_far_csi(forecast,obs):
    
    a,b,c,d=contingency_table(forecast,obs)
    
    
    hr=len(a)/(len(a)+len(c))
    
    far=len(a)/(len(a)+len(b))
    
    csi=len(a)/(len(a)+len(b)+len(c))
    
    
    return hr,far,csi
   