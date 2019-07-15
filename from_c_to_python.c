#include<stdio.h>
#include <stdlib.h>
#include <math.h>
int main(void)
{
    int num = 40;
    int R = 10;

    int theta_division = 20;

    int i;

    double data[num][2];
    for(i = 0; i < theta_division; i++){
        data[i][0] = R * cos((2.0 * M_PI) /(1.0 * theta_division)*i);
        data[i][1] = R * sin((2.0 * M_PI) /(1.0 * theta_division)*i);
        //printf("%d, %23.15e %23.15e\n", i, data[i][0], data[i][1]);
    }

    i = 0;

    FILE *fp;
    int c;
    fp = fopen( "data_1.txt", "a");
    fprintf(fp, "%d\n", theta_division);	


        /* ファイルを開くのに失敗したら */
        /* プログラムを終了して、シェルに戻る */
    for(i = 0; i < theta_division; i++){
        //printf("%d, %23.15e %23.15e\n", i, data[i][0], data[i][1]);
        fprintf(fp, "%f %f\n", data[i][0], data[i][1]);			
    }
    fclose(fp);                       /* ファイルを閉じる */


    // pythonのプログラムを呼び出し
    system("cul_normal_vectors_for_c_process.py");
    system("rm data_1.txt");//cによって生成された座標データを削除

    double normal_vec[num][2];//これはグローバルで宣言をしておく．
    fp = fopen("normal.txt", "r");//pythonのプログラムによって算出されたnormal_vectorのデータを配列に読み込む
    for(i =0; i < num; i++){
        fscanf(fp, "%lf, %lf", &normal_vec[i][0], &normal_vec[i][1]);
    }

    for(i =0; i < num; i++){
        printf("%f, %f\n", normal_vec[i][0], normal_vec[i][1]);
    }
    system("rm normal.txt");//pythonによって生成されたnormal_vectorのデータを削除


    return 0;
}