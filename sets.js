let tags = new Set();
tags.add("JavaScript");
tags.add("ES6");
tags.add({version: "2015"});
tags.add("Web")

for(let tag of tags){
    console.log(tag)
    let [a, b, c, d] = tags;
    console.log(a, b, c, d)
    
}