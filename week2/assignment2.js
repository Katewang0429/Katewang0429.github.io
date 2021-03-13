<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>

<body>
<script>

function calculate(min, max){
    let n = 1;
    let result = min;
    while (n < (max - min + 1)){
      result = result + (min + n);
      n++;
    }
  console.log(result);
}
calculate(1, 3); 
calculate(4, 8); 

function avg(data){
  employees = data.count;
  var salary = 0;
  for (i = 0; i <= employees - 1; i++) {
    money = data.employees[i].salary;
    salary += money;
  
  }
  console.log(salary / employees);
}
avg({
		"count":3,
		"employees":[
		{
			"name":"John",
			"salary":30000
		},
		{
			"name":"Bob",
			"salary":60000
		},	
		{
			"name":"Jenny",
			"salary":50000
		}
		]
	}); 

function maxProduct(nums){
	var product = []
	for (var i = 0; i < nums.length; i++) {
		for (var j = i+1; j < nums.length; j++) {
			product.push(nums[i]*nums[j]);
		}
	}
	console.log(Math.max.apply(null, product));

}
maxProduct([5, 20, 2, 6]); 
maxProduct([10, -20, 0, 3]); 

function twoSum(nums, target){
	for (var i = 0; i < nums.length; i++) {
    	for (var j = i+1; j < nums.length; j++) {
        	if (nums[i] + nums[j] == target) {
                    return ('[' + i + ',' + j + ']')
                    };
                };
            };
        }
result=twoSum([2, 11, 7, 15], 9)
console.log(result) 

</script>
	
</body>
</html>
