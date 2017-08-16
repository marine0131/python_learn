import net/http
import io/ioutil
import regexp
import strings
import os
import strconv
import fmt


func Check(err error) {
    defer func() { err = nil }()
    if err != nil {
        println("****ERROR****")
        panic(err)
    }
}

// »ñÈ¡ÍøÒ³
func GetHTML(url string) (body string) {
    res, err := http.Get(url)
    Check(err)
    defer res.Body.Close()
    // ÍøÒ³žñÊœ»¯
    data, err := ioutil.ReadAll(res.Body)
    Check(err)
    body = string(data)
    return
}

// »ñÈ¡ÏÂÔØÎÄŒþ
func downloadfile(url string) (file []byte) {
    res, err := http.Get(url)
    Check(err)
    defer res.Body.Close()
    // žñÊœ»¯
    file, err = ioutil.ReadAll(res.Body)
    Check(err)
    return
}

func main() {
    println("======================================================\n")
    println("\tÐ¡ÍŒÆ¬ÅÀÈ¡³ÌÐò\n")

    // ÅÀÈ¡Ò³Âë
    //pages := []string{"2", "3", "4", "5", "6", "7", "8", "9", "10"}
    pages := []string{"2"}
    for _, index := range pages {
        GetImages("http://boards.4chan.org/s/" + index + "/")
    }
}

// ÍŒÆ¬Æ¥ÅäÕýÔò
var imageItemExp = regexp.MustCompile(`"//i\.4cdn\.org/s/[0123456789]+s\.jpg"`)

// ÏÂÔØÍŒÆ¬·œ·š
func GetImages(url string) {

    // ÌáÈ¡ÍŒÆ¬ÁŽœÓ
    body := GetHTML(url)
    imgs := imageItemExp.FindAllStringSubmatch(body, 10000)
    // ÁŽœÓžñÊœ»¯(È¥µôÒýºÅ)
    imgUrl := make([]string, 0)
    for _, v := range imgs {
        u := strings.Replace(v[0], "\"", "", -1)
        url := u[0:28]
        imgUrl = append(imgUrl, url)
    }

    // ŽŽœšÄ¿ÂŒ
    dirName := "ÍŒÆ¬Žæ·ÅÄ¿ÂŒ"
    os.MkdirAll(dirName, 0777)
    // ÏÂÔØÍŒÆ¬
    for i, v := range imgUrl {
        fileName := "./" + dirName + "/img-" + strconv.Itoa(i) + ".jpg"

        data := downloadfile("http:" + v + ".jpg")

        // ±£ŽæÎÄŒþ
        if err := ioutil.WriteFile(fileName, data, 0666); err != nil {
            println("****ÏÂÔØŽíÎó****")
            panic(err)
        } else {
            fmt.Println("ÏÂÔØÍŒÆ¬:", fileName)
        }
    }
}
