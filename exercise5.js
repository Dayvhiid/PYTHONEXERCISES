function translate(word){
    resultantWord = " "
    for (char in word){
        if(!char.includes("a","e","i","o","u")){
            resultantWord = resultantWord + "o" + char
        } else{
            resultantWord = resultantWord + char
        }
    }
    console.log(resultantWord)
}
translate("David is a fun guy")