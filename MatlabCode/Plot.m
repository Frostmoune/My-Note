t = [-4:0.01:4];
y1 = 2*sin(2*pi*t);
y2 = 2*cos(2*pi*t);
y3 = 2*t;
plot (t, y1);
hold on                                         % 若无这个语句，则会在把原图清空并画新图
plot (t, y2, 'r');                              
plot (t, y3, 'g');                              % plot用于描点画图，第一个参数是自变量，第二个参数是因变量，第三个参数是图的颜色
xlabel ('x')                                    % 在横轴上标记x
ylabel ('y')                                    % 在纵轴上标记y
legend ('sin', 'cos', '2x')                     % 注明不同的曲线
title ('New Plot')                              % 注明图的标题
print -dpng 'New Plot.png'                      % 存储图片
hold off
close                                           % 关闭图片
figure (1);
plot (t, y1);
figure (2);
plot (t, y2);                                   % 将函数画在不同的画布里
close
subplot (2,3,1);
plot (t, y1, 'b');
axis ([0, 2, -2, 2]);
subplot (2,3,2);                                % 将画布分成2*2的网格然后选择第2块
plot (t, y2, 'r');
axis ([0, 2, -2, 2]);
subplot (2,3,3);
plot (t, y3, 'g');
axis ([0, 2, 1, 4]);                            % 改变当前网格的横纵坐标（横坐标变为0.5~1.5，纵坐标变为1~2）
y4 = normpdf(t);                                % 标准正态分布函数
                                                % 但例如normpdf(2, 2, 4)则得到N(2, 4)在自变量为2时的值
subplot (2,3,4);
plot (t, y4, 'r');
hold on
tx = [-1:0.01:1];
yx = normpdf(tx);
area (tx, yx);                                  % 画出下方面积
hold off
print -dpng 'New Plot_2.png'
close
A = magic(10);
imagesc(A)                                      % 在图上画出矩阵，根据值决定颜色深浅
colorbar                                        % 在图右方得到颜色深浅和矩阵的值对应表
colormap gray                                   % 将颜色定为灰色
print -dpng 'New Plot_3.png'
close