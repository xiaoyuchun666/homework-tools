#!/usr/bin/env bash  

# 定义要运行的命令  
command="./test.sh"  # 将此替换为实际命令  
output_file="output.log"     # 输出文件名  
count=0                       # 计数器  

# 清空输出文件  
> "$output_file"  

# 循环运行命令直到出错  
while true; do  
    # 运行命令并将输出和错误记录到文件  
    $command >> "$output_file" 2>&1  
    # 检查命令的退出状态  
    if [[ $? -ne 0 ]]; then  
        break  # 如果命令出错，退出循环  
    fi  
    count=$((count + 1))  # 增加计数  
done  

# 输出所有内容  
cat "$output_file"  

# 报告运行次数  
echo "脚本在失败前共运行了 $count 次。"
