import isUrl from 'is-url';
import isUrlHttp from 'is-url-http';
import fs from 'fs';

function isValidUrl1(url) {
    try {
        new URL(url);
        return true;
    } catch (err) {
        return false;
    }
}

function isValidUrl2(url) {
    return isUrl(url);
}

function isValidUrl3(url) {
    return isUrlHttp(url);
}

function isValidUrl4(str) {
    const pattern = new RegExp(
        '^([a-zA-Z]+:\\/\\/)?' + // protocol
        '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
        '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR IP (v4) address
        '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
        '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
        '(\\#[-a-z\\d_]*)?$', // fragment locator
        'i'
    );
    return pattern.test(str);
}

export function runValidationTest() {
    fs.readFile('../fuzz/fuzz.json', (err, data) => {
        if (err) {
            console.log("Error reading file from disk: ${err}");
        } else {
            let countFull = 0;
            let countTrue1 = 0;
            let countTrue2 = 0;
            let countTrue3 = 0;
            let countTrue4 = 0;
            const listUrl = JSON.parse(data)
            listUrl.forEach(tUrl => {
                let url = tUrl[0];
                countFull++;
                if (isValidUrl1(url)) {
                    countTrue1++;
                }
                if (isValidUrl2(url)) {
                    countTrue2++;
                }
                if (isValidUrl3(url)) {
                    countTrue3++;
                }
                if (isValidUrl4(url)) {
                    countTrue4++;
                }
            })
            console.log("Url Constructor", ((countTrue1 / countFull) * 100) + "%");
            console.log("is-url", ((countTrue2 / countFull) * 100) + "%");
            console.log("is-url-http", ((countTrue3 / countFull) * 100) + "%");
            console.log("Regex", ((countTrue4 / countFull) * 100) + "%");
        }
    })
}