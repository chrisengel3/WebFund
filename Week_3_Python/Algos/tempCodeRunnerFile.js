

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";


function decodeStr(str) {

  var tempLetter = []
  for(var i = 0; i <= str.length; i++){
    if (i % 2 == 0 || i == 0){
      console.log(str[i+1])
      tempLetter.push(str[i].repeat(parseInt(str[i+1])))
      console.log(tempLetter[0])
      tempLetter.join("")
      
    } 
    

  } 
  return tempLetter 
}


console.log(decodeStr(str1))