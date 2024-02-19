vowels = ["a","e","i","o","u"]

function vowelCheck(character){
     if (vowels.includes(character)){
        console.log(true);
     } else {
        console.log(false);
     } 
}

vowelCheck("d")