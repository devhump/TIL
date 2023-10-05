let arr = ['가', '바', '나', '아', '다']


arr.sort(function(a,b){
  return a > b ? 1 : -1;
});

console.log(arr)


let arr2 = ['f', 'a', 'c', 'b', 'z']

arr2.sort();
console.log(arr2)