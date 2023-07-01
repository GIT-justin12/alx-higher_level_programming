!#/usr/bin/node

const lengthOfArgs = process.argv.length;

if (lengthOfArgs === 2){
	console.log('No argument');
}else if(lengthOfArgs === 3){
	console.log('Argument found');
}else{
	console.log('Arguments found');
}
