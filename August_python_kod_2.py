# Pyhton Code for distance calibrating
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Center med corners ger mitten
def length(length):
    """ Calculates the amount of frames between two corners in x-axle"""
    length = np.array(length)
    length = length[:, 0]
    length = np.sort(length)[::-1]  # Sorts them with largest first
    length = length[0] - length[2]  # Takes the first and the third because they are beside each other in x-led
    return length


"""Corners from different distances"""
xy50 = [[ 614.71228027,  547.74334717],
 [1253.18017578,  588.39764404],
 [1247.99523926,   31.4212265 ],
 [ 692.62005615,   -4.00332165]]


xy75 = [[ 712.93182373,  664.82598877],
 [1158.08862305,  690.87103271],
 [1165.30603027,  279.21682739],
 [ 755.96588135,  255.93232727]]


xy100 = [[ 768.8480835,   729.71472168],
 [1103.07653809,  748.78253174],
 [1108.2722168 ,  438.58023071],
 [ 795.28741455,  415.69290161]]


xy125 = [[ 817.17376709,  754.67822266],
 [1090.36364746,  786.43035889],
 [1114.29553223,  525.30078125],
 [ 852.59558105,  495.24688721]]


xy150 = [[ 829.74536133,  779.26013184],
 [1056.95178223,  809.34790039],
 [1082.80969238,  589.04772949],
 [ 861.89001465,  559.91296387]]


xy175 = [[ 848.11486816,  805.33300781],
 [1045.72253418,  820.01696777],
 [1057.80725098,  628.53295898],
 [ 864.64782715,  614.13616943]]


xy200= [[ 863.40136719,  820.67834473],
 [1035.87329102,  831.69732666],
 [1045.35266113 , 664.18762207],
 [ 876.18591309 , 653.58288574]]



xy225 =  [[ 865.49304199,  834.84216309],
 [1018.03588867,  840.13537598],
 [1021.84313965,  690.83990479],
 [ 871.18572998 , 686.05633545]]



xy250 = [[ 877.86346436,  840.39300537],
 [1016.90258789 , 848.74780273],
 [1023.93426514 , 715.06341553],
 [ 887.82159424 , 706.44604492]]



xy275 =  [[ 878.00531006 , 850.39666748],
 [1004.7800293 ,  852.41156006],
 [1005.36114502 , 730.31774902],
 [ 880.9855957  , 727.58612061]]



xy300 =  [[ 893.42126465 , 852.37561035],
 [1009.13818359 , 861.61816406],
 [1017.92071533 , 750.38702393],
 [ 904.27905273 , 741.34570312]]



xy325 = [[ 897.44689941,  857.94555664],
 [1003.97595215 , 864.17504883],
 [1008.87811279 , 761.16473389],
 [ 903.95916748 , 754.50079346]]


xy350 =   [[ 902.88128662 , 860.74627686],
 [1002.3427124 ,  868.60809326],
 [1009.58782959 , 771.56976318],
 [ 911.1897583  , 763.83087158]]


xy375 = [[ 904.66101074 , 865.79400635],
 [ 996.37121582 , 871.28833008],
 [1000.30505371 , 782.60479736],
 [ 910.14678955 , 776.56970215]]



xy400 = [[907.29150391, 867.43389893],
 [993.60021973, 873.26635742],
 [998.86303711, 788.82678223],
 [913.22753906, 783.02593994]]


xy425 = [[ 925.17529297,  859.7243042 ],
 [1006.12896729,  868.67883301],
 [1014.77838135,  789.48901367],
 [ 934.38641357,  780.56671143]]


xy450 = [[922.68603516, 867.3918457 ],
 [999.42358398 ,866.46459961],
 [998.34655762, 790.89819336],
 [921.64202881, 792.19665527]]


xy475 = [[ 927.63140869 , 866.81878662],
 [ 999.92675781,  870.91229248],
 [1004.38641357,  800.32739258],
 [ 932.07568359 , 795.94061279]]

xy500 = [[ 933.93713379 , 867.8961792 ],
 [1002.5425415  , 874.56634521],
 [1009.17449951 , 807.22039795],
 [ 940.44561768 , 800.72259521]]


""" Calculates the distance between corners for each distance so it is possible to plot"""
measurement = [0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]
corners_size = [xy50,xy75,xy100,xy125,xy150,xy175,xy200,xy225,xy250,xy275,xy300,xy325,xy350,xy375,xy400,xy425,xy450, xy475, xy500]
distance_corners = []
for corners in corners_size:
    distance = length(corners)
    distance_corners.append(distance)


def length_corners(measurement):
    measurement = np.array(measurement)
    center_160 = measurement[0] - measurement[1]
    return center_160

""" Center point from different distances center_x_y
    x = distance from camera, y = distance to the right from the first measuring """
center50 = [953.40980565, 271.5997654 ]
center50_L = [633.22755024, 259.68489549] # moved 16cm to the left
center50_x = [center50[0], center50_L[0]]

center75 = [948.42054058, 464.09260189]
center75_L = [711.50795843, 449.42113541]
center75_x = [center75[0], center75_L[0]]

center100 = [945.47003764, 578.22065373]
center100_L = [754.30118642, 561.90525189]
center100_x = [center100[0], center100_L[0]]

center125 = [968.83307185, 637.59752588]
center125_L = [777.27044312 ,635.75132048]
center125_x = [center125[0], center125_L[0]]

center150 = [958.02255555, 682.8423033 ]
center150_L = [834.07111574, 676.27669438]
center150_x = [center150[0], center150_L[0]]

center175 = [954.16563802, 715.91735505]
center175_L = [895.80638477, 707.86083644]
center175_x = [center175[0], center175_L[0]]

center200 = [955.2052575 , 741.72063673]
center200_L = [853.25595098, 736.37741203]
center200_x = [center200[0], center200_L[0]]

center225 = [944.04078615, 762.49777244]
center225_L = [864.93634893, 757.88869718]
center225_x = [center225[0], center225_L[0]]

center250 = [951.78866016 ,776.96476085]
center250_L = [861.16390127 ,777.03630905]
center250_x = [center250[0], center250_L[0]]

center275 = [942.48681076, 789.59954054]
center275_L = [873.58135871 ,786.82208455]
center275_x = [center275[0], center275_L[0]]

center300 = [956.22512726 ,800.92737396]
center300_L = [889.6016119 , 793.68351921]
center300_x = [center300[0], center300_L[0]]

center325 = [953.7222851  ,809.06896307]
center325_L = [895.30754159, 805.24889077]
center325_x = [center325[0], center325_L[0]]

center350 = [956.51145067 ,815.92661609]
center350_L = [899.84178653, 811.7300155 ]
center350_x = [center350[0], center350_L[0]]

center375 = [953.05347561 ,823.70324201]
center375_L = [900.99038173, 820.01884565]
center375_x = [center375[0], center375_L[0]]

center400 = [953.26005279 ,827.97343605]
center400_L = [899.45801142 ,827.22190372]
center400_x = [center400[0], center400_L[0]]

center425 = [970.14026623 ,824.47855522]
center425_L = [906.6010968 , 830.15815781]
center425_x = [center425[0], center425_L[0]]

center450 = [960.4298988 , 829.23236847]
center450_L = [913.07580014, 823.05393982]
center450_x = [center450[0], center450_L[0]]

center475 = [966.07898909, 833.5123824 ]
center475_L = [925.56732959, 830.70647256]
center475_x = [center475[0], center475_L[0]]

center500 = [971.47584307, 837.62278391]
center500_L = [929.36085484 ,834.38810887] 
center500_x = [center500[0], center500_L[0]]


center_x = [center50_x, center75_x, center100_x, center125_x, center150_x, center175_x, center200_x, center225_x, center250_x, 
            center275_x, center300_x, center325_x, center350_x, center375_x, center400_x, center425_x, center450_x , center475_x, center500_x]

center_distance = []
for center in center_x:
    length_center = np.array(length_corners(center))
    center_distance.append(length_center)
center_distance = np.array(center_distance)

measurement_corners =  [0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5] #In meters
mean_distance = center_distance

""" Make the values in to a function"""
function_turn = np.polyfit(measurement_corners, mean_distance, 2)

def func_2(x, a, b, c):
    return a * x ** 2 + b * x + c

""" Does go against 0 with 2, tries exponantial instead """
def func(x, a, b, c):
    return a*np.exp(-b*x)+c

popt_corners, pcov = curve_fit(func, distance_corners, measurement, p0=(5, 1e-6, 1)) 
print(popt_corners)

""" Ploting the estimated function for distance"""

plt.plot(distance_corners, measurement, 'ro')
x = np.linspace(30, 800,1000)
plt.plot(x,func(x,*popt_corners))
plt.ylabel('Distance from camera to tag')
plt.xlabel('Frames')
plt.title('Function for distance from camera to tag')
plt.legend(['measured values', 'approximated function with curve_fit'])
plt.show()


""" Ploting the estimated function distance for turns"""
popt_center, pcov = curve_fit(func, measurement_corners, mean_distance, p0=(400, 1, 40)) 
print(popt_center)

plt.plot(measurement_corners, mean_distance, 'ro')
x = np.linspace(0.2, 6 ,1000)
plt.plot(x, func(x, *popt_center))
plt.xlabel('Distance')
plt.ylabel('Number of frames on 8cm')
plt.title('Function for distance from tag to middle line')
plt.legend(['measured values', 'approximated function with curve_fit'])
plt.show()