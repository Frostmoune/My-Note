void insertsort(int arr[], int n) {
	int now=0,j=0;
	for (int i = 1; i < n; ++i) {
		now = arr[i];j = i - 1;//找到arr[i]在arr[0]~arr[i-1]中应该有的位置
		while (j >= 0 && arr[j] > now) {
			arr[j + 1] = arr[j];
			j--;//若满足arr[j]>now，后值赋值给前值
		}
		arr[j + 1] = now;//将now放到它应该的位置
	}
}