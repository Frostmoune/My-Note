import java.io .*;

public class test {
	public static char read_a() {
		char a='\0';
		try {
			a=(char)System.in.read();
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return a;
	}//一个一个字符输入的方法
	public static String read_b() {
		BufferedReader buff=new BufferedReader(new InputStreamReader(System.in));
		String str="";
		try {
			str=buff.readLine();
		}
		catch(Exception e) {
			e.printStackTrace();
		}//注意异常处理必不可少
		return str;
	}//一行一行读取字符串的方法
	public static void main(String []args) {
		char a=0;
		for(int i=0;i<10;++i) {
			a=read_a();
			System.out.printf("%c", a);
		}
		System.out.print("\n");
		String str;
		for(int i=0;i<10;++i) {
			str=read_b();
			System.out.println(str);
			System.out.print("\n");
		}
	}
}