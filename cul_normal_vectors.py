import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
#import pandas as pd

def main(data_1):
    r = 10.0
    num = 40
    print(data_1)
    
    for i in range(0, num):
        if i == 0:
            a = np.array([data_1[num - 1][0],data_1[num - 1][1]])
        else:
            a = np.array([data_1[i-1][0],data_1[i-1][1]])
        b = np.array([data_1[i][0],data_1[i][1]]) 
        if i == num - 1:
            c = np.array([data_1[0][0],data_1[0][1]])
        else:
            c = np.array([data_1[i+1][0],data_1[i+1][1]])
        #print("aaaaaa")
        print(a)
        print(b)
        print(c)

        ba = a - b
        ab = b - a
        bc = c - b

        ab_c = ab[0] + ab[1]*1.0j
        bc_c = bc[0] + bc[1]*1.0j

        gamma_h = 2.0 * (ab_c * bc_c)/(ab_c + bc_c)
        gamma_vec = np.array([np.real(gamma_h), np.imag(gamma_h)])
        rad = np.pi / 2.0
        rot = np.array([[np.cos(rad), -np.sin(rad)],
                    [np.sin(rad), np.cos(rad)]])
        normal_gamma = np.dot(rot, gamma_vec)
        unit_normal_gamma = normal_gamma / np.linalg.norm(normal_gamma)

        cross = np.cross(ba,bc)
        n_ba = np.linalg.norm(ba, ord=2)
        n_bc = np.linalg.norm(bc, ord=2)
        vec_add = ab + bc
        n_vec_add = np.linalg.norm(vec_add, ord=2)
        sin = math.fabs(cross) / (n_ba * n_bc)
        kappa = (2.0 * sin)/(math.fabs(n_vec_add))
        #kappa = (2.0 * sin)/(n_ba + n_bc)
        R = 1.0 / kappa

        print("-----------------------------------------")
        print("culcuration unit_normal_vector")
        print("gamma_h =")
        print(gamma_h)
        print("gamma_vec =")
        print(gamma_vec)
        print("normal_gamm =")
        print(normal_gamma)
        print("unit_normal_gamma =")
        print(unit_normal_gamma)

        print("-----------------------------------------")
        print("norm of vector from O to  circul point ")
        print("n_a = %f" % np.linalg.norm(a, ord=2))
        print("n_b = %f" % np.linalg.norm(b, ord=2))
        print("n_c = %f" % np.linalg.norm(c, ord=2))


        print("-----------------------------------------")
        print("on circul vector")
        print("ab = ")
        print(ab)
        print("bc = ")
        print(bc)

        print("-----------------------------------------")
        print("cross of vector_ba and vector_bc")
        print("cross = %f" % cross)

        print("-----------------------------------------")
        print("sin of vector_ba and vector_bc")
        print("sin = %f" % sin)

        print("-----------------------------------------")
        print("curvatrue")
        print("kappa = %f" % kappa)

        print("-----------------------------------------")
        print("curvatue radius")
        print("R = %f" % R)

        plt.quiver(b[0],b[1],unit_normal_gamma[0],unit_normal_gamma[1],angles='xy',scale_units='xy',scale=1)
        #plt.quiver(a[0],a[1],ab[0],ab[1],angles='xy',scale_units='xy',scale=1)
        #plt.quiver(b[0],b[1],bc[0],bc[1],angles='xy',scale_units='xy',scale=1)
    plt.subplot().set_aspect('equal')
    # グラフ表示
    plt.xlim([-(r+2), r+2])
    plt.ylim([-(r+2), r+2])
    plt.grid()
    plt.draw()
    plt.show()

    

if __name__ == '__main__':
    data_1 = np.loadtxt("sample_1.csv",       # 読み込みたいファイルのパス
                  delimiter=",",    # ファイルの区切り文字
                  skiprows=0,       # 先頭の何行を無視するか（指定した行数までは読み込まない）
                  usecols=(0,1) # 読み込みたい列番号
                 )
    main(data_1)