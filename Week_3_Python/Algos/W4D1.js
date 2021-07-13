string_check = str.length

// check if the letter is the same as the previous if it is count++ if not push count then count = 0

 /* 
String Encode
You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
  var encoded = [];
  var count = 0;
  for(var i = 0; i <= str.length; i++){
    if(i == 0){
      encoded.push(str[i]);
      count++;
    }
    else if(str[i] == str[i-1]) {
      count++;
    }
    else{
      encoded.push(count);
      encoded.push(str[i]);
      count = 0;
      count++;
    }
  }
  //console.log(encoded.join(""));

  if(encoded.join("").length < str.length){
    return encoded.join("");
  }
  else{
    return str; 
  }
}

var newString1 = encodeStr(str1);
console.log(newString1)
var newString2 = encodeStr(str2);
console.log(newString2)
var newString3 = encodeStr(str3);
console.log(newString3)
var newString4 = encodeStr(str4);
console.log(newString4)


/* 
  String Decode  
*/


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