% Basic Operation :
% 若无注明，其他基本运算符号用法和功能与cpp相同
A = 1;
B = 2;
a = 1, b = 2, c = 3                 % 可以用逗号来连接语句
A ~= B                              % 相当于不等号(注意不是!=)
xor (1,0)                           % 异或
B ^ 3                               % 乘方
a = pi;
a 
disp (a)                            % 将a的值显示到命令行
disp (sprintf ('test: %0.2f', a))   % C风格输出。输出test: 3.14
disp (sprintf ('test: %0.6f', a))
b = 'Hello Matlab'                  % 定义一个字符串
              