public class data_type_test{
    public static void main(String []args){
        byte a=0;//不同于c++的byte类型,是八位整数,只占1byte
        System.out.println("byte size:"+Byte.SIZE/8);//得到byte的size
        System.out.println("byte min_value:"+Byte.MIN_VALUE);//得到byte能表示的最小值
        System.out.println("byte max_value:"+Byte.MAX_VALUE);//得到byte能表示的最大值
        boolean b=false;//同C++的bool
        String str="Hello World";//同c++的string,注意S要大
        System.out.println("String size:"+str.length());//得到str的size
        final double pi=3.1415;//这样用final定义的变量是常量
        //pi=6.2;//这一语句会报错
        System.out.println(pi);
    }
}
