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