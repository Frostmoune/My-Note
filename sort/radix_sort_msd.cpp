#include <cstring>
#include <cmath>
#include <vector>

using std::vector;

// 与lsd相同之处，都是一位一位来排序，且都可以处理非负整数的排序
// 与lsd不同之处，msd是从高位到低位来排序，故需要用到递归
// 若需要支持负整数,则需要将正数和负数分别处理

int maxdig(int arr[], int n) {
	int max = arr[0];
	for (int i = 0; i < n; ++i) {
		if (max < arr[i])max = arr[i];
	}
	int dig = 0;
	while (max) {
		max /= 10;
		dig++;
	}
	return dig;
}

int counts[10];

void radixsort(int arr[], int beg, int end,int maxd) {
    //maxd记录当前的位,初始化为最高位；beg、end则是被分隔的数组的起点坐标和终点坐标
    if (maxd<1)return;
    vector<int> tmp;
    memset(counts, 0, sizeof(counts));
	int k = 0, nowdig = pow(10, maxd-1);
	for (int i = beg; i <= end; ++i) {
        tmp.push_back(0);
		k =(arr[i] /nowdig) % 10;
		counts[k]++;
	}//这里arr[beg~end]就相当于当前需要处理的桶
	int count[10];//新辅助数组保存下一次递归的边界
	count[0] = counts[0];
	for (int i = 1; i < 10; ++i) {
		counts[i] = counts[i] + counts[i - 1];
		count[i] = counts[i];
	}
	for (int j = end; j >= beg; --j) {
		k = (arr[j] / nowdig) % 10;
		tmp[counts[k] - 1] = arr[j];
		counts[k]--;
	}
	for (int i = beg,j=0; i <= end; ++i,++j) {
		arr[i] = tmp[j];//注意i从beg开始,j从零开始
	}
	for (int i = 0; i < 10; ++i) {
	    if (!i&&count[i])radixsort(arr, beg, beg+count[i]-1, maxd - 1);
        if (i&&count[i] != count[i - 1])radixsort(arr, beg+count[i - 1], beg+count[i] - 1, maxd - 1);
        //这里相当于分桶操作
	}
}