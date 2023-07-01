!#/usr/bin/node

const lengthOfArgs = progress.argv.length;

if (lengthOfArgs === 2){
	console.log('No argument');
}else if(lengthOfArgs === 3){
	console.log('Argument found');
}else{
	console.log('Arguments found');
}
