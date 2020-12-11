# 业务订单状态
ORDER_DSC = 1
ORDER_SCZ = 2
ORDER_DFH = 3
ORDER_WC = 4
ORDER_STATUS = {
        (ORDER_DSC, '待生产'),
        (ORDER_SCZ, '生产中'),
        (ORDER_DFH, '待发货'),
        (ORDER_WC, '订单完成'),
}

# 用户的权限
POWER_YW = 1
POWER_SC = 2
POWER_SW = 3
POWER_JL = 4
POWER_STATUS = {
        (POWER_YW, '业务'),
        (POWER_SC, '生产'),
        (POWER_SW, '商务'),
        (POWER_JL, '经理'),
}
