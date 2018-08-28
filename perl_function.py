                                                             字符串函数
$name = uc($name);                        所有小写变大写
$name = ucfirst($name);                  只把第一个字母变大写
$name = lc($name);                         所有大写变小写
$name = lcfirst($name);                   只把第一个字母变小写
$size = length($string);                    得到字符串的长度;
$part = substr($whole, 4, 5)             截取字符串的第四到第五
chomp($var);                                    删除行尾(一般是删除换行符以及下面内容)
chop($var);                                       删除最后一个字符
$code = crypt($word, $salt);             拷贝(把$word的值拷贝给$salt)
eval $var;                                          把字符串当作perl代码来执行
$pos = index($string, $substring);    打印字符串(substring)在字符串(string)的什么位置
$pos = rindex($string, $substring);   最后面的substring在string的什么位置
$quote = quotemeta($string);           引用字符串

                                                          数组函数
@found = grep(/[Jj]ohn/, @users);    过滤出符合要求的元素,与unix中的grep类似
@new = map(lc($_), @start);            把数组各元素作为操作对象
$string = join(‘’, @arr);                       把数组中的元素组合成字符串,用给定的分隔符分割元素
@data = split(/&/,$ENV{‘QUERY_STRING’})   把一个字符串分割成一个数组
sort(@salery);                                    按字母顺序排序数组
reverse(@salery);                              将数组的次序颠倒
keys(%hash);                                     获取哈希的键
values(%hash);                                  获取哈希的值
each(%hash);                                     获取哈希的键和值
@arr = ();                                           清空数组
delete $hash{$key};                           删除哈希中的某个元素
if(exists $hash{$key}){;}                     检查哈希的某个键是否存在
scalar %hash;                                    查看哈希是否有元素
$last = pop(@IQ_list);                        把数组最后一个元素取出来并返回其值
$first = shift(@topguy);                      把数组第一个元素取出来并返回其值
push(@waiting, $name);                   在数组最后增加一个元素
unshift(@nowait, $name);                 在数组最前面增加一个元素
splice(@arr, 0, 2, $var);                     把数组从第0个元素起,共2个元素替换为$var,
scalar @arr;                                       得到数组有多少个元素
$lastindex = $#arr;                             得到数组的最后一个索引
                                                          
                                                           操作文件的函数
open(IN, “</path/file>”) || die “Cannot open file\n”;         打开文件作为输入内容
open(OUT, “>/path/file/”) || die “Cannot open file\n”;       打开文件作为输出内容
open(OUT, “>>$file”) || &myerr(“Couldn’t open $file”);    打开文件作为追加内容
close OUT;                关闭文件
chmod 0755, $file;    给文件设置权限
unlink $file;               删除文件
rename $file, $newname;            给文件重命名
link $existing_file, $link_name;    给文件做硬链接
symlink $existing_file, $link_name        给文件做软连接
mkdir $dirname, 0755;            创建目录
rmdir $dirname;                       删除目录
truncate $file, $size;                把$file的大小减小到$size
chown $uid, $gid                     修改文件的所属主以及所属组
$file = readlink, $linkfile           找到软链接文件的源文件
@stat = stat $file;                    获取文件的全部属性信息

                                                转换函数
chr $num;                数字变字符
ord($char);              字符变数字
hex(0x4f);                十六进制变浮点
oct(0700);                 八进制变幅点
localtime(time);         把time变成本地时间格式
gmtime(time);           把time变成格林威治格式
$string = pack(“C4”, split(/\./, $IP));
@arr = unpack(“C4”, $string);

