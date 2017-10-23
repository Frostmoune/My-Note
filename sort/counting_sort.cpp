#include <vector>

using std::vector;

void countingsort(int arr[], int neg, int pos, int n) {
    //数的范围满足neg<=x<=pos
    int *tmp = new int[n];//辅助数组
	vector<int> positive_count, negative_count;//非负、负整数计数数组
	for (int i = 0; i < pos + 1; ++i)positive_count.push_back(0);
	for (int i = 0; i < -neg + 1; ++i)negative_count.push_back(0);
	for (int i = 0; i < n; ++i) {
		if (arr[i] >= 0) {
			positive_count[arr[i]]++;//记录数字出现次数
		}
		else {
			negative_count[-arr[i]]++;
		}
	}
	for (int i = 1; i < pos; ++i)positive_count[i] = positive_count[i - 1] + positive_count[i];
	for (int i = -neg - 2; i >= 0; --i)negative_count[i] = negative_count[i + 1] + negative_count[i];//找到对应数字在数组中应该出现的位置
	int k = negative_count[0];//非负数在数组中出现的位置是k+positive_count
	for (int i = n - 1; i >= 0; --i) {
		if (arr[i] >= 0) {
			positive_count[arr[i]]--;//每出现一次就将位置减一
			tmp[k + positive_count[arr[i]]] = arr[i];
		}
		else {
			negative_count[-arr[i]]--;
			tmp[negative_count[-arr[i]]] = arr[i];//tmp对应位置上置为arr[i]
		}
	}//排序部分,得到的tmp是有序的
	for (int i = 0; i < n; ++i)arr[i] = tmp[i];
	delete []tmp;
}//一种对整数有效的计数排序