/* 
	Acronyms
	Create a function that, given a string, returns the string’s acronym 
	(first letter of each word capitalized). 
	Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

function acronymize(str) {
	var wordArr = str
	var outputStr = ""
    console.log(wordArr)
	for (var i = 0; i < wordArr.length; i++){
		if (wordArr[i] != ''){
			outputStr += wordArr[i][0+1]
		}
        else outputStr += wordArr[i][0]
	}
	return outputStr.toUpperCase()
}


console.log(acronymize(str1))
console.log(acronymize(str2))