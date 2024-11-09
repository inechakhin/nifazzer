package ru.inechakhin.tests;

import java.io.*;
import java.net.*;
import java.nio.file.*;

import com.github.cliftonlabs.json_simple.*;

public class UrlParserCorrectRFC {

    public void testNetURL(String url, JsonObject partUrl) throws MalformedURLException {
        URL parsingUrl = new URL(url);
        if ((parsingUrl.getProtocol() == null && partUrl.get("scheme") != null) || (parsingUrl.getProtocol() != null && partUrl.get("scheme") != null && !partUrl.get("scheme").equals(parsingUrl.getProtocol()))) {
            System.out.println("Problem in scheme:\n" + url + "\n" + partUrl.get("scheme") + "\n" + parsingUrl.getProtocol());
        }
        if ((parsingUrl.getUserInfo() == null && partUrl.get("userinfo") != null) || (parsingUrl.getUserInfo() != null && partUrl.get("userinfo") != null && !partUrl.get("userinfo").equals(parsingUrl.getUserInfo()))) {
            System.out.println("Problem in userinfo:\n" + url + "\n" + partUrl.get("userinfo") + "\n" + parsingUrl.getUserInfo());
        }
        if ((parsingUrl.getHost() == null && partUrl.get("host") != null) || (parsingUrl.getHost() != null && partUrl.get("host") != null && !partUrl.get("host").equals(parsingUrl.getHost()))) {
            System.out.println("Problem in host:\n" + url + "\n" + partUrl.get("host") + "\n" + parsingUrl.getHost());
        }
        if ((parsingUrl.getPort() != -1 && partUrl.get("port") != null && Integer.parseInt((String)partUrl.get("port")) != parsingUrl.getPort())) {
            System.out.println("Problem in port:\n" + url + "\n" + partUrl.get("port") + "\n" + parsingUrl.getPort());
        }
        if ((parsingUrl.getPath() == null && partUrl.get("path-abempty") != null) || (parsingUrl.getPath() != null && partUrl.get("path-abempty") != null && !partUrl.get("path-abempty").equals(parsingUrl.getPath()))) {
            System.out.println("Problem in path:\n" + url + "\n" + partUrl.get("path-abempty") + "\n" + parsingUrl.getPath());
        }
        if ((parsingUrl.getQuery() == null && partUrl.get("query") != null) || (parsingUrl.getQuery() != null && partUrl.get("query") != null && !partUrl.get("query").equals(parsingUrl.getQuery()))) {
            System.out.println("Problem in query:\n" + url + "\n" + partUrl.get("query") + "\n" + parsingUrl.getQuery());
        }
        if ((parsingUrl.getRef() == null && partUrl.get("fragment") != null) || (parsingUrl.getRef() != null && partUrl.get("fragment") != null && !partUrl.get("fragment").equals(parsingUrl.getRef()))) {
            System.out.println("Problem in fragment:\n" + url + "\n" + partUrl.get("fragment") + "\n" + parsingUrl.getRef());
        }
    }

    public void run() throws IOException, JsonException, URISyntaxException {
        Reader reader = Files.newBufferedReader(Paths.get("test/fuzz/fuzz.json"));
        JsonArray urlArray = (JsonArray) Jsoner.deserialize(reader);
        for (Object arUrl : urlArray) {
            try {
                JsonArray urlJsonArray = (JsonArray) arUrl;
                String url = urlJsonArray.getString(0);
                JsonObject partUrl = (JsonObject) urlJsonArray.get(1);
                testNetURL(url, partUrl);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }

    }
}
