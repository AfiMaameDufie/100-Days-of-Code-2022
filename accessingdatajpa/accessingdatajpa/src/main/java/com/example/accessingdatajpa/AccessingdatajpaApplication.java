package com.example.accessingdatajpa;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class AccessingdatajpaApplication {

	private static final Logger log = LoggerFactory.getLogger(AccessingdatajpaApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(AccessingdatajpaApplication.class, args);
	}

	@Bean
	public CommandLineRunner cmdLine(CustomerRepository repository) {
		return (args) -> {
			//to save a few customers
			repository.save(new Customer("Afi", "Maame"));
			repository.save(new Customer("Ransford", "Gbadago"));
			repository.save(new Customer("Jane", "Obeng"));
			repository.save(new Customer("Grace", "Nyamekye"));
			repository.save(new Customer("Johnson", "Gbadago"));


			//perform a fetch on Customers
			log.info("Customers found with findAll() method:");
			log.info("--------------------------------------");
			for(Customer customer: repository.findAll()) {
				log.info(customer.toString());
			}
			log.info("");

			//fetch a customer by a particular ID
			Customer customer = repository.findById(1L);
			log.info("Customers found with the ID(1L):");
			log.info("--------------------------------------");
			log.info("");

			//fetch Customers by their last name
			log.info("Customer found with findByLastName('Gbadago'):");
			log.info("----------------------------------------------");
			repository.findByLastName("Gbadago").forEach(gbadago -> {
						log.info(gbadago.toString());
			});
			log.info("");
		};
	}
}
