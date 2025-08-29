// const fs = require("fs");
//
// fs.readFile("input.txt", "utf8", (err, data) => {
// 	if (err) {
// 		console.error("Error reading file:", err);
// 		return;
// 	}
//
// 	let lines = data.split("\n").slice(0, data.split("\n").length - 1);
//
// 	let firstArray = [];
// 	let secondArray = [];
//
// 	for (let i = 0; i < lines.length; i++) {
// 		let [first, second] = lines[i].split("   ");
//
// 		firstArray.push(parseInt(first));
// 		secondArray.push(parseInt(second));
// 		
// 	}
//
// 	// console.table({firstArray, secondArray})
//
// 	firstArray.sort();
// 	secondArray.sort();
//
// 	// console.table({firstArray, secondArray})
//
// 	let distance = 0;
// 	for (let i = 0; i < firstArray.length; i++) {
// 		distance += Math.abs(firstArray[i] - secondArray[i]);
// 	}
//
// 	console.log(distance);
//
// });


const fs = require("fs");

fs.readFile("input.txt", "utf-8", (err, data) => {
	if (err) {
		console.error("Error: reading file: ", err);
		return;
	}


	let lines = data.split("\n").slice(0, data.split("\n").length - 1);

	let firstArray = [];
	let secondArray = [];

	for (let i = 0; i < lines.length; i++) {
		let [first, second] = lines[i].split("   ");

		firstArray.push(parseInt(first));
		secondArray.push(parseInt(second));


		// firstArray.sort();
		// secondArray.sort();

	}

	// console.table({
	// 	firstArray,
	// 	secondArray
	// })

	let j = 0;
	let sum = 0;

	for (let i = 0; i < firstArray.length; i++) {
		let multi = 0;
		j = 0;

		while (j < firstArray.length) {
			if (firstArray[i] === secondArray[j]) {
				multi++;
			}
			j++;
		}

		sum += firstArray[i] * multi;
		// console.log(multi)
	}

	console.log(sum);


})

