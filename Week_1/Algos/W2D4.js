var arr2d = [   [2, 5, 8],
                [3, 6, 1],
                [5, 7, 7]];
    
// console.log(arr2d[0] + "," + arr2d[1] + "," + arr2d[2]);


var flatten = [];

// for (i = 0; i<arr2d[0].length; i++) {
//         flatten.push(arr2d[0][i])
// }
// for (i = 0; i<arr2d[1].length; i++) {
//         flatten.push(arr2d[1][i])
// }
// for (i = 0; i<arr2d[2].length; i++) {
//         flatten.push(arr2d[2][i])
// }

// console.log(flatten)



for(x=0; x<arr2d.length; x++){
    for(i=0; i<arr2d[x].length; i++){
        flatten.push(arr2d[x][i]);
    }
    
} 
console.log(flatten);