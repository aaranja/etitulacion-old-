var fase=6;
$(function() {
		var btnRedirige=$('#btn-redirige');
		var tituloFase=$('#fase-title');
		var descripcionFase=$('#fase-description');
		switch(fase){
			case 1:
				$('#step-1').addClass('current');
				btnRedirige.html('Step 1');
				tituloFase.text('Step 1');
				descripcionFase.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Nullam quis iaculis sem. Suspendisse gravida ac tellus vel faucibus. Aenean dapibus lorem ut turpis fringilla, eget tempus enim tincidunt. Aenean eu tempor mi.');
			break;
			case 2:
				$('#step-2').addClass('current');
				$('#step-2').prevAll().addClass('complete');
				btnRedirige.html('Step 2');
				tituloFase.text('Step 2');
				descripcionFase.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Nullam quis iaculis sem. Suspendisse gravida ac tellus vel faucibus. Aenean dapibus lorem ut turpis fringilla, eget tempus enim tincidunt. Aenean eu tempor mi.');
			break;
			case 3:
				$('#step-3').addClass('current');
				$('#step-3').prevAll().addClass('complete');
				btnRedirige.html('Step 3');
				tituloFase.text('Step 3');
				descripcionFase.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Nullam quis iaculis sem. Suspendisse gravida ac tellus vel faucibus. Aenean dapibus lorem ut turpis fringilla, eget tempus enim tincidunt. Aenean eu tempor mi.');			
				break;
			case 4:
				$('#step-4').addClass('current');
				$('#step-4').prevAll().addClass('complete');
				btnRedirige.html('Step 4');
				tituloFase.text('Step 4');
				descripcionFase.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Nullam quis iaculis sem. Suspendisse gravida ac tellus vel faucibus. Aenean dapibus lorem ut turpis fringilla, eget tempus enim tincidunt. Aenean eu tempor mi.');
			break;
			case 5:
				$('#step-5').addClass('current');
				$('#step-5').prevAll().addClass('complete');
				btnRedirige.html('Step 5');
				tituloFase.text('Step 5');
				descripcionFase.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Nullam quis iaculis sem. Suspendisse gravida ac tellus vel faucibus. Aenean dapibus lorem ut turpis fringilla, eget tempus enim tincidunt. Aenean eu tempor mi.');
			break;
			case 6:
				$('#step-6').addClass('current');
				$('#step-6').prevAll().addClass('complete');
				btnRedirige.html('Step 6');
				tituloFase.text('Step 6');
				descripcionFase.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Nullam quis iaculis sem. Suspendisse gravida ac tellus vel faucibus. Aenean dapibus lorem ut turpis fringilla, eget tempus enim tincidunt. Aenean eu tempor mi.');
			break;
			default:
				btnRedirige.html('Iniciar');
				tituloFase.text('Comenzar proceso');
				descripcionFase.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Nullam quis iaculis sem. Suspendisse gravida ac tellus vel faucibus. Aenean dapibus lorem ut turpis fringilla, eget tempus enim tincidunt. Aenean eu tempor mi.');
			break;
		}
	});

	window.addEventListener('click',(e)=>{
		console.log(e);
		if(e.target.id=="btn-redirige"){
			switch(fase){
				case 1:
					$(location).attr('href','https://dam.ngenespanol.com/wp-content/uploads/2019/06/mirada-perros.png');
				break;
				case 2:
					$(location).attr('href','https://estaticos.elperiodico.com/resources/jpg/1/6/gato-1502194230861.jpg');
				break;
				case 3:
					$(location).attr('href','https://img.huffingtonpost.com/asset/5c8ad782230000d50423cebe.jpeg?ops=scalefit_630_noupscale');
				break;
				case 4:
					$(location).attr('href','https://www.lavanguardia.com/r/GODO/LV/p6/WebSite/2019/04/02/Recortada/img_mrius_20190402-141602_imagenes_lv_terceros_gato_nombre2-328-kLmH-U461425413181OZB-992x558@LaVanguardia-Web.jpg');
				break;
				case 5:
					$(location).attr('href','https://www.hola.com/imagenes/estar-bien/20180831128704/ronroneo-gatos-causas/0-595-638/gato-ronroneo-1-t.jpg?filter=w600&filter=ds75');
				break;
				case 6:
					$(location).attr('href','https://misanimales.com/wp-content/uploads/2016/10/crecen-los-gatos.jpg');
				break;
				default:
					$(location).attr('href','https://misanimales.com/wp-content/uploads/2016/10/crecen-los-gatos.jpg');
				break;
			}
		}
	});

