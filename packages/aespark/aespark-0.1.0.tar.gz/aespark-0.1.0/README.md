2023.08.08

增加诸多功能，完善诸多细节，极大简化了代码名称

1. 增加了ipv6的解析查询；
2. 优化了Palette函数，现在可以传入列表参数，一次性记录多条信息了；
3. 简化了函数名称；

2023.08.07

1. 新增银行卡归属行查询功能，与IP查询类似，需要先实例化，具体查看说明；

2023.08.04

1. 新增交易金额清洗：DataClean_amontCleaning；
2. doc模块新增插入图片函数，支持图片缩放；
3. 优化了快速资金透视表功能，加入了事前清洗，降低了调用该函数的参数要求；
4. 其他细节优化；

2023.08.02

1. 新增快速计算资金透视表功能；
2. 多sheet合并新增参数save，用于设置是否保存合并文件，默认保存；
3. 单sheet合并提取合并文件名称改进，现在能够产出语序正确的文件名称了；
4. doc模块的插表函数，现在表格能够自动调整到合适的宽度了；