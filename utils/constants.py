# 业务订单状态
ORDER_BLZ = 1
ORDER_DSC = 2
ORDER_SCZ = 3
ORDER_DFH = 4
ORDER_WC = 5
ORDER_STATUS = {
        (ORDER_BLZ, '备料中'),
        (ORDER_DSC, '待生产'),
        (ORDER_SCZ, '生产中'),
        (ORDER_DFH, '待发货'),
        (ORDER_WC, '订单完成'),
}


# 生产订单状态
PROD_BL = 1
PROD_SC = 2
PROD_DFH = 3
PROD_WC = 4
PROD_STATUS = {
        (PROD_BL, '备料中'),
        (PROD_SC, '生产中'),
        (PROD_DFH, '待发货'),
        (PROD_WC, '订单完成'),
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
