package tests

import (
	"encoding/json"
	"github.com/go-playground/validator/v10"
	"log"
	"net/url"
	"os"
)

func url_validator1(url_string string) bool {
	u, err := url.ParseRequestURI(url_string)
	if u != nil && err == nil {
		return true
	}
	return false
}

func url_validator2(url_string string) bool {
	u, err := url.Parse(url_string)
	if u != nil && err == nil {
		return true
	}
	return false
}

func url_validator3(url_string string) bool {
	validate := validator.New(validator.WithRequiredStructEnabled())
	err := validate.Var(url_string, "url")
	return err == nil
}

func Url_Validation() {
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
	count_full := 0
	count_true1 := 0
	count_true2 := 0
	count_true3 := 0
	for i := 0; i < len(arr_url); i++ {
		url_string := arr_url[i][0].(string)
		//part_url := arr_url[i][1].(map[string]interface{})
		count_full++
		if url_validator1(url_string) {
			count_true1++
		}
		if url_validator2(url_string) {
			count_true2++
		}
		if url_validator3(url_string) {
			count_true3++
		}
	}
	res := make(map[string]float32)
	res["net/url(ParseRequestURI)"] = float32(count_true1) / float32(count_full) * 100
	res["net/url(Parse)"] = float32(count_true2) / float32(count_full) * 100
	res["validator/v10"] = float32(count_true3) / float32(count_full) * 100
	log.Println(res)
}
