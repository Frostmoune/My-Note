import java.lang.Math;//引入Math,注意要有分号
public class loop_array {
	public static int[] toodds(int num) {
		int []array=new int[(int)(Math.ceil(num/2))];//向上取整函数
		int j=0;
		for(int i=1;i<=num;++i) {
			if(i%2==1) {
				array[j++]=i;
			}
		}
		return array;//java有可以返回数组的函数
	}
	public static void main(String []args) {
		char []strs={'H','E','L','L','O',' ','W','O','R','L','D'};
		char strsa[]={'H','E','L','L','O',' ','W','O','R','L','D'};
		//常量数组的定义方法
		for(char x:strs)System.out.printf("%c ",x);
		//java的for循环和while循环语法和c++基本相同，这是一种特别的for循环方法
		System.out.print("\n");
		String s[][] = new String[2][];
		s[0] = new String[2];
		s[1] = new String[3];
		s[0][0] = new String("Good");
		s[0][1] = new String("Luck");
		s[1][0] = new String("to");
		s[1][1] = new String("you");
		s[1][2] = new String("!");
		//数组的另一种定义方式,以二维数组为例
		for(String []p:s) {
			for(String q:p) {
				System.out.println(q);
			}
		}//二维数组的遍历方法
		int []myodds=toodds(20);
		for(int x:myodds) {
			System.out.printf("%d ",x);
		}
		System.out.print("\n");
	}
}
