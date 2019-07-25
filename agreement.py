def distance_scale (f1, f2):
#14.06.2019
#this calculate the distance between f1, f2
#f1 and f2 are the observed and forecast rainfall
if f1 > 0 or f2 > 0:
   D = (f1 - f2)**2 / ((f1) ** 2 + (f2) ** 2) 
elif f1 == 0 and f2 == 0:
   D = 1 
return D 


def Dcrit (alpha, maxscale, scale):

#alpha and maxscale can be chosen by the user
#alpha measures the tolerance about different can be f1 and f2 and maxscale is the maximum scale we are
#investigating the similarity between the fields

return alpha + (1 - alpha) * scale / maxscale 


def agreement_scale (f1, f2, alpha, maxscale, scale):

  D = distance_scale (f1, f2)
  Dcr = Dcrit (alpha, maxscale, scale) 
	if D<=Dcrit:
          return scale 

def eight_neighbor_average_convolve2d (x, scale):
  kernel = np.ones ((scale * 2 + 1, scale * 2 + 1))
#this is to calculate the spatial average for each neighbourhood size
  neighbor_sum = ndimage.convolve (x, kernel, mode = 'reflect')
  num_neighbor = ndimage.convolve (np.ones (x.shape), kernel, mode = 'reflect') 
  return neighbor_sum / num_neighbor 


def agreement_scale_calculation (maxscale, obs, forecast):
#this is the main code to calculate the agreement scale
#obs and forecast are the rainfall accumulations over a certain time window.
  for s in range (maxscale, -1, -1):
  print s, 'scale' f1 = eight_neighbor_average_convolve2d (obs, s) f2 = eight_neighbor_average_convolve2d (forecast,: ,:], s)
      for i in range (len (latitude): #this is to calculate the agreement scale at each point
        for j in range (len (longitude)):


	 if distance_scale(f1[i, j], f2[i, j])<= Dcrit (alpha, maxscale, s):
            agr_scale[i, j] = s
		      
return agr_scale		      
