import csv
from Sklejane import spline_interpolation, evaluate_spline
from Lagrange import Lagrange
import matplotlib.pyplot as plt
import numpy as np
import glob
folder_path = 'paths'
csv_files = glob.glob(folder_path + '/*.csv')
# Ścieżka do pliku CSV
#csv_file = 'p_w/2018_paths/Hel_yeah.csv'




def getTable(arr1,arr2):
    arr = []
    for i in arr1:
        arr.append(arr2[i])
    return arr

def zageszczona_tablica_srodek(array, num_points):
    dis1 = len(array)//3
    dis2 = 2*dis1
    dis3 = len(array)-1
    num = num_points//4
    indx1 = np.linspace(0,dis1,num,endpoint=False).astype(int)
    indx2 = np.linspace(dis1,dis2,num_points - 2*num).astype(int)
    indx3 = np.linspace(dis2,dis3,num+1).astype(int)
    indx3 = indx3[1:]
    array1 = getTable(indx1,array)
    array2 = getTable(indx2,array)
    array3 = getTable(indx3,array)
    x = np.concatenate((array1,array2,array3))
    return x


def zageszczona_tablica_brzegi(array, num_points):
    dis1 = len(array)//6
    dis2 = 5*dis1
    dis3 = len(array)-1
    num = int(num_points/3)
    indx1 = np.linspace(0,dis1,num,endpoint=False).astype(int)
    indx2 = np.linspace(dis1,dis2,num_points - 2*num).astype(int)
    indx3 = np.linspace(dis2,dis3,num+1).astype(int)
    indx3 = indx3[1:]
    array1 = getTable(indx1,array)
    array2 = getTable(indx2,array)
    array3 = getTable(indx3,array)
    x = np.concatenate((array1,array2,array3))
    return x


for csv_file in csv_files:
    print("Dane z pliku:", csv_file)
    # Listy przechowujące dane o odległościach i wysokościach
    distances = []
    heights = []

    # Wczytanie danych z pliku CSV
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            distance = float(row[0])
            height = float(row[1])
            distances.append(distance)
            heights.append(height)
    for l in range(8):
        fig, axs = plt.subplots(2, 3, figsize=(10, 6))
        # Wyświetlenie trasy na wykresie
        axs[0][0].plot(distances, heights, color='green', linewidth=1.5)
        axs[0][0].fill_between(distances, min(min(heights),0),heights, color='green', alpha=0.5)
        axs[0][0].set_xlabel('Odległość od startu [m]')
        axs[0][0].set_ylabel('Wysokość [m]')
        axs[0][0].set_title(f'Profil wysokościowy trasy: {csv_file}')
        num = [31,23,17,11,7]
        # METODA J
        xx = 0
        y = 1
        for j in num:
            if l == 0 or l == 4:
                distances2 = np.linspace(0,len(distances)-1,j).astype(int)
                distances2 = getTable(distances2,distances)
                heights2 = np.linspace(0,len(distances)-1,j).astype(int)
                heights2 = getTable(heights2,heights)
            elif l == 1 or l == 5:
                distances2 = zageszczona_tablica_srodek(distances,j)
                heights2 = zageszczona_tablica_srodek(heights,j)
            elif l == 2 or l == 6:
                distances2 = zageszczona_tablica_brzegi(distances,j)
                heights2 = zageszczona_tablica_brzegi(heights,j)
            if l == 3 or l == 7:
                distances2 = np.linspace(0,len(distances)-1,j).astype(int)
                distances2 = getTable(distances2,distances)
                heights2 = np.linspace(0,len(distances)-1,j).astype(int)
                heights2 = getTable(heights2,heights)
                heights2 = np.array(heights2)
                error_percentage = 5
                error = heights2 * (error_percentage / 100)
                heights2 = heights2 + np.random.uniform(-error, error)
            new_heights = []
            new_distances = np.linspace(min(distances),max(distances),512)
            if l < 4:
                for i in new_distances:
                    new_heights.append(Lagrange(distances2,heights2,i))
            else:
                cs = spline_interpolation(distances2, heights2)
                for i in new_distances:
                    new_heights.append(evaluate_spline(distances2,cs,i))
            axs[xx][y].plot(new_distances, new_heights, color='red', linewidth=1.5, label='Wartości interpolacji')
            axs[xx][y].plot(distances, heights, color='black', linewidth=1.5, label='Orginalne wartości')
            axs[xx][y].set_ylim(min(min(new_heights)-10,min(heights)-10,0), max(max(new_heights)+10, max(heights)+10))
            axs[xx][y].ticklabel_format(style='plain')
            axs[xx][y].scatter(distances2, heights2, color='red', label='Punkty węzłowe')
            axs[xx][y].fill_between(new_distances, min(min(new_heights)-10,min(heights)-10,0),new_heights, color='green', alpha=0.5)
            axs[xx][y].set_xlabel('Odległość od startu [m]')
            axs[xx][y].set_ylabel('Wysokość [m]')
            axs[xx][y].legend()
            axs[xx][y].set_title(f'Dla: {j} punktów')
            y += 1
            if y > 2:
                y = 0
                xx = 1
        if l == 0:
            fig.suptitle('Interpolacja Lagrange’a')
        if l == 1:
            fig.suptitle('Interpolacja Lagrange’a punkty gęstsze w środku')
        if l == 2:
            fig.suptitle('Interpolacja Lagrange’a punkty gęstsze na zewnątrz')
        if l == 3:
            fig.suptitle(f'Interpolacja Lagrange’a punkty z 5% błędem')
        if l == 4:
            fig.suptitle('Interpolacja splajnami trzeciego stopnia')
        if l == 5:
            fig.suptitle('Interpolacja splajnami trzeciego stopnia punkty gęstsze w środku')
        if l == 6:
            fig.suptitle('Interpolacja splajnami trzeciego stopnia punkty gęstsze na zewnątrz')
        if l == 7:
            fig.suptitle(f'Interpolacja splajnami trzeciego stopnia punkty z 5% błędem')
        plt.show()


