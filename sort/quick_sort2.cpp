void swap(int &a, int &b) {
    if(a==b)return;
	int tmp = a;
	a = b;
	b = tmp;
}//交换两个数

int part(int arr[], int beg, int end) {
	if (end <= beg)return beg;
    int num = arr[end], i = beg - 1;
    //将当前数组的最后一个数作为排序的基准数
	for (int j = beg; j <= end - 1; ++j) {
		if (num >= arr[j]) {
            i++;
            //根据算法,必有i<=j
            if(i<j)swap(arr[i], arr[j]);
            //当i<j-1时,能够保证arr[i]>num,arr[j]<=num,
            //此时arr[i]经过上一次交换后第1个大于num的数
		}
	}
	swap(arr[i + 1], arr[end]);//将当前的基准数放到当前数组应有的位置
	return i + 1;//返回基准数的数组下标
}

void qsort(int arr[], int beg, int end) {
	if (end <= beg)return;
	int now = part(arr, beg, end);
    qsort(arr, beg, now - 1);
	qsort(arr, now + 1, end);//根据返回的数组下标进行划分并排序
}
