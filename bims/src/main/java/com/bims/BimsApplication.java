package com.bims;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.bims.mapper")
public class BimsApplication {

    public static void main(String[] args) {
        SpringApplication.run(BimsApplication.class, args);
    }

}
