package com.example.batchprocessing;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.batch.item.ItemProcessor;

public class PersonItemProcessor implements ItemProcessor<Personc, Personc> {

    private static final Logger log = LoggerFactory.getLogger(PersonItemProcessor.class);

    @Override
    public Personc process(final Personc personc) throws Exception {
        final String firstName = personc.getFirstName().toUpperCase();
        final String lastName = personc.getLastName().toUpperCase();

        final Personc transformedPerson = new Personc(firstName, lastName);

        log.info("Converting (" + personc + ") into (" + transformedPerson + ")");

        return transformedPerson;
    }

}
}
