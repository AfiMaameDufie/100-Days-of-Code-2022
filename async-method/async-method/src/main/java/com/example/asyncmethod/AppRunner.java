package com.example.asyncmethod;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.concurrent.CompletableFuture;

@Component
public class AppRunner implements CommandLineRunner {
    private static final Logger logger = LoggerFactory.getLogger(AppRunner.class);

    private static GithubLookupService githubLookupService;

    public AppRunner(GithubLookupService githubLookupService) {
        this.githubLookupService = githubLookupService;
    }

    @Override
    public void run(String... args) throws Exception {
        //Starting the clock
        long Start = System.currentTimeMillis();

        //Start the async lookups
        CompletableFuture<User> page1 = githubLookupService.findUser("PivotalSoftware");
        CompletableFuture<User> page2 = githubLookupService.findUser("CloudFoundry");
        CompletableFuture<User> page3 = githubLookupService.findUser("Spring-Projects");

        //wait till the lookups are done
        CompletableFuture.allOf(page1,page2,page3).join();

        //Display results
        logger.info("Time used: " + (System.currentTimeMillis() - start));
        logger.info("----" + page1.get());
        logger.info("----" + page2.get());
        logger.info("----" + page3.get());

    }
}
