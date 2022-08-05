drop table if exists `bims_user`;
create table `bims_user`
(
	`user_id` int primary key auto_increment comment '用户id',
	`user_name` varchar(64) not null unique comment '用户名',
	`nick_name` varchar(64) null comment '昵称',
	`password` varchar(64) not null comment '密码',
	`address` varchar(64) null comment '地址',
	`phone` varchar(64) null comment '电话',
	`created` datetime not null default current_timestamp comment '创建时间',
	`createdBy` int null comment '创建用户',
	`updated` datetime not null default current_timestamp on update current_timestamp comment '更新时间',
	`updatedBy` int null comment '更新用户',
	`del_flag` char default '0' comment '删除标志(0:未删除, 1:已删除)',
	`status` char default '0' comment '状态(0:正常, 1:停用)'
)comment='用户表';