void bubble_sort(int arr[],int size){
    int temp=0;
    for(int i=0;i<size-1;++i){
        for(int j=0;j<size-i-1;++j){
            if(arr[j]>arr[j+1]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}

void improved_bubble_sort(int arr[],int size){
    int temp=0;
    bool flag=true;
    for(int i=0;i<size-1;++i){
        flag=false;
        for(int j=0;j<size-i-1;++j){
            if(arr[j]>arr[j+1]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
                if(flag==false)flag=true;//如果进行了交换就将flag置为true
            }
        }
        if(flag==false)return;//如果flag为false说明没有进行交换,即表示排序已经完成
    }
}