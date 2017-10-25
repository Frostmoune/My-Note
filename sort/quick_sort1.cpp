void qsort(int arr[],int beg, int end) {
	if (beg >= end)return;
	int nowb = beg, nowe = end;
	int num = arr[(beg+end)/2];
	arr[(beg+end)/2]=arr[beg];
	arr[beg]=num;
	//每次都取中间的数作为基准数,并将它与当前数组的第一个数交换
	while (nowb<nowe) {
		while (nowb<nowe&&arr[nowe] >= num)--nowe;
		arr[nowb] = arr[nowe];//把小于num的第一个数和num交换位置
		while (nowb<nowe&&arr[nowb] <= num)++nowb;
		arr[nowe] = arr[nowb];//把大于num的第一个数和num交换位置
	}//重复以上过程直到nowe>=nowb
	arr[nowb] = num;//把num放到它的最终位置，这时num左边的数小于num,右边的数大于num
	qsort(arr,beg, nowb - 1);
	qsort(arr,nowb + 1, end);//将数组以num的位置分块，继续排序
}//一种快排

#include <ctime>
#include <cstdlib>

using namespace std;

void qsort_b(int arr[],int beg, int end) {
	if (beg >= end)return;
	int nowb = beg, nowe = end;
	srand(time(0));
	int pos = beg+rand()%(end-beg+1);
	int num=arr[pos];
	arr[pos]=arr[beg];
	arr[beg]=num;
	//每次都取一个随机的数作为基准数,并将它与当前数组的第一个数交换
	while (nowb<nowe) {
		while (nowb<nowe&&arr[nowe] >= num)--nowe;
		arr[nowb] = arr[nowe];
		while (nowb<nowe&&arr[nowb] <= num)++nowb;
		arr[nowe] = arr[nowb];
	}
	arr[nowb] = num;
	qsort(arr,beg, nowb - 1);
	qsort(arr,nowb + 1, end);
}//一种快排的优化方法,尽量避免由于选取基准数导致的最坏情况