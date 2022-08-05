package com.bims.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

@Data
@AllArgsConstructor
@NoArgsConstructor
@TableName("bims_user")
public class User {
    @TableId(type = IdType.AUTO)
    private int userId;
    @TableField("user_name")
    private String userName;
    private String nickName;
    private String password;
    private String address;
    private String phone;
    private Date created;
    @TableField("createdBy")
    private int createdBy;
    private Date updated;
    @TableField("updatedBy")
    private int updatedBy;
    private String delFlag;
    private String status;
}
