package com.example.angularspring;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.util.Locale;
import java.util.stream.Stream;

@SpringBootApplication
public class AngularSpringApplication {

	public static void main(String[] args) {
		SpringApplication.run(AngularSpringApplication.class, args);
	}

	@Bean
	CommandLineRunner init(UserRepository userRepository) {
		return args -> {
			Stream.of("Afi","Jane","Ransford","Grace","NK").forEach(name -> {
				User user = new User(name,name.toLowerCase() + "@domain.com");
				userRepository.save(user);
			});
			userRepository.findAll().forEach(System.out::println);
		};
	}
}
