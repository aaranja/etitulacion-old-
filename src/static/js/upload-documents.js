 $(document).ready(function(){

                // show buttons if files exist on server
                if($('#actaD').prop('checked') === false){
                    alert('no hay acta');
                    document.getElementById('actaB').style.display = "block";
                }
                if($('#curpD').prop('checked') === false){
                    document.getElementById('curpB').style.display = "block";
                }
                if($('#cdiD').prop('checked') === false){
                    document.getElementById('cdiB').style.display = "block";
                }
                if($('#cdbD').prop('checked') === false){
                    document.getElementById('cdbB').style.display = "block";
                }

                // show fileview on frame and show delete button
                $('.clearablefileinput').on('change', function(){
                    // Validate type file
                    var fileName = $(this).get(0).files[0].name
                    var idxDot = fileName.lastIndexOf(".") + 1;
                    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();

                    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"|| extFile=="pdf"){
                        var id = $(this).attr('value');

                        // display button and set checked to false
                        document.getElementById(id+'B').style.display = "block";
                        document.getElementById(id+'L').style.display = "block";
                        $( "#"+id+'D').prop('checked', false);
                        
                        // display document on frame
                        document.getElementById(id+'F').src=URL.createObjectURL($(this).get(0).files[0])+"#toolbar=0&navpanes=0";
                }else{
                    alert("Sólo archivos jpg/jpeg, png y pdf están permitidos!");
                    $(this).val('')
                }   
                });

   

                // remove file for frame and server
                $('.del-label').on('click', function(){
                    $(this).css({"display":"none"}); // hide delete button
                    id =$(this).attr('id');
                    id = id.substring(0, id.length - 1); // get id of button

                    document.getElementById(id+'F').src=""; // remove frame document
                    // remove file from iput file
                    if(id==='acta')  $("#id_acta_de_nacimiento").val('');
                    else if (id==='cdi')  $("#id_certificado_de_ingles").val('');
                    else if (id==='curp')  $("#id_cURP").val('');
                    else if (id==='cdb')  $("#id_certitificado_de_bachiller").val('');
                });
            });