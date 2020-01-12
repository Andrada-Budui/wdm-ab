var sir = [];

function add() {
	var name = prompt('Ce nume doriti sa adaugati?');
	sir.push(name);
}

function remove() {
	var newName = prompt('Ce nume doriti sa stergeti?');
	poz = sir.indexOf(newName);
	if (poz >= 0) {
		sir.splice(poz,1);
	}
}

function display() {
	for(elem of sir) {
		console.log(elem);
	}
}

var start = prompt('Doriti sa deschidem aplicatia? (da/nu)');
var comanda = '';
if(start === 'da') {
	while(comanda !== 'quit') {
	comanda = prompt('Selectati o actiune: add, remove, display sau quit.');
		if(comanda === 'add') {
			add();
		}
		else if(comanda === 'remove') {
			remove();
		}
		else if(comanda === 'display') {
			display();
		}
	}
}
alert('Multumim pentru timpul acordat!');
