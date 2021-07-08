const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

function parensValid(str1) {
    testArray = []
    for(i = 0; i < str.length-1; i++){   
        if (str[i]=="(" || str[i]=="{" || str[i]=="["){;
          testArray.push(str[i]);
        } 
        else if(str[i]==")"){
          if(testArray.length==0)return false;
          else if(testArray[testArray.length-2]=="("){
            testArray.pop();
          }
        }
        else if(str[i]=="}"){
          if(testArray.length==0)return false;
          else if(testArray[testArray.length-2]=="{"){
            testArray.pop();
          }
        }        
        else if(str[i]=="]"){
          if(testArray.length==0)return false;
          else if(testArray[testArray.length-2]=="["){
            testArray.pop();
          }
        }
    }
    if(testArray.length==0){
       return true;
    }
    else return false;
  }
  
