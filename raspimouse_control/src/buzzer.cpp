#include <ros/ros.h>
#include <ros/package.h>
#include "std_msgs/UInt16.h"
#include <iostream>
#include <fstream>
#include <cmath>
#include <cassert>
#include <cstdlib>

using namespace std;

//static const double f1 = (double)100;			// 振動数1
//static const double f2 = (double)880;			// 振動数2
static const int t = 1;					// 時間
static const double pi = 3.141592653589793;		// 円周率
void callback_buzzer(const std_msgs::UInt16::ConstPtr& msg);
//int main(void);

void callback_buzzer(const std_msgs::UInt16::ConstPtr& msg)
{
	int riff_p = 0, data_p = 0, last_p = 0, fn = 0;
	double time = 0;
	short out = 0;
	int buf = 0; short buf2 = 0;

	ifstream ifs("/../../../../../../dev/rtbuzzer0");
	string str;
	if (ifs.fail())
	{
		cerr << "失敗" << endl;
		return;
	}
	while (getline(ifs, str))
	{
		ofstream of;
		of.open("output.wav", ios::out | ios::binary | ios::trunc);
		assert(of);

		of.seekp(0,ios::beg);	// ファイルポインタを頭へ

		of.write("RIFF",4);			// RIFFヘッダ
		riff_p = of.tellp();
		of.seekp(sizeof(char)*4, ios::cur);	// サイズを出力するための場所を空ける
		of.write("WAVE",4);			// WAVEヘッダ
		of.write("fmt ",4);			// fmt ヘッダ
		buf = 16;
		of.write((char*)&buf, 4);	// fmt ヘッダ長
		buf2 = 1;
		of.write((char*)&buf2, 2);	// リニアPCM
		buf2 = 1;
		of.write((char*)&buf2, 2);	// チャネル数
		buf = 44100;
		of.write((char*)&buf, 4);	// サンプリングレート
		buf = 88200;
		of.write((char*)&buf, 4);	// データ速度
		buf2 = 2;
		of.write((char*)&buf2, 2);	// ブロックサイズ
		buf2 = 16;
		of.write((char*)&buf2, 2);	// サンプルあたりのビット数
		cout << "data" << endl;
		of.write("data", 4);		// dataヘッダ
		data_p = of.tellp();
		of.seekp(sizeof(char)*4, ios::cur);		// 4バイト分進める

		cout << "初期化完了" << endl;
	
		while((int)time < t)
		{
			for(int i=0; i<44100; i++){
				/*if(time == 2.0)
					fn = f1 * exp( log( (double)(44100 + i)/(double)44100) );
				else if(time >= 3.0)
					fn = f2;
				else */
				//fn = atoi(str.c_str());
				fn = msg->data;
				out = (short)( (sin((double)2*pi*fn*(double)i/(double)44100) ) * (double)0x7FFF);
				of.write((char*) &out, sizeof(short));
			}
			cout << "t=" << time << endl;
			cout << "fn=" << fn << endl;
			cout << "-----" << endl;
			time = time + 1.0;
		}

		last_p = of.tellp();
		of.seekp(riff_p, ios::beg);
		buf = last_p - 8;
		of.write((char*)&buf, 4);
		of.seekp(data_p, ios::beg);
		buf = last_p - data_p - 4;
		of.write((char*)&buf, 4);

		of.close();
	}
}

int main(int argc, char **argv){
	ros::init(argc,argv,"buzzer");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscribe("buzzer", 10, callback_buzzer);

	ros::spin();
	exit(0);
}
