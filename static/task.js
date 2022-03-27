function cook(){
	let form = document.getElementsByTagName('form')[0];
	let input1 = document.getElementsByTagName('input')[0].value;
	let input2 = document.getElementsByTagName('input')[1].value;

	if ((input1=='')&&(input2=='')) {
		alert('Wow, such empty');
		return;
	};


	let xhr = new XMLHttpRequest();
	xhr.open("POST", 'localhost:5000');

	let formData = new FormData(form);
	xhr.send(formData);
}