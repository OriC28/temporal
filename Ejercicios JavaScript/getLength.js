
const getLength = (array)=>{
	return array.flat(Infinity).length;
}
alert(getLength([1,2,3,4,[5,6,[7,[8]]]]));




