
const count = (word)=>{
	let c = 0;
	for(i of word){
		if(i == " "){
			c++;
		}
	}
	return c;
}

const determine = (word)=>{
	const letters = "abcdefghijklmnopqrstuvwxyz";
	let rest_letters = 0;
	word = word.trim().toLowerCase();
	let spaces = count(word)*2;
	
	let first_last_letters = parseInt((letters.indexOf(word[0]) - letters.indexOf(word.slice(-1))));
	for (i of word){
		if(!letters.includes(i) && i!=" "){
			return 0;
		}
	}
	for (i of word.substring(1,word.length-1)){
		if(i!=" "){
			rest_letters+=parseInt(letters.indexOf(i));
		}
	}
	let result = (spaces>=1) ? (first_last_letters + rest_letters)*spaces : first_last_letters + rest_letters;
	return result;
}

alert(determine("hola que tal"));
