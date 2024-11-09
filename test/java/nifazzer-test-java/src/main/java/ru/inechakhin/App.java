package ru.inechakhin;

import java.util.Map;

import ru.inechakhin.tests.*;

public class App {

    public static void main(String[] args) {
        try {
            ValidationFuzzUrl valFuzzUrl = new ValidationFuzzUrl();
            Map<String, String> map = valFuzzUrl.run();
            System.out.println(map);
            UrlParserCorrectRFC parsingFuzzUrl = new UrlParserCorrectRFC();
            parsingFuzzUrl.run();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
