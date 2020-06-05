$(document).ready(function(){
	const cm = document.querySelector('.custom-cm');
	var idFila="";
	//metodo que oculta o muestra el context-menu
	function showContextMenu(show = true) {
		cm.style.display=show ? 'inline-block': 'none'; 
	}		
	//click derecho sobre una fila que despliega el context-menu
	window.addEventListener('contextmenu',(e)=>{
		console.log(e.toElement);
		e.preventDefault();
		console.log(e);
		var clase = e.path[1].className;
		clase = clase.substr(0,10);
		idFila = e.path[1].id;
		//idFila=e.target.parentElement.id; //guardamos valor de fila seleccionada
		if(clase=="row-custom"){ //"row-custom" es el nombre de la clase de cada fila
			showContextMenu(true);
			cm.style.top=e.y+cm.offsetHeight > window.innerHeight ? window.innerHeight - cm.offsetHeight +'px' : e.y+'px';
			cm.style.left=e.x+cm.offsetWidth > window.innerWidth ? window.innerWidth - cm.offsetWidth +'px' : e.x+'px';
		}
	});
	//click sobre la opcion del context-menu
	window.addEventListener('click',(e)=>{
		if(e.srcElement.className!='custom-cm_item'){ //"custom-cm_item" es el nombre de la clase de cada opcion del context-menu
			showContextMenu(false);
		}else{
			//ejecutar acciones segun la opcion
			switch(e.target.innerText){
				case 'Uno':
				break;
				case 'Dos':
				break;
				case 'Generar carta de no inconvenientes':
				showContextMenu(false);
				window.location=idFila+"/carta-no-inconveniencia/";
				break;
				case 'Validar documentación':
				showContextMenu(false);
				window.location="validar-documentos/"+idFila+'/';
				break;
			}
		}
	});
	//cerrar context-menu con tecla ESC
	window.addEventListener('keydown',(e)=>{
		if(e.keyCode==27)
			showContextMenu(false);
	});
});