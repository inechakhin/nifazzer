package ru.inechakhin.tests;

import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;

import org.apache.commons.validator.routines.UrlValidator;

import com.github.cliftonlabs.json_simple.*;

public class ValidationFuzzUrl {

    public boolean isValidURL1(String url) throws MalformedURLException, URISyntaxException {
        try {
            new URL(url).toURI();
            return true;
        } catch (MalformedURLException e) {
            return false;
        } catch (URISyntaxException e) {
            return false;
        }
    }

    public boolean isValidURL2(String url) throws MalformedURLException {
        UrlValidator validator = new UrlValidator();
        return validator.isValid(url);
    }

    public boolean isValidURL3(String url) {
        String regex = "^(https?|ftp|file)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]";
        Pattern p = Pattern.compile(regex);
        if (url == null) {
            return false;
        }
        Matcher m = p.matcher(url);
        return m.matches();
    }

    public Map<String, String> run() throws IOException, JsonException, URISyntaxException {
        Reader reader = Files.newBufferedReader(Paths.get("test/fuzz/fuzz.json"));
        JsonArray urlArray = (JsonArray) Jsoner.deserialize(reader);
        float countFull = 0;
        float countTrue1 = 0;
        float countTrue2 = 0;
        float countTrue3 = 0;
        for (Object arUrl : urlArray) {
            JsonArray urlJsonArray = (JsonArray) arUrl;
            String url = urlJsonArray.getString(0);
            countFull++;
            if (isValidURL1((String) url)) {
                countTrue1++;
            }
            if (isValidURL2((String) url)) {
                countTrue2++;
            }
            if (isValidURL3((String) url)) {
                countTrue3++;
            }
        }
        Map<String, String> map = new HashMap<String, String>();
        map.put("Using JDK", String.valueOf((countTrue1 / countFull) * 100) + "%");
        map.put("Url Validator (Apache Commons)", String.valueOf((countTrue2 / countFull) * 100) + "%");
        map.put("Regex", String.valueOf((countTrue3 / countFull) * 100) + "%");
        return map;
    }
}
