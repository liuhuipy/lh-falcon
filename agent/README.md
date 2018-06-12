# lh-falcon-agent

## 主要采集系统常见指标：
* cpu相关采集项
    ```
    ## 通过读取/proc/stat来获取cpu信息
    cpu.user            # 从系统启动开始累计到当前时刻，用户态的cpu时间，不包含nice值为负的进程
    cpu.nice            # 从系统启动开始累计到当前时刻
    cpu.system          # 从系统启动开始累计到当前时刻，nice值为负的进程所占用的CPU时间
    cpu.idle            # 从系统启动开始累计到当前时刻，除硬盘IO等待时间以外其它等待时间
    cpu.iowait          # 从系统启动开始累计到当前时刻，硬盘IO等待时间
    cpu.irq             # 从系统启动开始累计到当前时刻，硬中断时间
    cpu.softirq         # 从系统启动开始累计到当前时刻，软中断时间
    cpu.steal           #
    cpu.guest           #
    cpu.switches        #
    ```
* 磁盘相关采集项
    ```
    ## 通过获取df命令结果来采集每个挂载点的blocks和inode的使用情况
    df.sizes.free                # 磁盘可用量
    df.sizes.free.percent        # 磁盘可用量占总量的百分比
    df.sizes.total               # 磁盘总大小
    df.sizes.used                # 磁盘已用大小
    df.sizes.used.percent        # 磁盘已用大小占总量的百分比
    df.inodes.total             # inode总数
    df.inodes.free              # 可用inode数目
    df.inodes.free.percent      # 可用inode占比
    df.inodes.used              # 已用的inode数据
    df.inodes.used.percent      # 已用inode占比
    ```
* 内存相关采集项
    ```
    通过读取/proc/meminfo中内容获取mem信息，其中mem.memfree=free+buffers+cached，mem.memused=mem.memtotal-
    mem.memfree。
    mem.memtotal                # 内存总大小
    mem.memused                 # 使用了多少内存
    mem.memused.percent         # 使用的内存占比
    mem.memfree                 # 空闲内存大小
    mem.memfree.percent         # 空闲内存占比
    mem.swaptotal               # swap总大小
    mem.swapused                # 使用了多少swap
    mem.swapused.percent        # 使用的swap的占比
    mem.swapfree                # 空闲swap大小
    mem.swapfree.percent        # 空闲swap占比
    ```
* IO相关采集项
    ```
    ## 通过读取/proc/diskstats来获取io信息
    disk.io.ios_in_progresss
    disk.io.msec_read
    disk.io.msec_total
    disk.io.msec_weighted_total
    disk.io.msec_write
    disk.io.read_merged
    disk.io.read_requests
    disk.io.read_sectors
    disk.io.write_merged
    disk.io.write_requests
    disk.io.write_sectors
    disk.io.read_bytes
    disk.io.write_bytes
    ```
* 机器负载
    ```
    ## 通过读取/proc/loadavg
    load.1min
    load.5min
    load.15min
    ```
* 端口采集项
    ```
    ## 通过ss -ln，来判断指定的端口是否处于listen状态
    net.port.listen/port={22}
    ```
* 网络采集项
    ```
    ## 通过读取/proc/net/dev获取net信息
    net.if.in.sizes
    net.if.in.compressed
    net.if.in.dropped
    net.if.in.errors
    net.if.in.fifo.errs
    net.if.in.frame.errs
    net.if.in.multicast
    net.if.in.packets
    net.if.out.sizes
    net.if.out.carrier.errs
    net.if.out.collisions
    net.if.out.compressed
    net.if.out.dropped
    net.if.out.errors
    net.if.out.fifo.errs
    net.if.out.packets
    net.if.total.sizes
    net.if.total.dropped
    net.if.total.errors
    net.if.total.packets
    ```
* 进程资源采集项


