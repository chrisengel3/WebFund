// var start = 0;
// var end = 12;
    
// while(start < end) {
//     console.log("start: " + start + ", end: " + end);
//     start += 2;
//     end -= 2;
// }



// for loops are for when you know exactly how many iterations you want.
// 



var start = 0;
var end = 12;
    
while(start < end) {
    console.log("start: " + start + ", end: " + end);
    start += 2;
    end -= 2;
}

var array = ["a", "b", "c", "d", "e"];
array.reverse();
console.log(array)





function reverse(arr) {
    for(var left=0; left<arr.length/2; left++) {
        var right = arr.length-1-left;
        if(arr[left] != arr[right]) {
        }
    }
}
    
var result1 = reverse( ["a", "b", "c", "d", "e"] );
console.log(result1);


var arrayorigin = ["a", "b", "c", "d", "e"];

function reverse(arr){
    var arr1 = arrayorigin[0]
    var arr4 = arrayorigin[4]
    var x = arr1


}




["a", "b", "c", "d", "e"]


function isPal(arr) {
    for(var left=0; left<3; left++) {
        var right = arr.length-1-left;
        if(arr[left] != arr[right])

    }

}
    
var result1 = isPal( [1, 1, 2, 2, 1] );
console.log(result1);
    
// var result2 = isPal( [3, 2, 1, 1, 2, 3] );
// console.log(result2);



var array = ["a", "b", "c", "d", "e"];
array.reverse();
console.log(array)

var array = ["a", "b", "c", "d", "e"];

function ReversePro(array){
    var temp;
    var last = array.length - 1;
    for(var i = 0; i<array.length/2; i++){
        temp = array[i];
        array[i] = array[last];
        array[last] = temp;
        --last;
    }
    return array;
}

console.log(array)