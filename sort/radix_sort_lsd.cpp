/*原理如下：
以81 43 56 71 24 55 32 14 31为例
第一步：将这组数据按在数组中的顺序依次按个位数排列，并记录下相应数字的个数
1:81 71 31 3个
2:32 1个
3:43 1个
4:24 14 2个
5:55 1个
6:56 1个
7:0个
8:0个
9:0个

第二步：将排列后的数据按顺序复制到辅助数组中，再将辅助数组的内容复制到原数组中
第一次排列的结果为：
81 71 31 32 43 24 14 55 56

第三步：将这组数据按在数组中的顺序依次按十位数排列，并记录下相应数字的个数
1:14 1个
2:24 1个
3:31 32 2个
4:43 1个
5:55 56 2个
6:0个
7:71 1个
8:81 1个

第四步：将排列后的数据按顺序复制到辅助数组中，再将辅助数组的内容复制到原数组中
第二次排列的结果为：
14 24 31 32 43 55 56 71 81

这时候整个数列已经排序完毕；如果排序的对象有三位数以上，则持续进行以上的动作直至到数组中最大数的最高位数为止。*/
#include <cstring>

int maxdig(int arr[],int n){
	int num=0;
	for(int i=0;i<n;++i){
		if(num<arr[i])num=arr[i];
	}
	int dig=0;
	while(num){
		num/=10;
		dig++;
	}
	return dig;
}//得到数组内最大数的最高位数

void lsd(int arr[],int n){
	int max=maxdig(arr,n);
	int count[10];//记录在当前位数下0-9的出现次数
	int *tmp=new int [n];//辅助数组
	int nowrad=1;
	for(int i=0;i<max;++i){
		memset(count,0,sizeof(count));//注意：计数器必须清零
	    int k=0;
		for(int j=0;j<n;++j){
			k=(arr[j]/nowrad)%10;//k为arr数组上第j个数在nowrad位上的数字
			count[k]++;//k每出现一次便++
		}
		for(int j=1;j<10;++j)count[j]=count[j-1]+count[j];//记录某个数在数组tmp上的位置
		for(int j=n-1;j>=0;--j){//注意，必须从后往前
			k=(arr[j]/nowrad)%10;
			tmp[count[k]-1]=arr[j];//将arr[j]的内容复制到tmp的相应位置上
			count[k]--;
		}
		for(int j=0;j<n;++j)arr[j]=tmp[j];//将辅助数组的内容复制到arr中
		nowrad*=10;
	}
	delete []tmp;
}//此算法只适用于非负整数的排序