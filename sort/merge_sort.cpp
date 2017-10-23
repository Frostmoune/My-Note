void merge(int arr[],int beg,int mid,int end){
	int *tmp=new int[end-beg+1];//辅助数组
    int i=beg,j=mid+1,p=0;
    //当前被划分好的数组又可以被划分成arr[beg~mid]、arr[mid+1~end]两个部分,
    //由于这两个部分已经被处理过,所以这两部分内部元素一定是有序的
	while(i<=mid&&j<=end){
		if(arr[i]<arr[j])tmp[p++]=arr[i++];
        else tmp[p++]=arr[j++];
        //将当前被划分的数组内的元素放到辅助数组中,使得辅助数组里面的元素是有序的
	}
	while(i<=mid)tmp[p++]=arr[i++];
	while(j<=end)tmp[p++]=arr[j++];//将剩余的元素放入辅助数组里
    for(int k=beg;k<=end;++k)arr[k]=tmp[k-beg];
    //将辅助数组中的值放回到原来被划分好的数组中,使得当前数组有序
}//合并部分

void mergesort(int arr[],int beg,int end,int n){
	if(end-beg<1)return;
	int mid=(end+beg)/2;
	mergesort(arr,beg,mid,n);
	mergesort(arr,mid+1,end,n);//将数组二分
	merge(arr,beg,mid,end);//将二分的两个数组合并
} //划分+合并部分