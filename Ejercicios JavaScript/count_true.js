

const countTrue = (array)=>{
	let count = 0;
	for(i of array){
		if(typeof(i)!='boolean'){
			console.log("The array must be only boolean values.");
			return count=0;
		}else{
			if(i == true){
				count++;
			}
		}
	}
	return count;
}

alert(countTrue([false, false, false]));