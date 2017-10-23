void selectsort(int arr[],int size){
	int now;
	for(int i=0;i<size-1;++i){
		int tmp=0;
		now=i;//初始化要交换的数字下标
		for(int j=i+1;j<size;++j){
            if(arr[now]>arr[j])now=j;
            //从arr[i]~arr[size-1]选择一个最小的数,得到其数组下标
		}
		if(now!=i){
			tmp=arr[i];
			arr[i]=arr[now];
			arr[now]=tmp;
        }//如果now发生了改变,那么说明i+1~size-1中能找到一个比arr[i]小的数
        //便可以将这个最小的数和arr[i]互换
	}
}