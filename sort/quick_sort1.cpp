void qsort(int arr[],int beg, int end) {
	if (beg >= end)return;
	int nowb = beg, nowe = end;
	int num = arr[beg];
	while (nowb<nowe) {
		while (nowb<nowe&&arr[nowe] >= num)--nowe;
		arr[nowb] = arr[nowe];//把小于num的第一个数和num交换位置
		while (nowb<nowe&&arr[nowb] <= num)++nowb;
		arr[nowe] = arr[nowb];//把大于num的第一个数和num交换位置
	}//重复以上过程直到nowe>=nowb
	arr[nowb] = num;//把num放到它的最终位置，这时num左边的数小于num,右边的数大于num
	qsort(arr,beg, nowb - 1);
	qsort(arr,nowb + 1, end);//将数组以num的位置分块，继续排序
}//核心代码