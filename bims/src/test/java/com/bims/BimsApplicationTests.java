package com.bims;

import com.bims.entity.User;
import com.bims.mapper.UserMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class BimsApplicationTests {

    @Test
    void contextLoads() {
    }
    @Autowired
    private UserMapper userMapper;

    @Test
    public void testUserMapper(){
        User user = new User();
        user.setUserName("admin");
        user.setPassword("123456");
        userMapper.insert(user);
    }

}
