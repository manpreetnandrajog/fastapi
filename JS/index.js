// 1.Ways to print in JS
//alert("Yo");
//  document.write("this is document write") this command needs to be avoided and not used in everyday coding.

//2.Javascript console API
//console.log("Hello World", 6 + 9, " ANOTHER LOG ");
//console.warn("this is warning");
//console.error("This is an error");

// 3.JavaScript Variables- Containers to store data values.

// way to execute a multiline comment:
 /*
 multi
 line
 comment
 */

var number1 = 67;
var number2 = 78;
//console.log(number1+number2);

// 4. Data types in JavaScript
// Numbers
var num1 = 4756;
var num2 = 46.87;

//string
var str1= "This is a string";
var str2 = 'This is also a string ' ;

//objects
var marks = {
    ravi: 87 ,
    shubham: 76,
    derek: 12
}
//console.log(marks);

//boolean
var a = true;
var b = false;
//console.log(a);

//""undefined or null data type""
var und= undefined; //thing which is not defined
//console.log(und);
// if no values is assigned to the variable, the default value is displayed as "undefined"

var n = null;
//console.log(n);
//NOTE: undefined and null are two different things. 

/* At a very high level , there are two types of data types in javascript
1. Primitive data types:undefined, Null, Number,String, Boolean, Symbol - whenever symbol is used, it generates a unique value/key is generated.
2. reference data types: Arrays ,Object 
*/

//Array
var arr= [1,2,"string",4,5];
//can consists of strings as well.
//console.log(arr);

//Operators in javascrpit
//arithmetic operators
//var a=10;
//var b= 100;
//console.log("the value of a+b is", a+b);
//console.log("The value of a-b is", a-b);
//console.log("The value of a*b is", a*b);
//console.log("The value of a/b is", a/b);

//assignment Operator
//var c=b;
//c +=2;// c=c+2;
//c -=2;// c= c-2
//c *=2; // c=c*2
//c /=2;// c=c/2
//console.log(c);

//comparsion operator
//var x= 34;
//var y= 56;
//console.log(x==y);
//console.log(x>=y);
//console.log(x<=y);
//console.log(x>y);
//console.log(x<y);

//logical operator

//console.log(true && true)
//console.log(false&&false)
//console.log(false && true)
//console.log(true && false)

//OR operators
//console.log(true || true)
//console.log(false || false)
//console.log(false || true)
//console.log(true || false)

//logical not
//console.log(!true);
//console.log(!false);

//functions in javascript
 //if a answer is displayed in blue color, then it is a number ; if black in color ,then it is a string .
//function avg(a,b){
  //  return (a+b)/2;
//}
//DRY= Do Not repeat yourself
//c1= avg(4,6);
//c2= avg(14,98);
//console.log(c1,c2);

//CONDITIONALS IN JS
var age = 11;
//Single If Statement
//if (age >32){
  //  console.log("you are not a kid");
//}
//IF-ELSE STATEMENT
//if (age > 7){
  //  console.log("you are not a kid");
//}
//else {
  //console.log("you are a kid ");
//}

//IF-ELSE LADDER
/*
var age=20;
if(age > 32){
  console.log("You are not a kid");
}
else if (age > 26) {
  console.log("bacche nahi rahe");
}
else if (age > 22) {
  console.log("yes bacche nahi rahe");
}
else if (age > 18) {
  console.log("18 bacche nahi rahe");
}
else  {
  console.log(" bacche ");
}
console.log("End of ladder");
*/

//LOOP IN JS
//FOR-LOOP
var arr = [1,2,3,4,5,6,7];
console.log(arr); 
for(var i=0; i< arr.length; i++){
  console.log(arr[i])
}