// 堆排序：建立一个最大堆(特性：每个父节点都一定比子节点大)
// heapsize是堆的长度(<=数组长度length)(亦可认为heapsize=length-数列中的有序序列的长度)
// 对于数列A[1]~A[length]中的每一个A[i](i<=length/2),均有一个左结点(left)和右结点(right),其中left=2*i,right=2*i+1

void swap(int &a, int &b) {
	if(a==b)return;
	int tmp = a;
	a = b;
	b = tmp;
}//交换两个元素

void maxheapify(int arr[], int heapsize, int beg) {
	int large, left = 2 * beg+1, right = left + 1;//注意数组是以0开始,left是左结点下标,right是右结点下标,beg是父节点下标
	if (left <= heapsize&&arr[left] > arr[beg])large = left;
	else large = beg;
    if (right <= heapsize&&arr[right] > arr[large])large = right;
    //large记录父节点、左结点和右结点中最大数的下标
	if (large != beg) {
		swap(arr[beg], arr[large]);//将父节点与子节点中最大的数交换位置
		maxheapify(arr, heapsize, large);//将large作为新的父节点的下标,将arr[large]移动到合理的位置
	}
}

void build(int arr[], int length) {
	for (int i = length / 2; i >= 0; --i) {
		maxheapify(arr, length, i);
	}
}//初始化一个堆,将最大的数移到arr[0],次大的数移到arr[1]、arr[2]以此类推

/*不管每一次堆中的最大元素的位置在哪,经过足够的maxheapify操作,总能找到它2*(0,heapsize/2)=(1,heapsize),通过递归将其不断移动
设其当前位置为pos,则它将移动到[0,pos/2]->[0,pos/4]->……直到其移动到位置0*/

void heapsort(int arr[],int length) {
	build(arr, length);
	int heapsize = length;
	for (int i = length; i >= 1; --i) {
		swap(arr[0], arr[i]);//i即为上一次当前的heapsize,arr[0]即为上一个堆中的最大值,进行这次交换后,使得arr[heapsize]~arr[n]变成有序的
		heapsize -= 1;//令heapsize减1
		maxheapify(arr, heapsize, 0);//从零开始maxheapify操作,arr[0]=max(arr[0],arr[1],arr[2]),以此类推
	}
}