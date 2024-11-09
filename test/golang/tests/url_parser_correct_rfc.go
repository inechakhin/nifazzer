package tests

import (
	"encoding/json"
	"fmt"
	"log"
	"net"
	"net/url"
	"os"
)

func net_url_Parse(url_string string, part_url map[string]interface{}) bool {
	u, err := url.Parse(url_string)
	if err != nil {
		return false
	}
	if (u.Scheme == "" && part_url["scheme"] != "") || (u.Scheme != "" && u.Scheme != part_url["scheme"]) {
		fmt.Println("Problem in scheme:\n", url_string, "\n", part_url["scheme"], "\n", u.Scheme)
	}
	if (u.User == nil && part_url["userinfo"] != "") || (u.User != nil && u.User.String() != part_url["userinfo"]) {
		fmt.Println("Problem in userinfo:\n", url_string, "\n", part_url["userinfo"], "\n", u.User)
	}
	host, port, _ := net.SplitHostPort(u.Host)
	if port == "" {
		if (u.Host == "" && part_url["host"] != "") || (u.Host != "" && u.Host != part_url["host"]) {
			fmt.Println("Problem in host:\n", url_string, "\n", part_url["host"], "\n", u.Host)
		}
	} else {
		if (host == "" && part_url["host"] != "") || (host != "" && host != part_url["host"]) {
			fmt.Println("Problem in host:\n", url_string, "\n", part_url["host"], "\n", host)
		}
		if (port == "" && part_url["port"] != "") || (port != "" && port != part_url["port"]) {
			fmt.Println("Problem in port:\n", url_string, "\n", part_url["port"], "\n", port)
		}
	}
	if (u.Path == "" && part_url["path-abempty"] != "") || (u.Path != "" && u.Path != part_url["path-abempty"]) {
		fmt.Println("Problem in path-abempty:\n", url_string, "\n", part_url["path-abempty"], "\n", u.Path)
	}
	if (u.RawQuery == "" && part_url["query"] != "") || (u.RawQuery != "" && u.RawQuery != part_url["query"]) {
		fmt.Println("Problem in query:\n", url_string, "\n", part_url["query"], "\n", u.RawQuery)
	}
	if (u.Fragment == "" && part_url["fragment"] != "") || (u.Fragment != "" && u.Fragment != part_url["fragment"]) {
		fmt.Println("Problem in fragment:\n", url_string, "\n", part_url["fragment"], "\n", u.Fragment)
	}
	return true
}

func Url_Parser_Correct_RFC() {
	// Read Json
	data, err := os.ReadFile("../fuzz/fuzz.json")
	if err != nil {
		log.Fatal("Error when opening file: ", err)
	}
	// Parse Json
	var arr_url [][]any
	err = json.Unmarshal(data, &arr_url)
	if err != nil {
		log.Fatal("Error during Unmarshal(): ", err)
	}
	// Test
	for i := 0; i < len(arr_url); i++ {
		url_string := arr_url[i][0].(string)
		part_url := arr_url[i][1].(map[string]interface{})
		net_url_Parse(url_string, part_url)
	}
}
